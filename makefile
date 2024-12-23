version ?= 1 
p ?= 80
run:
	python3.9 manage.py runserver 0.0.0.0:$(p)
build:
	echo "build"
	cd ../
	tar cvf OVP.tar.gz OVP 
up:
	python3.9 manage.py makemigrations 
	python3.9 manage.py  migrate
	