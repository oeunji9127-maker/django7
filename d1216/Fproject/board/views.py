from django.shortcuts import render,redirect
from board.models import Board
import datetime



def write(request):
    if request.method=='GET':
        return render(request,'board/write.html')
    elif request.method=='POST':
        btitle= request.POST.get('btitle')
        bfile= request.FILES.get('bfile')  # file타입이기에 FILES로 읽어야 함 
        print('post정보: ',btitle)
        print('post정보: ',bfile)
        print('날짜: ',datetime.datetime.now())
        
        
        # 파일저장
        qs= Board(btitle=btitle,bfile=bfile)
        qs.save()
        
        return render(request,'board/write.html')