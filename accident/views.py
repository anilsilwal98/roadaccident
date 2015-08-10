from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from accident.models import District,Location,Case
from django.db.models import Count

def  tasks_json(request):
    JSONSerializer = serializers.get_serializer("json")
    json_serializer = JSONSerializer()
    with open("accident/static/district.json","w") as out:
        json_serializer.serialize(District.objects.all(),stream=out)
     
    return HttpResponseRedirect('/login/')
 
def  index(request):
    name = "Mike"
    t = get_template('admin/index.html')
    html = t.render(Context({'name':name}))
    return HttpResponse(html)

def  login(request):
    c ={}
    c.update(csrf(request))
    return render_to_response('admin/form/login.html',c)


def  auth_view(request):
   #if form is not filled  then username and password are assigned to empty string and 
   #if username and password are saved to username and password variable

    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/loggedin/')
    else:
        return HttpResponseRedirect('/invalid/')


def  loggedin(request):

    JSONSerializer = serializers.get_serializer("json")
    json_serializer = JSONSerializer()
    with open("accident/static/date.json","w") as out:
        json_serializer.serialize(Case.objects.filter(date='2071-04-01'),stream=out)
    return render_to_response('admin/form/loggedin.html',{'details':Case.objects.all()})

def  invalid_login(request):
    return render_to_response('admin/form/invalid_login.html')

def  logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

def  register_user(request):
    if request.method == 'POST':
        form =  UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect('/register_success/')


    args = {}
    args.update(csrf(request))
    
    args['form'] = UserCreationForm()
    
    return render_to_response('admin/form/register.html',args)

def  register_success(request):
    return render_to_response('admin/form/register_success.html')

 #Create your views here.
