from django.db import models

# Create your models here.

# 老师信息表
class TeaInfo(models.Model):
    # 教师姓名
    name = models.CharField(max_length=20)
    #教师工号
    work_id = models.IntegerField()
    # 性别，1为男，2为女
    gender = models.IntegerField()
    # 登录密码，初始密码为空
    password = models.CharField(max_length=20)
    # 入职时间
    join_time = models.CharField(max_length=20)
    # 所带的班级专业
    speciality = models.CharField(max_length=20)
    # 联系电话
    tel = models.CharField(max_length=20)
    # 通讯地址
    ddress = models.CharField(max_length=20, default='')
    class Meta:
        db_table='teainfo'

#班级信息表
class ClassInfo(models.Model):
    # 班级名称，如：人工智能1811
    class_name = models.CharField(max_length=10)
    # 班级学生数量
    stu_count = models.IntegerField()
    # 外建关联老师
    t_id = models.ForeignKey(TeaInfo, on_delete=models.CASCADE)
    class Meta:
        db_table='classinfo'

# 阶段信息表
class Stage(models.Model):
    # 阶段名称
    name = models.CharField(max_length=20)
    # 阶段介绍
    detail = models.TextField(blank=True)
    class Meta:
        db_table='stage'

# 课程信息表
class Course(models.Model):
    # 课程名称
    name = models.CharField(max_length=20)
    # 课程介绍
    detail = models.TextField()
    # 阶段
    stage = models.CharField(max_length=20)
    class Meta:
        db_table='course'

# 学生考勤状态
class StuStatus(models.Model):
    # 考勤状态
    status = models.CharField(max_length=20)
    # 记录日期
    date = models.CharField(max_length=20)
    # 违纪学生姓名
    name = models.CharField(max_length=20)
    # 违纪学生学号
    account = models.IntegerField()
    class Meta:
        db_table='stustatus'

# 老师考勤状态
class TeaStatus(models.Model):
    # 考勤状态
    status = models.CharField(max_length=20)
    # 记录日期
    date = models.CharField(max_length=20)
    # 违纪老师姓名
    name = models.CharField(max_length=20)
    # 违纪老师工号
    account = models.IntegerField()
    class Meta:
        db_table='teastatus'

# 学生成绩表
class StuScore(models.Model):
    # 学生姓名
    name = models.CharField(max_length=20)
    # 学生学号
    account = models.IntegerField()
    # 学生所处阶段
    stage = models.CharField(max_length=10)
    # 期中笔试成绩
    midterm_pen = models.CharField(max_length=10)
    # 期中机试成绩
    midterm_com = models.CharField(max_length=10)
    # 期中总分
    midterm_total = models.CharField(max_length=10)
    # 期末笔试成绩
    finalterm_pen = models.CharField(max_length=10)
    # 期末机试成绩
    finalterm_com = models.CharField(max_length=10)
    # 期末总分
    finalterm_total = models.CharField(max_length=10)
    class Meta:
        db_table='stuscore'

# 管理员表
class AdminInfo(models.Model):
    # 管理员账号名称
    name = models.CharField(max_length=10)
    # 管理员账号
    account = models.IntegerField()
    # 管理员账号密码，默认为空
    password = models.CharField(max_length=20, default='')
    class Meta:
        db_table='admininfo'

# 积分表
class Integral(models.Model):
    # 总积分
    total = models.IntegerField()
    # 学生学号
    account = models.IntegerField()
    # 学生姓名
    name = models.CharField(max_length=20)
    class Meta:
        db_table='integral'

# 学生信息表
class StuInfo(models.Model):
    # 学生姓名
    name = models.CharField(max_length=20)
    # 学生学号，家长登录系统时使用
    account = models.AutoField(primary_key=True)
    # 身份证号
    ID_number = models.CharField(max_length=20)
    # 入学时间
    join_time = models.CharField(max_length=30)
    # 所在阶段
    stage = models.CharField(max_length=10)
    # 缴费情况 1为全交，2为欠费
    is_pay = models.IntegerField()
    # 性别，1为男，2为女
    gender = models.IntegerField()
    # 民族
    nation = models.CharField(max_length=10)
    # 所学专业
    speciality = models.CharField(max_length=10)
    # 所在班级的名字
    class_name = models.CharField(max_length=10)
    # 家长登录系统时的密码，默认为空
    password = models.CharField(max_length=20, default='')
    # 外建关联老师，老师学生一对多
    t_id = models.ForeignKey(TeaInfo, null=True, on_delete=models.SET_NULL)
    # 外建关联积分，一个学生一个积分
    int_id = models.OneToOneField(Integral, on_delete=True)
    # 外建关联阶段表，一个学生一个阶段
    s_id = models.OneToOneField(Stage, null=True, on_delete=models.SET_NULL)
    class Meta:
        db_table='stuinfo'


# 课件表
class Courseware(models.Model):
    # 课件名称
    name = models.CharField(max_length=20)
    # 发布老师的名称
    t_name = models.CharField(max_length=20)
    # 课件内容
    content = models.TextField()
    class Meta:
        db_table='courseware'

# 活动表
class Activity(models.Model):
    # 活动标题
    title = models.CharField(max_length=50)
    # 活动内容
    detail = models.TextField()
    # banner图连接
    banner_url = models.CharField(max_length=255)
    # 其他图片，用于详情页展示，可为空
    url = models.CharField(max_length=255, blank=True)
    # 其他图片，用于详情页展示，可为空
    url1 = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table='activity'
