from django.db import models
# Create your models here.
# 我们的模型类，需要继承 models.model
# 系统会自动为我们添加一个主键 --id
# 字段
# 字段 = model.类型(选项)
# 字段名不要使用python关键字
class BookInfo(models.Model):
    # id
    name = models.CharField(max_length=10)
    # 重写 str方法让admin来显示书籍名字
    def __str__(self):
        return  self.name
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)