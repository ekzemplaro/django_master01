from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# @login_required
def index(request):
	message = ""
	message += 'app03 からのメッセージです。<br />'
	message += str(request.user.id) + '&nbsp;&nbsp;'
	message += request.user.username + '<p />'
	dd = {
		'hour': datetime.now().hour,
		'minute': datetime.now().minute,
		'message': message,
	}
	return render(request, 'app03/app03.html', dd)
