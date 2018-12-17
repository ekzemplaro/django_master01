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


https://askubuntu.com/questions/227940/uwsgi-cant-find-python-plugin

If you have installed your uwsgi with pip or make (or otherwise made a custom build), your python plugin would be built into the binary and thus not created as a shared library (.so file). 
