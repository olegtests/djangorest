# djangorest
solution django RestApi with docker and docker-compose

to execute the application:
1. download sources:
  git clone https://github.com/olegtests/djangorest.git ~/blog
  
2. goto project folder: 
  cd ~/blog
  
3. run docker compose:
  docker-compse up
   or as a daemon
  docker-compse up -d
  
4. web application:
  a. get all posts 
    http://127.0.0.1:8000/posts
  b. get api description
    http://127.0.0.1:8000/docs
  
