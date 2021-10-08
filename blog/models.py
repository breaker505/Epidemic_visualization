# from django.db import models
#
# # Create your models here.
# class Stu(models.Model):
#     '''自定义Stu表对应的model类'''
#     #定义属性，默认主键自增id字段可不写
#     id=models.AutoField(primary_key=True)
#     name=models.CharField(max_length=16)
#     age=models.SmallIntegerField()
#     sex=models.CharField
#     classid=models.CharField()
#
#     #定义默认输出格式
#     def __str__(self):
#         return "%d:%s:%d:%s:%s:"(self.id ,self.name ,self.age ,self.sex ,self.classid)
#
#     #自定义对应的表名，默认表名blog_stu
#     class Meta:
#         db_table="stu"
#
#
