# -*- coding: utf-8 -*-

from django.contrib import admin


class OrderableAdmin(admin.ModelAdmin):
    list_display = list_editable = exclude = ('position',)

    class Meta:
        abstract = True

    class Media:
        js = (
            'love_utils/js/orderable.js',
        )