from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    # return HttpResponse("sunck is a good man")
    return render(request,'myApp/index.html')



from .models import Students,Grades
def students(request):
    studentsList = Students.stuObj2.all()
    return render(request, 'myApp/students.html', {"students":studentsList})
def students2(request):
    # 报异常
    studentsList = Students.stuObj2.get(sgender=True)
    return HttpResponse("^^^^^^^^^^^^^^^^^")

# 显示前5条学生
def students3(request):
    studentsList = Students.stuObj2.all()[0:5]
    return render(request, 'myApp/students.html', {"students": studentsList})

# 分页显示学生
def stupage(request, page):
    #0-5    5-10    10-15
    # 1      2        3
    #  page*5
    page = int(page)
    studentsList = Students.stuObj2.all()[(page - 1) * 5:page * 5]
    return render(request, 'myApp/students.html', {"students": studentsList})




from django.db.models import Max
def studentsearch(request):
    studentsList = Students.stuObj2.filter(sname__contains="孙")
    # studentsList = Students.stuObj2.filter(sname__startswith="孙")
    # studentsList = Students.stuObj2.filter(pk__in=[2,4,6,8,10])
    # studentsList = Students.stuObj2.filter(sage__gt=30)
    # studentsList = Students.stuObj2.filter(lastTime__year=2017)
    # studentsList = Students.stuObj2.filter(sname__contains="孙%")
    #描述中带有'薛延美'这三个字的数据时属于哪个班级的
    grade = Grades.objects.filter(students__scontend__contains='薛延美')
    print(grade)
    # maxAge = Students.stuObj2.aggregate(Max('sage'))
    # print(maxAge)
    # studentsList = Students.stuObj2.filter(~Q(pk__lte=3))
    return render(request, 'myApp/students.html', {"students":studentsList})



def addstudent(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudnet("刘德华",34,True,"我叫刘德华，请多关照", grade, "2017-8-10", "2017-8-11")
    stu.save()
    return HttpResponse("alfjl")
def addstudent2(request):
    grade = Grades.objects.get(pk=1)
    stu = Students.stuObj2.createStudnet("张学友",55,True,"我叫张学友，凯哥帅", grade, "2017-8-10", "2017-8-11")
    stu.save()
    return HttpResponse("*********")

from django.db.models import F,Q
def grades(request):
    # g = Grades.objects.filter(ggirlnum__gt=F('gboynum')+20)
    # print(g)
    return HttpResponse("OOOOOOOo")

