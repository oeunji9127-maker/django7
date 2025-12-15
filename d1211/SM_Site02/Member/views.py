from django.shortcuts import render,redirect
from django.urls import reverse

def write(request):
    return render(request,'member/write.html')
