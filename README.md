# Django Project Setup

### Getting Started

To get the project up and running, follow these steps:

1.  **Clone the repository and navigate into the project directory.**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Run the setup script below.** This will create a virtual environment, install dependencies, run migrations, and start the development server.

    **Note:** This script is for macOS and Linux. If you are on Windows, you will need to activate the virtual environment manually with `venv\Scripts\activate` and then run the subsequent commands.

    ```bash
    # Create and activate a virtual environment
    python -m venv venv && source venv/bin/activate

    # Install dependencies from requirements.txt
    pip install -r requirements.txt

    # Apply database migrations
    python manage.py migrate

    # Start the development server
    python manage.py runserver
    ```

3.  **Access the project.** The development server will be running at `http://127.0.0.1:8000/`.
