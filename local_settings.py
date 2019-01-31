ALLOWED_HOSTS = [ '*' ]

DATABASES = { 
    'default': { 
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'dataroom',
        'USER': 'dataroom',
        'PASSWORD': 'secret'
    } 
} 

INSTALLED_APPS += [
    'notes',
    'sites',
]
