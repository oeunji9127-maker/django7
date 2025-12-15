from django.db import models
from member.models import Member


class Board(models.Model):
    bno= models.AutoField(primary_key=True)
    # 회원정보 모두를 가져옴, 객체전체를 가져옴
    member= models.ForeignKey(Member,on_delete=models.DO_NOTHING,null=True)
    btitle=models.CharField(max_length=1000)
    bcontent=models.TextField()
    bhit= models.IntegerField()
    bdate=models.DateField(auto_now=True)
    
    
    
    # 답변 댓글 사용에 필요한 칼럼
    # bgroup,bstep,bindent
    # 파일첨부
    # bfile
    
    def __str__(self):
        return f"{self.bno},{self.btitle},{self.member.id},{self.bdate}"
