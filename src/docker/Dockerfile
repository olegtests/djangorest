#from alpine:latest
FROM python:3.6-alpine
 
RUN apk --update add wget git nano virtualenv virtualenvwrapper
ENV PYTHONUNBUFFERED 1
ADD ./blog /home/blog

RUN pip install -r /home/blog/requirements.txt

EXPOSE 8000
RUN cd /home/blog/src
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

