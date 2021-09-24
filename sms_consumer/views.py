from django.shortcuts import render
from django.views.generic.edit import View, CreateView
from .models import *
from django.http.response import HttpResponse,HttpResponseRedirect
from .forms import *
from django.contrib.auth import views as auth_views
from django.shortcuts import resolve_url

# Create your views here.
class List(View):
    def get(self, request):
        user = SmsUser.objects.all()
        smform = SmsForm()
        return render(request=request, template_name="sms_consumer/list.html", context={"user":user, "smform":smform})
    def post(self, request):
        if request.method=="POST":
            pi = SmsUser.objects.get(pk=1)
            form = SmsForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
            return HttpResponse("SMS assign succesfull")


class LoginView(auth_views.LoginView):
    template_name = 'registration/login.html'
    fields = ["email", 'password']

    def get_success_url(self):
        return resolve_url('home')

class LogoutView(auth_views.LogoutView):
    template_name = 'registration/logout.html'



class smslog(View):
    def get(self, request):
        form = SmsLogForm()
        user = SmsLogModel.objects.all()
        return render(request=request, template_name='sms_log/msg.html', context={'forms':form, 'user':user})

    def post(self, request):
        # md = SmsLogModel(request.POST)
        current_user = SmsUser.objects.all()
        user_id = current_user
        # md.instance.contact_no=['contact_no']
        # count = 1
        breakpoint()
        nm = request.POST.getlist('contact_no')
        ms = request.POST.getlist('message')
        reg = SmsLogModel(contact_no = nm, message = ms, count=1)
        reg.save()
        return HttpResponseRedirect('/log')


class smslog1(CreateView):
    model = SmsLogModel
    form_class = SmsLogForm
    template_name = 'sms_log/msg.html'
    success_url = '/login'
    
