# Blog Bridger (WIP)

## Introduction

Blog Bridger is a simple tool that allows Djamgo Rest Framework Developers to set up a simple blog API without worrying about the underlying code. The tool takes care of things like CRUD operations for blog posts, as well as the comment feature for each post.

## Table of Contents

- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#Installation-and-Setup)
- [Testing](#testing)
- [API Documentation](docs/api_docs.md)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

The following instructions will help you install WhisperTime on your local system and have it running.

### Prerequisites

- Python 3.10 or higher
- Pip
- Django Rest Framework

### Installation and Setup
1. Install the package with:

```bash
pip install drfblogbridger
```
2. Include the following settings in your `settings.py` file:
```python
INSTALLED_APPS = [

    'posts',
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

<!-- 1. Clone the repository

```
git clone https://github.com/ade555/WhisperTime.git
```

2. Change directory to the project folder

```
cd WhisperTime
```

3. Create a virtual environment
```
python -m venv env
```

4. Install the project dependencies into your virtual environment

```
pip install -r requirements.txt
```

5. Generate a new secret key

```
python secret_key.py
```

6. Create an environment variable (`.env` file) and include the necessary information from the `.env_sample` file

7. Open your CLI and start the project

```
python manage.py runserer
``` -->

## Contributing

Contributions are welcome! Feel free to open a pull request right away.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
