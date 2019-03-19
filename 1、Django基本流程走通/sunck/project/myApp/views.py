from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("sunck is a good man")
def detail(request,num,num2):
    return HttpResponse("detail-%s-%s"%(num,num2))



from .models import Grades
def grades(request):
    # 去模板里取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板，模板在渲染页面，将渲染好的页面返回浏览器
    return render(request, 'myApp/grades.html', {"grades":gradesList})

from .models import Students
def students(request):
    studentsList = Students.objects.all()
    return render(request, 'myApp/students.html', {"students":studentsList})


def gradesStudents(request,num):
    # 获得对应的班级对象
    grade = Grades.objects.get(pk=num)
    # 获得班级下的所有学生对象列表
    studentsList = grade.students_set.all()
    return render(request, 'myApp/students.html',{"students":studentsList})