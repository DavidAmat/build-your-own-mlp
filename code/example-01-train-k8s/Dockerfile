FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Locate entrypoint to run
COPY bin/entrypoint /entrypoint

# Execute permissions
RUN chmod +x /entrypoint

ENTRYPOINT ["/entrypoint"]