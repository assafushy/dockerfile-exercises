Exercise 2: Create a Python Application Image

Description: This image will run a simple Python application that displays "Hello, Docker!".

Before Starting your Dockerfile:

1. Create a directory named `exercise2-flask`.
2. create a file named `app.py` with the following contents.

File: app.py

```python
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

Instructions:

1. Use the latest Python image as your base.
2. Create a directory named `app` for your Python script.
3. Set this directory as your work directory.
4. Copy your Python script into the newly created directory.
5. Install the `flask` library for your Python script to use.(use "pip install flask" command)
6. Run the script when the container starts.(use "python app.py" command)

Docker commands:

```bash
  docker build -t my-python-app .
  docker run -p 3030:5000 my-python-app
```
