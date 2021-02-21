FROM python:3.8.8-alpine3.12

RUN apk add --no-cache libressl-dev musl-dev libffi-dev python3-dev postgresql-dev

LABEL maintainer="Brian Amolo <amolo@dalasystems.com, railamolo@gmail.com>"

COPY . /src
WORKDIR /src

EXPOSE 8080

RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "'0.0.0.0:8080'", "index:app" ]
