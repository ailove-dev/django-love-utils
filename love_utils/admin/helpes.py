# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

from django.conf import settings


def imageable_field(image, short_description='Image', size=settings.FILEBROWSER_ADMIN_THUMBNAIL):
    def image_thumbnail(self, object):
        image = eval(image_thumbnail.image)

        if image and os.path.exists(settings.MEDIA_ROOT + image.path):
            return '<img src="' + image.version_generate(size).url + '" />'
        else:
            return 'No Image'

    image_thumbnail.__dict__.update({'short_description': short_description, 'allow_tags': True, 'image': image})

    return image_thumbnail