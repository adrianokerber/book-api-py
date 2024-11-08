# Book API (Generated with Cursor AI)

A simple REST API for managing books built with FastAPI.

> ⚠️ Disclaimer: This is a simple example generated using [Cursor AI](https://www.cursor.com/). In a real application, you should use a database and handle errors and edge cases more gracefully.

## First steps

After cloning the repository, run the following commands to set up the project:

```bash
# 1. Navigate to the project directory
cd your-project-name

# 2. Create a virtual environment (PS: py_env is just an example name, change as you like)
python -m venv py_env

# 3. Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Install the dependencies
pip install -r requirements

# 5. Run the application
uvicorn main:app --reload
``` 

This example includes:

1. A FastAPI application setup
2. A Pydantic model for data validation
3. In-memory storage (you can replace this with a database in a real application)
4. CRUD endpoints:

    - GET /books - List all books
    - GET /books/{id} - Get a specific book
    - POST /books - Create a new book
    - PUT /books/{id} - Update a book
    - DELETE /books/{id} - Delete a book

You can test the API using the automatic interactive documentation at:

- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/redoc (ReDoc)

Example request to create a book using curl:

```bash
curl -X 'POST' \
  'http://localhost:8000/books' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "price": 9.99,
  "in_stock": true
}'
```

---

### Python setup for Linux:

On my machine that has a Windows 11, I used WSL2 (With Ubuntu) as the target system to run the commands.

So to install Python on Linux for this project, I followed these steps:

```bash
# Install Python and pip

# Update package list   
sudo apt update

# Install Python and pip
sudo apt install python3 python3-pip

# Create a Virtual Environment (Recommended)
# Install venv
sudo apt install python3-venv

# Create the virtual environment
python3 -m venv py_env

# Activate the virtual environment
source py_env/bin/activate

# Example: Install the dependencies
pip install <package_name>
```