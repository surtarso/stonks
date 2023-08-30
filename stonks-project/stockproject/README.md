# Index of `stockproject`
This guide will provide an overview of the key project configuration files and their purposes.

- [asgi.py](#asgipy)
- [celery.py](#celerypy)
- [wsgi.py](#wsgipy)
- [urls.py](#urlspy)
- [settings.py](#settingspy)

Jump to [`mainapp`](../mainapp/)

## asgi.py

The [asgi.py](asgi.py) file is the entry point for the ASGI (Asynchronous Server Gateway Interface) application. It's used to serve Django applications asynchronously and supports real-time features like WebSocket handling. This file is important when deploying Django projects on asynchronous servers, such as Daphne or Uvicorn.

Here's a breakdown of the code snippet line by line:

```python
# Import necessary modules
import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from mainapp.routing import websocket_urlpatterns
```

- The code begins by importing required modules for setting up Django's ASGI (Asynchronous Server Gateway Interface) application using Channels. These modules include `os` for environment variables, `AuthMiddlewareStack` for authentication handling, `ProtocolTypeRouter` for protocol-based routing, `URLRouter` for URL-based routing, and `get_asgi_application` to retrieve the ASGI application instance for Django.

```python
# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockproject.settings')
```

- This line sets the default value for the environment variable `DJANGO_SETTINGS_MODULE` to `'stockproject.settings'`. This specifies the Django settings module to be used for the project's configuration.

```python
# Define the ASGI application using ProtocolTypeRouter
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
```

- Here, the ASGI application is defined using the `ProtocolTypeRouter` from Channels. This router allows handling different protocols (e.g., HTTP and WebSockets) within the same application instance.

- For the "http" protocol, the Django ASGI application instance is obtained using `get_asgi_application()`, which provides a traditional HTTP handling mechanism for Django views.

- For the "websocket" protocol, the `AuthMiddlewareStack` is applied to the `URLRouter`. The `AuthMiddlewareStack` adds authentication support to the WebSocket protocol. Inside the `URLRouter`, the `websocket_urlpatterns` from the `mainapp.routing` module are used. This means that WebSocket connections are routed to the appropriate consumers based on URL patterns defined in `websocket_urlpatterns`.

In summary, this code sets up the ASGI application using Channels to handle both HTTP and WebSocket protocols. It uses different routing mechanisms for these protocols and includes authentication middleware for WebSocket connections. The URL patterns for WebSocket consumers are defined in the `websocket_urlpatterns` variable from the `mainapp.routing` module.

[Back to top](#index-of-stockproject)

## celery.py

The [celery.py](celery.py) file configures the Celery distributed task queue for handling asynchronous processing and background tasks in your Django project. Celery allows you to perform tasks outside the request-response cycle, such as sending emails, processing data, and more. This file defines the Celery instance and sets up the necessary configurations.

Here's a breakdown of the code snippet line by line:

```python
# Import necessary modules
from __future__ import absolute_import, unicode_literals
import os
```

- The code begins by importing required modules. The use of `__future__` indicates that this import is intended to be compatible with both Python 2 and Python 3. The `absolute_import` ensures that explicit relative imports are used.

```python
# Import the Celery library and Django settings
from celery import Celery
from django.conf import settings
```

- The code imports the `Celery` class from the Celery library and the `settings` module from Django.

```python
# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockproject.settings')
```

- This line sets the default value for the environment variable `DJANGO_SETTINGS_MODULE` to `'stockproject.settings'`. This specifies the Django settings module to be used for the project's configuration.

```python
# Create a Celery instance named 'app' for the 'stockproject'
app = Celery('stockproject')
```

- An instance of the `Celery` class is created with the name `'stockproject'`. This name will be used to identify the Celery instance.

```python
# Disable the default UTC timezone for Celery
app.conf.enable_utc = False
```

- The UTC timezone is disabled for the Celery instance. This indicates that Celery will use the local timezone instead of UTC.

```python
# Set the timezone for the Celery instance
app.conf.update(timezone='America/Sao_Paulo')
```

- The timezone for the Celery instance is set to `'America/Sao_Paulo'`, which is the timezone for São Paulo, Brazil.

```python
# Configure Celery using Django settings
app.config_from_object(settings, namespace='CELERY')
```

- The Celery instance is configured using the Django settings. The namespace `'CELERY'` indicates that Celery-related settings should be retrieved from the `settings` module.

```python
# Define Celery beat schedule (commented out for now)
app.conf.beat_schedule = {
    # 'every-10-seconds': {
    #     'task': 'mainapp.tasks.update_stock',
    #     'schedule': 10,
    #     'args': (['ITSA4', 'CIEL3'],)
    # },
}
```

- This section defines the Celery beat schedule, which specifies periodic tasks to be executed. The example schedule is commented out but demonstrates how to define a task to run every 10 seconds using the `update_stock` task from the `mainapp.tasks` module with specific arguments.

```python
# Autodiscover and register Celery tasks from installed apps
app.autodiscover_tasks()
```

- This line automatically discovers and registers Celery tasks from all installed apps.

```python
# Define a debug task for Celery
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
```

- This section defines a simple Celery task named `debug_task`. The `@app.task(bind=True)` decorator indicates that the task is bound to the task instance. When the task is executed, it prints information about the request. This task can be used for debugging purposes.

In summary, this code sets up a Celery instance for the Django project named `'stockproject'`. It configures Celery settings using Django settings, defines Celery beat schedules for periodic tasks (currently commented out), autodiscovers and registers tasks from installed apps, and includes a debug task. The Celery instance is configured to use the local timezone.

[Back to top](#index-of-stockproject)

## wsgi.py

The [wsgi.py](wsgi.py) file serves as the entry point for the WSGI (Web Server Gateway Interface) application. It's used to serve Django applications on traditional web servers like Apache or Nginx. The WSGI server communicates with the Django application to handle incoming HTTP requests and generate responses.

Here's a breakdown of the code snippet line by line:

```python
# Import the 'os' module
import os
```

- This line imports the built-in `os` module, which provides a way to interact with the operating system.

```python
# Import the 'get_wsgi_application' function from 'django.core.wsgi'
from django.core.wsgi import get_wsgi_application
```

- The `get_wsgi_application` function is imported from the `django.core.wsgi` module. This function is used to obtain the WSGI (Web Server Gateway Interface) application for a Django project.

```python
# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockproject.settings')
```

- This line sets the default value for the environment variable `DJANGO_SETTINGS_MODULE` to `'stockproject.settings'`. This specifies the Django settings module to be used for the project's configuration.

```python
# Obtain the WSGI application for the Django project
application = get_wsgi_application()
```

- This line uses the `get_wsgi_application` function to obtain the WSGI application instance for the Django project. This application instance can be used to serve the Django project using a web server that supports the WSGI protocol.

In summary, this code sets up the WSGI application for the Django project named `'stockproject'`. It ensures that the appropriate Django settings module is used and obtains the WSGI application instance, which can be used to serve the Django project using a compatible web server.

[Back to top](#index-of-stockproject)

## urls.py

The [urls.py](urls.py) file defines the URL patterns for routing incoming HTTP requests to appropriate view functions in your Django application. Each URL pattern is associated with a specific view that renders content or performs actions in response to the request. This file is crucial for mapping URLs to corresponding views.

Here's a breakdown of the code snippet line by line:

```python
# Import necessary modules and functions from Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
```

- These lines import various modules and functions from Django that are needed for URL routing, including the admin site and handling static files.

```python
# Define URL patterns for the application
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

- This section defines the URL patterns for the application. It consists of a list of URL patterns that will be matched to corresponding views. Here's what's happening:
  - The first pattern maps the URL path `'admin/'` to the admin site interface.
  - The second pattern uses the `include` function to include URL patterns defined in the `'mainapp.urls'` module. This allows for modular URL configuration.
  - The `+ static(...)` part adds a pattern to serve static files during development. It's used to serve files like CSS, JavaScript, and images. The `settings.STATIC_URL` specifies the URL prefix, and `settings.STATIC_ROOT` is the absolute filesystem path to the directory where static files are collected.

```python
# Define a custom handler for HTTP 404 errors
handler404 = "mainapp.views.http_404_error"
```

- This line specifies a custom view function to be used when a 404 (Not Found) error occurs. In this case, the view function `http_404_error` from the `'mainapp.views'` module will be invoked. This allows you to customize the appearance and behavior of your 404 error page.

In summary, this code defines the URL patterns for your Django application using the `urlpatterns` list. It includes patterns for the admin site and routes to views defined in the `'mainapp.urls'` module. It also sets up a handler for customizing the behavior of HTTP 404 errors. Additionally, it configures static file serving during development using the `static` function.

[Back to top](#index-of-stockproject)

## settings.py

The [settings.py](settings.py) file is a vital configuration file that holds various settings for your Django project. It includes database settings, installed applications, middleware configurations, authentication settings, static and media file configurations, internationalization settings, and more. This file plays a central role in customizing the behavior of your Django application.

Here's a detailed explanation of the Django settings code:

```python
# Import required modules and functions
from pathlib import Path
```

- This line imports the `Path` class from the `pathlib` module. This class provides a way to work with file and directory paths in a more object-oriented manner.

```python
# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent
```

- This line uses the `Path` class to define the base directory of the project by going up two levels from the location of the current file (`__file__`). This is a common practice to reference other directories and files within the project.

```python
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# Set the secret key used in production (not secure in this example)
SECRET_KEY = 'django-insecure-h!&-fg8y+^*_5npjhdrt&y7(ifp^1vg5a&e49563b&#xde153%'
```

- This section includes a security warning and sets the Django `SECRET_KEY` setting. In this example, the key is hard-coded, which is not secure for production environments. In real-world scenarios, you should store the secret key in a secure manner, such as in environment variables.

```python
# Set the debug mode (not suitable for production)
DEBUG = True
```

- This line sets the `DEBUG` mode to `True`, which is not suitable for production environments. Debug mode provides additional error information and traceback details that can be helpful during development but may expose sensitive information in a production environment.

```python
# Allow all hosts (not recommended for production)
ALLOWED_HOSTS = ['*']
```

- This line sets the `ALLOWED_HOSTS` setting to allow all hosts to access the application. In a production environment, you should specify only the trusted domain names that can access your application.

```python
# Define the list of installed applications
INSTALLED_APPS = [
    # ...
]
```

- This section defines the list of installed applications in the Django project. These are Django apps and third-party apps that the project will use.

```python
# Define middleware settings
MIDDLEWARE = [
    # ...
]
```

- This section defines the list of middleware classes that process requests and responses globally before reaching the view functions.

```python
# Set the root URL configuration
ROOT_URLCONF = 'stockproject.urls'
```

- This line sets the root URL configuration for the project, which determines how URLs are matched to view functions.

```python
# Define template settings
TEMPLATES = [
    # ...
]
```

- This section configures the templates for rendering HTML. It specifies template engines, directories, and context processors.

```python
# Set the WSGI and ASGI application
WSGI_APPLICATION = 'stockproject.wsgi.application'
ASGI_APPLICATION = "stockproject.asgi.application"
```

- These lines set the WSGI (Web Server Gateway Interface) and ASGI (Asynchronous Server Gateway Interface) applications for the project.

```python
# Configure the database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

- This section configures the database settings for the project. In this example, it uses SQLite as the database backend.

```python
# Configure password validation
AUTH_PASSWORD_VALIDATORS = [
    # ...
]
```

- This section configures password validation rules, such as requiring minimum length, similarity, and common password checks.

```python
# Configure internationalization and localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True
```

- These lines configure the internationalization and localization settings. They define the default language, time zone, and whether the application should use internationalization and time zone support.

```python
# Configure static files settings
STATIC_URL = '/static/'
```

- This line configures the URL prefix for serving static files, such as CSS, JavaScript, and images.

```python
# Configure the default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

- This line sets the default primary key field type to `BigAutoField`, which is suitable for databases that support big integers as primary keys.

```python
# Configure Celery settings
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
# ... (other Celery settings)
```

- This section configures Celery settings, such as the broker URL for the message queue (Redis in this case) and other Celery-related options.

```python
# Configure channel layers for Django Channels
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
```

- This section configures channel layers for Django Channels, which allows real-time communication over WebSockets. It specifies the backend (Redis in this case) and related configuration.

```python
# Configure session settings
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 86400  # Seconds (1 day)
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_NAME = 'DSESSIONID'
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = False
```

- This section configures session settings, such as session expiration, session cookie settings, and security-related settings.

In summary, this Django settings code configures various aspects of a Django project, including security settings, database configuration, internationalization, static files, Celery for task scheduling, Django Channels for real-time communication, and session management settings. These settings help customize the behavior of the Django project and ensure its proper functioning. Remember that some settings, such as the secret key and debug mode, need to be configured securely for production environments.

[Back to top](#index-of-stockproject)

## Conclusion

Understanding these key configuration files will help you navigate and configure your Django project effectively. Feel free to explore each file's content to tailor your project to your specific requirements.

For more detailed information, refer to the official [Django Documentation](https://docs.djangoproject.com/en/3.2/).

If you have any questions or need assistance, please don't hesitate to ask!
