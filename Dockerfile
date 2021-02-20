
FROM python:3.8.8-alpine3.12

LABEL maintainer="Brian Amolo <amolo@dalasystems.com, railamolo@gmail.com>"

COPY ./app /app
WORKDIR /app

EXPOSE 8080

RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "'0.0.0.0:8080'", "app:app" ]
