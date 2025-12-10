from django.shortcuts import render
from student.models import Student

def write(request):
    return render(request,'student/write.html')

def list(request):
    qs= Student.objects.all().order_by('-sno')
    context= {"our_class":"SM유니버스 직무교육","stu_list":qs}
    return render(request,'student/list.html',context)

