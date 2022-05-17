FROM python:3.9

RUN apt-get update -y
RUN apt-get upgrade -y

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./blog_app_backend/requirements.txt ./
RUN pip3 install -r requirements.txt

COPY ./blog_app_backend ./blog_app_backend
CMD [ "python3", "./blog_app_backend/manage.py", "runserver", "0.0.0.0:8000"]
