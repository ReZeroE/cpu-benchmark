# Use official Python image
FROM python

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Set the default command (can be overridden)
CMD ["python", "multicore_cpubench.py", "-v", "--processes", "16", "--load", "60000"]
