from django.shortcuts import HttpResponse,render
from datetime import datetime,timedelta

def datetimee(request):
    now = datetime.now()
    return HttpResponse(f"current datetime is {now}") 

def offset(request):
    now = datetime.now()
    offset=4
    four_before=now-timedelta(hours=offset)
    four_after=now+timedelta(hours=offset)
    HTML=f"<html><head><title>something</title></head>"\
        f"<p>current time is: {now}"\
        f"<p>four houres after is: {four_after}"\
        f"<p>four houres before is: {four_before}"
    return HttpResponse(HTML)
