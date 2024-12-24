version ?= 1 
p ?= 80
run:
	python3.9 manage.py runserver 0.0.0.0:$(p)
build:
	echo "build"
	test -f OVP.tar.gz && rm -rf OVP.tar.gz
	tar cvf OVP.tar.gz .
	sudo docker build -t huangchengwu6904/hi-app:OVP . 

up:
	python3.9 manage.py makemigrations 
	python3.9 manage.py  migrate
start:
	docker-compose up -d 


