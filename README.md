# Demo-Python-Web-Project-

Explanation:
✅ Uses Python 3.10 as the base image

✅ Sets the working directory to /app

✅ Copies all files from your project to the container

✅ Installs dependencies from requirements.txt

✅ Exposes port 5000

✅ Runs the Flask app using gunicorn for production

How to Build and Run:

# Build the Docker image
docker build -t flask-app .

# Run the container
docker run -p 5000:5000 flask-app


This will start your Flask application inside a Docker container, accessible at http://localhost:5000/. 🚀
