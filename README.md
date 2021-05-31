# React/Django Tic-Tac-Toe

### Running backend:
  python3 -m venv env  
  source env/bin/activate  
  pip3 install django  
  pip3 install djangorestframework  
  pip3 install django-cors-headers  
  python3 manage.py runserver 

### Running frontend:
  npm start

### Kill port:
  sudo lsof -t -i tcp:8000 | xargs kill -9

### Flush all data:
  python3 manage.py flush
