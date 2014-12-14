# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from django.db.models import FieldDoesNotExist

from rest_framework.serializers import ModelSerializer


class NullModelSerializer(ModelSerializer):
    def to_native(self, obj):
        ret = self._dict_class()
        ret.fields = self._dict_class()

        for field_name, field in self.fields.items():
            if field.read_only and obj is None:
                continue
            field.initialize(parent=self, field_name=field_name)
            key = self.get_field_key(field_name)
            value = field.field_to_native(obj, field_name)
            if not isinstance(value, bool) and not value:
                value = None
            method = getattr(self, 'transform_%s' % field_name, None)
            if callable(method):
                value = method(obj, value)
            if not getattr(field, 'write_only', False):
                ret[key] = value
            ret.fields[key] = self.augment_field(field, field_name, key, value)

        return ret

    def restore_fields(self, data, files):
        reverted_data = {}

        if data is not None and not isinstance(data, dict):
            self._errors['non_field_errors'] = ['Invalid data']
            return None

        for field_name, field in self.fields.items():
            field.initialize(parent=self, field_name=field_name)

            # special method del null fields
            if not field.read_only:
                try:
                    _field_model, _model, _direct, _m2m = self.Meta.model._meta.get_field_by_name(field_name)
                except FieldDoesNotExist:
                    _field_model, _model, _direct, _m2m = None, None, None, None

                try:
                    if _direct and not _field_model.null and data[field_name] is None:
                        _data = data.copy()
                        _data[field_name] = ''

                        try:
                            field.field_from_native(_data, files, field_name, reverted_data)
                        except ValidationError as err:
                            self._errors[field_name] = list(err.messages)
                        continue
                except KeyError:
                    pass

            try:
                field.field_from_native(data, files, field_name, reverted_data)
            except ValidationError as err:
                self._errors[field_name] = list(err.messages)

        return reverted_data