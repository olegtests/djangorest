#from alpine:latest
FROM python:3.6-alpine
 
RUN apk --update add wget git nano 	
ENV PYTHONUNBUFFERED 1
ADD ./ /home/blog

RUN pip install -r /home/blog/requirements.txt

EXPOSE 8000
ENV MANAGE_PY /home/blog/manage.py

RUN python ${MANAGE_PY} makemigrations
RUN python ${MANAGE_PY} migrate
CMD ["python", "/home/blog/manage.py", "runserver", "0.0.0.0:8000"]
