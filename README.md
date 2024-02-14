# FastAPI Application

This is a FastAPI application that provides CRUD (Create, Read, Update, Delete) operations for managing items and user authentication.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd <project_directory>
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `.env` file in the project directory.

2. Define the following environment variables in the `.env` file:

    ```plaintext
    MONGODB_URI=<your_mongodb_uri>
    DATABASE_NAME=<your_database_name>
    SECRET_KEY=<your_secret_key>
    ```

    - `MONGODB_URI`: The URI for your MongoDB instance.
    - `DATABASE_NAME`: The name of the MongoDB database to use.
    - `SECRET_KEY`: A secret key used for JWT token generation.

## Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
