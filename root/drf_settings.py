REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'shared.paginations.CustomPageNumberPagination',
    'PAGE_SIZE': 25

}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Book shop with drf',
    'DESCRIPTION': 'Drf Book shop',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'COMPONENT_SPLIT_REQUEST': True,
}
