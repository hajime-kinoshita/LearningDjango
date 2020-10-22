from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

# Create your views here.

def index(request):
#    return HttpResponse("Hello, Django!")


#    now = datetime.now()

#    html_content = "<html><head><title>Hello, Django</title></head><body>"
#    html_content += "<strong>Hello Django</strong> on " + now.strftime("%A, %d %B, %Y at %X")
#    html_content += "</body></html>"

#    return HttpResponse(html_content)


    now = datetime.now()

    return render(
        request,
        "HelloDjangoApp/index.html",
        {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )