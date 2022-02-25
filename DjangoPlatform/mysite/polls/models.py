

# Create your models here.
from django.db import models


class Interface_data(models.Model):
    id = models.AutoField(primary_key = True)   # 序号
    interface_name = models.TextField() # 接口名称
    interface_url = models.TextField() # 接口地址
    system_type = models.CharField(max_length=60) # 系统类型
    interface_date = models.DateField()    # 新建接口时间
    interface_json = models.TextField() # 接口json

class Mysql_data(models.Model):
    id = models.AutoField(primary_key = True)   # 序号
    mysql_name = models.TextField() # 接口名称
    mysql_Remark = models.TextField() # 数据库语句
    system_type = models.CharField(max_length=60) # 系统类型
    interface_date = models.DateField()    # 新建数据时间
    mysql_statement = models.TextField() #  数据库描述
class Test_Case_Data(models.Model):
    id = models.AutoField(primary_key=True)  # 序号
    Test_case_name = models.TextField()  # 用例名称
    Test_case_url = models.TextField()  # 用例接口地址
    system_type = models.CharField(max_length=60)  # 系统类型
    interface_date = models.DateField()  # 新建用例时间
    Test_case_json = models.TextField()  # 用例json

