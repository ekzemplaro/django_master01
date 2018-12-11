from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    message = ""
    message += 'app02 からのメッセージです。<br />'
    message += str(request.user.id) + '&nbsp;&nbsp;'
    message += request.user.username + '<p />'
    dd = {
        'hour': datetime.now().hour,
        'minute': datetime.now().minute,
        'message': message,
    }
    return render(request, 'app02.html', dd)
