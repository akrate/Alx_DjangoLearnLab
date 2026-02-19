INSTALLED_APPS = [
    # ...
    'rest_framework',
    'rest_framework.authtoken',
    'accounts',
    'posts',
    'django_filters',
]

AUTH_USER_MODEL = 'accounts.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_PAGE_SIZE': 10,
}