# Stability AI Text-to-Image Generator

This Django application generates three images in parallel using the Stability AI's Text-to-Image generation API. The application uses Celery for parallel processing to manage asynchronous API calls.

## Features

- **Django Integration:** Handles API requests through Django views.
- **Celery Integration:** Uses Celery with Redis as the broker for asynchronous task management.
- **Parallel Image Generation:** Generates three images in parallel using Celery groups.

## Prerequisites

- Python 3.7+
- Django 3.x+
- Redis
- Stability AI Account (with API key)

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/priyanshukatiyar14/stability-ai-integration-api.git
cd stability-ai-integration-api
```

### 2. Create and Activate Virtual Environment

# Create a virtual environment

```bash
python -m venv venv
```

# Activate the virtual environment

# On Windows

```bash
venv\Scripts\activate
```

# On macOS/Linux

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the project root and add your Stability AI API key:

```bash
STABILITY_AI_API_KEY=your_api_key
REDIS_URL=your_redis_url
SECRET_KEY=your_secret_key
```

### 5. Configure Django Settings

Ensure your `settings.py` is configured with Redis as the broker for Celery:

```python
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
```

### 6. Migrate the Database

Run the following command to apply the migrations and set up the database:

```bash
python manage.py migrate
```

### 7. Start Redis Server

Ensure Redis is running if using local url:

```bash
redis-server
```

### 7. Start Celery Worker

Run the Celery worker to handle background tasks:

```bash
celery -A stability_ai worker -P eventlet
```

### 8. Start Django Server

Finally, start the Django development server:

```bash
python manage.py runserver
```

## Usage

### Generate Images

Send a GET request to the `/generate_images/` endpoint to trigger image generation:

```bash
http://localhost:8000/prompt/generate-images/
```

The application will generate three images in parallel using the provided prompts and return the task IDs for each.

### Monitor Tasks

You can monitor the tasks using the Celery command line or Flower (if installed).

### Storing Image Data (Bonus)

The application also simulates storing the generated image URLs in the Django database. The model used for this is `GeneratedImage`.

## Contact

For any inquiries or support, please reach out to [priyanshukatiyar111@gmail.com](mailto:priyanshukatiyar111@gmail.com).
