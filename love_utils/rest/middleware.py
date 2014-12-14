# -*- coding: utf-8 -*-

from django.conf import settings
from rest_framework.status import is_success, is_client_error, is_server_error

REST_API_APP_NAME = getattr(settings, 'REST_API_APP_NAME', 'api')


class StatusResponseMiddleware(object):
    def process_template_response(self, request, response):
        if request.resolver_match.app_name == REST_API_APP_NAME:
            response.data = {'status': 'unknown', 'data': response.data}

            if is_success(response.status_code):
                response.data['status'] = 'success'

                if request.method == 'POST' and not response.data['data']:
                    del response.data['data']
            elif is_client_error(response.status_code) or is_server_error(response.status_code):
                response.data['status'] = 'error'

        return response