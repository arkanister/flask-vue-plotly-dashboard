FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1

MAINTAINER arkanister "arkanister.dev@gmail.com"

WORKDIR /app

COPY backend/src/ .

ADD ./backend/requirements.pip /
ADD ./dockerfiles/backend/gunicorn.py /

# required for healthy check
RUN apt update && apt install curl -y

# install requirements
RUN pip install gunicorn==20.0 && \
    pip install -r /requirements.pip

ENTRYPOINT ["gunicorn", "-c", "/gunicorn.py", "wsgi:application"]
EXPOSE 5000