from django.contrib import admin
from student.models import Student


# model 페이지 안에 생성한 db를 admin 페이지에 등록해서 보여줌
admin.site.register(Student)

