import os
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# ADD --MA-- para se usar em ambiente de programação
load_dotenv(BASE_DIR / '.env')

# ADD --MA-- a chave poderá ser gerada, djecrety.ir
SECRET_KEY = os.environ.get('SECRET_KEY', default='1234567890qwertyuiopasdfghjklç')

# ADD -- MA-- It allows: things like true, True, TRUE, 1, "1", TrUe, t, T
DEBUG = os.getenv("DEBUG", 'False').lower() in ('true', '1', 't')

# ADD --MA-- poderás e deverás colocar também .railway.app
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS','127.0.0.1,localhost').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webapp', # ADD --MA-- o nosso projecto
    'cloudinary', # ADD --MA-- necessário para usarmos o cloudinary
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # ADD --MA-- necessário para usarmos whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'railway.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'railway.wsgi.application'


# ADD --MA-- nas variaveis de ambiente poderás e deverás colocar os dados para um postgresql, eu uso o https://bit.io/
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600,
        conn_health_checks=True,
    )
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ADD --MA-- nosso idioma
LANGUAGE_CODE = 'pt-PT'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

# ADD --MA-- parte das static files , onde o whitenoise irá funcionar
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# JUST IN CASE
if not os.path.isdir(STATIC_ROOT):
    os.makedirs(STATIC_ROOT, mode=0o755)
    
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ADD --MA-- parte da configuração do https://cloudinary.com/
cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key=os.environ.get("CLOUDINARY_API_KEY"),
    api_secret=os.environ.get("CLOUDINARY__API_SECRET"),
    secure=True,
)
