_THIRD_PARTY_APPS = [
    'friendship'
]

_MAIN_APPS = [
    'applications.users',
    'applications.gifts',
    'applications.squads',
    'applications.wishlists',
]

_CORE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = _CORE_APPS + _MAIN_APPS + _THIRD_PARTY_APPS
