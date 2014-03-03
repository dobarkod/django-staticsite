# -*- coding: utf-8 -*-

from django.conf import settings
from django.template.loader import render_to_string


def google_analytics(self):
    """Context processor
    for render analytics code.

    Insert in template:

        {{ google_analytics_code }}
    """
    if settings.DEBUG is not False:
        return {
            'google_analytics_code': render_to_string('analytics.html', {
                'ANALYTICS_CODE': settings.GOOGLE_ANALYTICS_KEY,
                'ANALYTICS_DOMAIN': settings.GOOGLE_ANALYTICS_DOMAIN
            })
        }
    else:
        return {'google_analytics_code': ""}
