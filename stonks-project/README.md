This section contains the project that is structured to manage various functionalities related to stock tracking, alerts, and more. The project is organized into the [mainapp](mainapp) directory, which holds the main application functionalities, and the [stockproject](stockproject) directory, which contains the project settings and configurations.

### `mainapp`

The [mainapp](mainapp) directory is where the core functionalities of the project reside. It includes:

- `migrations/`: Auto-generated database migration files.
- `static/`: Static files like CSS, JavaScript, and images.
- `templates/`: HTML templates for rendering views.
- `views/`: View functions handling user requests.
- `forms.py`: Django forms for user input validation.
- `models.py`: Database models for storing data.
- `tasks.py`: Asynchronous tasks using libraries like Celery.
- `urls.py`: URL routing for mapping views to URLs.
- `consumers.py`: Associated search data in the database for the respective assets and users.
- `routing.py`: Handle WebSocket connections and route them to appropriate consumers.

### `stockproject`

The [stockproject](stockproject) directory contains project-level settings and configurations:

- `settings.py`: Project-wide settings such as installed apps, database configuration, and more.
- `urls.py`: Project-level URL routing and URL configuration.
- `asgi.py`: Enables support for asynchronous web servers and real-time applications.
- `celery.py`: Sets up the Celery distributed task queue to handle asynchronous processing and background tasks.
