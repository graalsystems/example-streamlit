FROM python:3.11

# Copy the current directory contents into the container at /app
COPY . /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8501

# Run app
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]