from django.apps import AppConfig


class DbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'db'

class DbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'db'

class CppcompilerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cppcompiler'

class JavacompilerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'javacompiler'

class JscompilerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jscompiler'

class CompilerAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'phpcompiler'

class PycompilerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pycompiler'

class TestingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testing'

class CompilerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webcompiler'

