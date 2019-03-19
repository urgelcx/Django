from django.contrib import admin

# Register your models here.
from .models import Grades,Students
# 注册
class StudentsInfo(admin.TabularInline):#StackedInline
    model = Students
    extra = 2
class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
    #列表页属性
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5
    # 添加、修改页属性
    # fields = ['ggirlnum','gboynum','gname','gdate','isDelete']
    fieldsets = [
        ("num",{"fields":['ggirlnum','gboynum']}),
        ("base",{"fields":['gname','gdate','isDelete']}),
    ]
admin.site.register(Grades, GradesAdmin)

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    #设置页面列的名称
    gender.short_description = "性别"
    list_display = ['pk','sname','sage',gender,'scontend','sgrade','isDelete']
    list_per_page = 10
    # 执行动作的位置
    actions_on_top = False
    actions_on_bottom = True
# admin.site.register(Students,StudentsAdmin)