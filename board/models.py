from django.db import models
from member.models import CustomUser


'''
{"병원명":"김은주산부인과의원",
"주소":"서울 구로구 신도림동",
"구":"구로구",
"예약가능여부":null,
"진료시작시각":"10:00에 진료 시작",
"방문자리뷰":"방문자 리뷰 428",
"블로그리뷰":"블로그 리뷰 116",
"산부인과전문의수":"산부인과전문의 1명",
"기타전문의여부":null}
'''

class Board(models.Model):
    hospital_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100,null=True)
    gu=models.CharField(max_length=100,null=True)
    reservation=models.CharField(max_length=100,null=True)
    visitcnt=models.CharField(max_length=100,null=True)
    blogcnt=models.CharField(max_length=100,null=True)
    maindoctorcnt=models.CharField(max_length=100,null=True)



class Comment(models.Model):
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE,related_name='comments')
    board=models.ForeignKey(Board, null=True,on_delete=models.CASCADE,related_name='comments')
    title=models.CharField(max_length=100)
    body=models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    star=models.CharField(max_length=100) 


