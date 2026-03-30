from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def set(request):
    request.session["name"] = "Uday"
    request.session["last_name"] = "Kadam"
    request.session["country_visited"] = { "Asia": "India", "Europe": "France" }
    # we can this in settings.py as well using SESSION_COOKIE_AGE = 20
    #request.session.set_expiry(20) 

    return HttpResponse("Session set")

def get(request):
    name = request.session.get("name", "Not set")
    last_name = request.session.get("last_name", "Not set")
    country_visited = request.session.get("country_visited", "Not set")
    session_expiry = request.session.get_expiry_age()

    return HttpResponse(f"Session value: {name} {last_name} {country_visited} (Expires in {session_expiry} seconds)")

def delete(request):
    # del request.session['last_name']
    # del request.session['name']
    request.session.flush()
    request.session.clear_expired()

    return HttpResponse("Session deleted")

def update(request):
    request.session["country_visited"]["Europe"] = "Germany"
    request.session.modified = True

    return HttpResponse("Session updated")
