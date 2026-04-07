TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,   # ✅ must be True
    },
]

ROOT_URLCONF = 'my_first_demo.urls'

DEBUG = True

INSTALLED_APPS = [
    'django.contrib.admin',        # ✅ ADD THIS
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'members',  # your app
]