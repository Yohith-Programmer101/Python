from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
import datetime 

def list_view(request):
    context = {}
    context["dataset"] = PractiseModel.objects.all()
    return render(request, "practiseapp/list_view.html", context)

def index(request):
    now = datetime.datetime.now()
    html = f"Time is {now}"
    return HttpResponse(html)

class class_based_view(ListView):
    model = PractiseModel

def create_view(request):
    context = {}
    form = PractiseForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form 
    return render(request, "practiseapp/create_view.html", context)

def detail_view(request, id):
    context = {}
    context["data"] = PractiseModel.objects.get(id=id)
    return render(request, "practiseapp/detail_view.html", context)

def update_view(request, id):
    context = {}
    obj = get_object_or_404(PractiseModel, id = id)
    form = PractiseForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
    context["form"] = form 
    return render(request, "practiseapp/update_view.html", context)

def delete_view(request, id):
    context = {}
    obj = get_object_or_404(PractiseModel, id = id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "practiseapp/delete_view.html", context)

class class_create_view(CreateView):
    model = PractiseModel
    fields = ["title", "description"]
    success_url = "/"

class class_detail_view(DetailView):
    model = PractiseModel

class class_update_view(UpdateView):
    model = PractiseModel
    fields = ["title", "description"]
    success_url = "/"

class class_delete_view(DeleteView):
    model = PractiseModel
    success_url = "/"

class create_name(CreateView):
    model = Name
    fields = ["firstname", "lastname"]
    success_url = "/viewname"

def view_name(request):
    context = {}
    context["dataset"] = Name.objects.all()
    return render(request, "practiseapp/name_viewer.html", context)

def login_form(request):
    context = {}
    context["form"]  = LoginForm()
    return render(request, "practiseapp/login_form.html", context)

def logged_in(request):
    now = datetime.datetime.now()
    form = LoginForm(request.POST or None)
    user_name = ""
    password = ""
    if form.is_valid():
        user_name = form.cleaned_data.get("user_name")
        password = form.cleaned_data.get("password")
    return HttpResponse(f'''<span style ='font-family: Arial, Helvetica, sans-serif; font-size: 20px;'>
                            Welcome back again {user_name}!
                            <br>
                            Logged in again at {now} 
                            </span>''')