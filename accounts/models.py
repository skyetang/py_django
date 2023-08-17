from django.db import models

# Create your models here.
# python manage.py check 检查模型是否创建正确
# python manage.py makemigrations 生成同步原语
# python manage.py migrate 执行前面生成的同步原语，会在数据库生成相应的表


class CommonModel(models.Model):
    create_at = models.DateTimeField('创建时间', auto_now_add=True)
    update_at = models.DateTimeField('最后更新时间', auto_now=True)

    # 元数据，声明该类是一个抽像类，便不会生成对应的数据表
    class Meta:
        abstract = True


class User(CommonModel):
    name = models.CharField('name', max_length=64)
    sex = models.CharField('性别', max_length=1, choices=(
        ('1', '男'),
        ('0', '女')
    ), default=0)
    # 正整数
    age = models.PositiveIntegerField('年龄', default=0)
    username = models.CharField('用户名', max_length=64, unique=True)
    password = models.CharField('密码', max_length=64)
    remark = models.CharField('备注', max_length=64, null=True, blank=True)

    # 用户收藏的问题，可以是一个用户收藏多个问题，一个问题也可以被多个用户收藏，所以是多对多的关系
    collect_questions = models.ManyToManyField('question')

    # 元数据，需要固定的Meta类名称，用于修改数据表的某些配置，比如表名等
    class Meta:
        db_table = 'user'


class Profile(CommonModel):

    # 和user表建立一对一的关系，并通过反向引用related_name，当查询出了一个user的对象后，在user对象当中使用profile
    # 便可以查询出对应用户的profile数据,如下：
    # user = User()
    # profile = user.profile
    # 通过关联建立的字段，都会在后面加一个id,如下的会在数据表中变成user_id字段，如果想要不加，可以通过tb_column =‘xxx’来设定
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    nickname = models.CharField('呢称', max_length=64)


class Question(CommonModel):
    name = models.CharField('问题名称', max_length=256)


class Answer(CommonModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField('答案的内容')


class Classify(models.Model):
    # 分类
    # 1 酒水
    #   2 红酒
    #   3 白酒
    # 这样在查询出1的分类后，可以通过children把他的子类2,3一起查询出来
    name = models.CharField('分类名称', max_length=64)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children')

