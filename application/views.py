from django.shortcuts import render
from django.http import StreamingHttpResponse
import time

def home(request):
    return render(request, 'home.html', {})

def automate_run(request):    
    response = StreamingHttpResponse(automate_foo(), content_type="application/json")
    # https://stackoverflow.com/a/78177230/126833
    response["Cache-Control"] = "no-cache"  # prevent client cache
    response["X-Accel-Buffering"] = "no"  # Allow Stream over NGINX server    return response
    return response

def automate_foo():
    for i in range(1, 11):
        status = "Step %d" % i
        percentage = i * 10
        json_string = f'{{"status": "{status}","percentage": "{percentage}"}}'
        print(json_string)
        yield json_string
        time.sleep(1) # Do some python task that would take a few seconds to run