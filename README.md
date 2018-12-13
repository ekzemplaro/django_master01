# django_master01
Django Master


Ubuntu 18.04

	sudo apt install libmysqlclient-dev

	pip3 install mysqlclient

	sudo apt install uwsgi-core
	sudo apt install uwsgi-plugin-python3

create user 'django'@'localhost' identified by 'tiger123';
create schema django;
grant all on django.* to django@localhost;

