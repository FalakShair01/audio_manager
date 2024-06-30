
---

## Setup Project Locally

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd audio_manager
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   - API Root: `http://127.0.0.1:8000/api/`
   - Admin Interface: `http://127.0.0.1:8000/admin/`

## Authentication

To authenticate, send a POST request to `http://127.0.0.1:8000/api/token/` with the following JSON body:
   ```json
   {
     "username": "admin",
     "password": "123"
   }
   ```
These are the Credentials For my User. If you want to create your own superuser Replace `"admin"` and `"123"` with your superuser credentials.

## API Endpoints

- **List and Create Audio Clips:**
  - `GET /api/audio/`
  - `POST /api/audio/` (multipart form data with fields: `title`, `description`, `audio_file`)

- **Retrieve, Update, and Delete Audio Clip:**
  - `GET /api/audio/{id}/`
  - `PUT /api/audio/{id}/`
  - `PATCH /api/audio/{id}/`
  - `DELETE /api/audio/{id}/`

## Filter

You can filter audio clips using query parameters:
- `GET /api/audio/?title=XYZ`
- `GET /api/audio/?description=XYZ`
- `GET /api/audio/?title=ABC&description=XYZ`

## File Validation

Audio file uploads are validated for file type and size:
- **File Type:** Only accepts certain file types. See [file validation reference](https://stackoverflow.com/questions/3648421/only-accept-a-certain-file-type-in-filefield-server-side).

## Future Enhancements

### 1. Compress File Size

To optimize storage and network bandwidth usage, implement file compression techniques such as:
- **Lossless Compression:** Reduce file size without losing quality using algorithms like gzip or bzip2.

### 2. Asynchronous File Uploads with Celery

Implement Celery to handle asynchronous file upload tasks:
- **Task Queue:** Use Celery to offload file upload tasks to background workers.

---
