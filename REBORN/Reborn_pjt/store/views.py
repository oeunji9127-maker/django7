from django.shortcuts import render



def list(request):
    return render(request,'store/list.html')
