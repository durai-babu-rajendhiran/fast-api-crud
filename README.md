FastAPI Application
This is a FastAPI application that provides CRUD (Create, Read, Update, Delete) operations for managing items and user authentication.

Installation
Clone this repository to your local machine:

bash

git clone <repository_url>
Navigate to the project directory:

bash

cd <project_directory>
Create a virtual environment (optional but recommended):

python -m venv venv
Activate the virtual environment:

On Windows:
venv\Scripts\activate
On macOS and Linux:

bash
source venv/bin/activate
Install the required dependencies:

pip install -r requirements.txt
Configuration
Create a .env file in the project directory.

Define the following environment variables in the .env file:

makefile .env
MONGODB_URI=<your_mongodb_uri>
DATABASE_NAME=<your_database_name>
SECRET_KEY=<your_secret_key>
MONGODB_URI: The URI for your MongoDB instance.
DATABASE_NAME: The name of the MongoDB database to use.
SECRET_KEY: A secret key used for JWT token generation.
Running the Application
To run the FastAPI application, use the following command:

Run App
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
app:app specifies the module and the FastAPI instance within that module.
--host 0.0.0.0 specifies the host address.
--port 8000 specifies the port.
--reload enables auto-reloading so that the server restarts automatically when code changes are detected.
Access the FastAPI application at http://localhost:8000 in your web browser.

API Documentation
Once the application is running, you can access the API documentation (Swagger UI) at
http://localhost:8000/docs 
or the alternative ReDoc interface at 
http://localhost:8000/redoc.
