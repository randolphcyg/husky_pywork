from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print(username, password)
    return render(request, "login_1722441026.html")

def redirect_login(request):
    return redirect('/login/')

def index(request):
    return render(request, "index_1722441026.html")

