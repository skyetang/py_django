from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CommonModel(models.Model):
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    update_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        abstract = True


class User(CommonModel):
    USER_STATUS = (
        ('1', '正常'),
        ('0', '删除')
    )
    username = models.CharField('用户名称', max_length=256, unique=True)
    nickname = models.CharField('用户呢称', max_length=128, null=True, blank=True)
    password = models.CharField('用户密码', max_length=256)
    avatar = models.ImageField('用户头像', upload_to='avatar', null=True, blank=True)
    status = models.SmallIntegerField('用户状态', default=1, choices=USER_STATUS)
    is_super = models.BooleanField('是否为超级管理员', default=False)

    class Meta:
        db_table = 'account_user'

    # 可以在console日志查询后默认展示记录的内容
    def __str__(self):
        return 'User: {}'.format(self.username)


class UserProfile(CommonModel):
    USER_SEX = (
        ('2', '未知'),
        ('1', '男'),
        ('0', '女')
    )
    user = models.OneToOneField(User, verbose_name='关联用户', on_delete=models.CASCADE, related_name='profile')
    username = models.CharField('用户名称', max_length=256, unique=True)
    realname = models.CharField('真实姓名', max_length=256, null=True, blank=True)
    sex = models.SmallIntegerField('用户性别', default=2, choices=USER_SEX)
    address = models.CharField('住址', max_length=128)

    class Meta:
        db_table = 'account_user_profile'


class LoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_history')
    username = models.CharField('用户名称', max_length=256)
    login_type = models.CharField('账号平台', max_length=128)
    ip = models.CharField('IP地址', max_length=64, default='')
    ua = models.CharField('UA信息', max_length=256, default='')
    created_at = models.DateTimeField('登录时间', auto_now_add=True)

    class Meta:
        db_table = 'account_login_history'
        ordering = ['-created_at']


# 新建
# from account.models import User
# 1、user = User(username='zs', password = '123')
# user.save()
# 2、user = User.objects.create(username='zs', password = '123')
# user_list = [User(username='1'), User(username='2']
# 3、User.objects.bulk_create(user_list)

# 查询
# user_obj = User.objects.get(id=2)
# user_2 = User.object.get(id=2, username='zs')
# user_list = User.object.all()
# latest = LoginHistory.objects.latest('created_at')
# earliest = LoginHistory.objects.earliest('created_at')
# zs = User.objects.get_or_create(username='zs')
# first = User.objects.first()
# last = user.objects.last()


# 修改
# user_edit = User.objects.get(id=1)
# user_edit.username = 'ls'
# user_edit.save()
# 批量修改
# userList = User.object.all()
# userList.update(status=0)
# 更好的批量修改
# bulk_update()


# 删除
# user_obj = User.objects.get(pk=1)
# user_obj.delete()
# 删除多条数据
# User.objects.all().delete()

# 判断表当中是否有数据
# User.objects.all().exists()  有一条以上的记录会返回True，否则False
# user.objects.all().using('account') 指定使用哪个数据库进行查询
# user.objects.all().filter()  筛选满足条件的记录
# user.objects.all().exclude()  排除满足条件的记录
# user.objects.all().order_by()  对记录进行排序



# 条件查询
# user.objects.all().filter(username__exact='zs')  双下划线后，exact为姓名完全巨配，iexact 为姓名LIKE后面的Zs
# gt,gte,lt,let,isnull
# contains 包含**值，icontains 包含**值，; 带i是不区分大小写
# in 是否在某个列表内，如 username__in=['zs', 'ls']
# startswith,istartwith 以什么开头，endswith, iendswith 以什么结束
# date,year, month,day,hour/minutes/second , week/week_day

# 示例：
# from datetime import datetime
# d = datetime(2025, 11, 5).date()
# user_list = User.objects.filter(update_at__date=d)
# user_list = User.objects.filter(update_at__day=25)

# 外键关联查询
# list = UserProfile.objects.filter(user__nickname__contains='管理员')
# 查询中的user 为 profile 一对一关联的模型名称，后面的nickname 则为user模型中的字段
# 整个意思就是通过profile 查询其外键关联模型中，nickname 包含有 管理员 的数据


# 多条件查询
# 1、 filter 当中放多个条件
# User.objects.filter(nickname='zs', status = 1)
# 2、 Q函数
# from django.db.models import Q
# query = Q(nickname = 'zs') & Q(status = 1)  且
# query = Q(nickname = 'zs') | Q(status = 1)  或
# User.objects.filter(query)

# 内置聚合函数
# Sum 求和， Avg 平均数， Count 计数，  Max/Min 最大值/最小值
# aggregate 返回一个结果
# annotate 在列表中使用，返回多个结果

