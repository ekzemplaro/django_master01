from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    str_out = ""
    str_out += "*** home *** start ***<p />"
    str_out += "ホームです。<p />"
    str_out += str(request.user.id) + "&nbsp;&nbsp;"
    str_out += request.user.username + "<p />"
    str_out += "<a href='app01/'>app01</a><p />"
    str_out += "<a href='app02/'>app02</a><p />"
    str_out += '<a href="accounts/logout/">Logout</a><p />'
    str_out += "*** Dec/11/2018 AM 10:36 ***<p />"
    str_out += "*** home *** end ***<p />"
    return HttpResponse(str_out)
