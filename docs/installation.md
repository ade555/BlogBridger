## Getting Started

The following instructions will help you install Blog Bridger on your local system and have it running.

### Prerequisites

- Python 3.8 or higher
- Pip
- Django Rest Framework

### Installation and Setup
1. Install the package with:

    ```bash
    pip install drf_blog_bridger
    ```

2. Include the following settings in your `settings.py` file:

    ```python title="settings.py"

    INSTALLED_APPS = [

        'blog_bridger_drf',
        'rest_framework',
    ]

    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES':[
            'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        ]
    }
    ```

3. Include the following in your project level `urls.py` file:

    ```python title="urls.py"
    path('api/posts/', include('blog_bridger_drf.urls')),
    ```

4. Run `python manage.py migrate` to migrate the models into your database. You should read the [API reference](api_docs.md) to understand how the endpoints work.
