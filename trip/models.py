from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, ContentType, GenericRelation
# Create your models here.


class Sight(models.Model):
    # 景点表
    name = models.CharField('景点名称', max_length=256)
    address = models.CharField('景点地址', max_length=256)
    # 第三种方法当中需要在原表中添加：
    # 与MultipleComment建立返回关联，则可以通过sight的对象拿到对应的所有评论数据
    # 也可以通过query_name 进行满足条件的查询，使用如下：
    # sight = Sight()
    # sight.comments 就可以拿到该景点下所有的评论
    comments = GenericRelation('MultipleComment', related_query_name='sight_comments')


class Order(models.Model):
    # 订单表
    sn = models.CharField('订单号', max_length=64)
    amount = models.FloatField('订单金额')
    comments = GenericRelation('MultipleComment', related_query_name='sight_comments')


# 第一种方式，分别建两张评价表进行关联，缺点是如果要增加其它产品，如酒店等等，则需要增加更多的评价表
# class SightComment(models.Model):
#     # 景点评价表
#     sight = models.ForeignKey('sight', on_delete=models.CASCADE, related_name='comment')
#     comment = models.TextField('评论内容')
#     score = models.FloatField('评分', default=5)
#
#
# class OrderComment(models.Model):
#     # 订单评价表
#     order = models.ForeignKey('order', on_delete=models.CASCADE, related_name='comment')
#     comment = models.TextField('评论内容')
#     score = models.FloatField('评分', default=5)


# 第二种方式：
# 合并优化以上两张评价表到一张表上面的处理方法如下
# 缺点是如果增加酒店，虽然表不用增加，但是会在此方法中修改
# 并且每一条记录，除了对应的那个评价字段外，其它字段则为null
# class Comment(models.Model):
#     sight_comment = models.ForeignKey('sight', on_delete=models.CASCADE, null=True)
#     order_comment = models.ForeignKey('order', on_delete=models.CASCADE, null=True)
#     comment = models.TextField('评论内容')
#     score = models.FloatField('评分', default=5)


# 第三种方法：复合类型的关联
class MultipleComment(models.Model):
    # 现对应的content_type表建立关联
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # 保存对应的产品ID，如订单ID，或者景点ID
    object_id = models.IntegerField('订单ID')
    # 将content_type 与 object_id 建立关联，则可以据此找到对应数据所关联的对象，如下：
    # m_comment = MultipleComment()
    # m_comment.content_object 如果关联的是sight,则返回sight这个对象
    content_object = GenericForeignKey('content_type', 'object_id')
    comment = models.TextField('评论内容')
    score = models.FloatField('评分', default=5)
