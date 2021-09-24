from django.shortcuts import render
from django.views.generic import *
from .models import *


class View(ListView):    
    def get(self, request):
        transaction = SmsTransaction.objects.all()
        return render(request=request,template_name = 'smstransaction/view.html',context={"transaction":transaction})