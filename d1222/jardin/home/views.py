from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home.models import ChartData


def main(request):
    return render(request,'main.html')


def chart(request):
    return render(request,'chart1.html')

def chart2(request):
    return render(request,'chart2.html')

# @csrf_exempt # csrf_token 예외처리
def chart_json(request):
    
    context={'dd_data':[10, 19, 5, 9, 2, 3],'ll_data':['홍길동','유관순','이순신','강감찬','김구','오은지']}
    return JsonResponse(context)


def chart_json2(request):
    if request.method=='GET':
        print("test")
    
    elif request.method=='POST':
        qs= ChartData.objects.all().order_by('cno')
        l_qs= list(qs.values())
        context={'data_list':l_qs}
        return JsonResponse(context)
    
    
        
        
    