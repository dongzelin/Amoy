import base64
import datetime
import json
import requests
from django.views import View
from django.http.response import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django_simple_api import Query
from django.views.generic import FormView
from django.core import serializers
from polls.models import Interface_data, Mysql_data, Test_Case_Data


class JustTest(View):
    def get(self, request, id: int = Query()):
        return HttpResponse(id)


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


class TableList(FormView):
    # 访问post请求
    def post(self, request, *args, **kwargs):
        # 为序列化json做准备，因为json是不可序列化 所以必须加values
        Interface = Interface_data.objects.all().values('pk', 'interface_name', 'interface_url', 'system_type',
                                                        'interface_date', 'interface_json')
        # 将获取到的数据进行list为序列化做准备
        test = json.dumps(list(Interface), cls=DateEncoder, ensure_ascii=False)
        number = Interface_data.objects.all().count()
        data = json.loads(test)
        # 返回json数据
        return JsonResponse(data, safe=False)


class doEdit(FormView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('测试一下')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = (request.body).decode('utf-8')
            data = json.loads(name)
            interface_name = data['interface_name']
            interface_url = data['interface_url']
            interface_json = data['interface_json']
            # 判断是否有id传入，有就是编辑，没有就是新增
            Key = 'pk' in data.keys()
            # True就是编辑，Flase就是新增
            if Key == True:
                ORM_data = Interface_data.objects.filter(id=data['pk']).update(interface_name=interface_name,
                                                                               interface_url=interface_url,
                                                                               system_type='system_type',
                                                                               interface_date=datetime.datetime.now(),
                                                                               interface_json=interface_json)
                try:
                    ORM_data.save()
                except:
                    print('test')
            else:
                ORM_data = Interface_data(interface_name=interface_name, interface_url=interface_url,
                                          system_type='system_type', interface_date=datetime.datetime.now(),
                                          interface_json=interface_json)
                try:
                    ORM_data.save()
                except:
                    print('test')
            return JsonResponse({
                "code": 200,
                "msg": "success",
                "data": data
            })


class doDelete(FormView):
    def post(self, request, *args, **kwargs):
        name = (request.body).decode('utf-8')
        data = json.loads(name)
        print(data, 'sdasdasdsada')
        if len(data) == 1:
            data_id = data['ids']
            del_obj = Interface_data.objects.get(id=data_id)
            del_obj.delete()
            # 为序列化json做准备，因为json是不可序列化 所以必须加values
            Interface = Interface_data.objects.all().values('pk', 'interface_name', 'interface_url', 'system_type',
                                                            'interface_date', 'interface_json')
            # 将获取到的数据进行list为序列化做准备
            test = json.dumps(list(Interface), cls=DateEncoder, ensure_ascii=False)
        else:
            print(data)

        return JsonResponse({
            "code": 200,
            "msg": "success",
            "data": json.loads(data)
        })


class MysqlList(FormView):
    def post(self, request, *args, **kwargs):
        mysql = Mysql_data.objects.all().values('pk', 'mysql_name', 'mysql_Remark', 'system_type',
                                                'interface_date', 'mysql_statement')
        # 将获取到的数据进行list为序列化做准备
        test = json.dumps(list(mysql), cls=DateEncoder, ensure_ascii=False)
        number = Mysql_data.objects.all().count()
        data = {
            "code": 200,  # 成功的状态码
            "msg": "success",  # 提示信息
            "totalCount": number,  # 总条数（表格中用到）
            "data": json.loads(test)  # 返回数据
        }

        print(data)
        # 返回json数据
        return JsonResponse(data, safe=False)


class mysqldoEdit(FormView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('测试一下')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = (request.body).decode('utf-8')
            data = json.loads(name)
            number = Mysql_data.objects.all().count()
            interface_name = data['mysql_name']
            interface_url = data['mysql_Remark']
            interface_json = data['mysql_statement']
            # 判断是否有id传入，有就是编辑，没有就是新增
            Key = 'pk' in data.keys()
            # True就是编辑，Flase就是新增
            if Key == True:
                ORM_data = Mysql_data.objects.filter(id=data['pk']).update(mysql_name=interface_name,
                                                                           mysql_Remark=interface_url,
                                                                           system_type='system_type',
                                                                           mysql_statement=interface_json)
                try:
                    ORM_data.save()
                except:
                    print('test')
            else:
                ORM_data = Mysql_data(mysql_name=interface_name,
                                      mysql_Remark=interface_url,
                                      system_type='system_type',
                                      interface_date=datetime.datetime.now(),
                                      mysql_statement=interface_json)
                try:
                    ORM_data.save()
                except:
                    print('test')
            return JsonResponse({
                "code": 200,
                "msg": "success",
                "totalCount": number,  # 总条数（表格中用到）
                "data": data
            })


class mysqldoDelete(FormView):
    def post(self, request, *args, **kwargs):
        name = (request.body).decode('utf-8')
        data = json.loads(name)
        number = Mysql_data.objects.all().count()
        print(data, 'sdasdasdsada')
        if len(data) == 1:
            data_id = data['ids']
            del_obj = Mysql_data.objects.get(id=data_id)
            del_obj.delete()
            # 为序列化json做准备，因为json是不可序列化 所以必须加values
            mysql_data = Mysql_data.objects.all().values('pk', 'mysql_name', 'mysql_Remark', 'system_type',
                                                        'interface_date', 'mysql_statement')
            # 将获取到的数据进行list为序列化做准备
            test = json.dumps(list(mysql_data), cls=DateEncoder, ensure_ascii=False)
        else:
            print(data)

        return JsonResponse({
            "code": 200,
            "msg": "success",
            "totalCount": number,  # 总条数（表格中用到）
            "data": json.loads(test)})


class TestCase(FormView):
    def post(self, request, *args, **kwargs):
        mysql = Test_Case_Data.objects.all().values('pk', 'Test_case_name', 'Test_case_url', 'system_type',
                                                'interface_date', 'Test_case_json')
        # 将获取到的数据进行list为序列化做准备
        test = json.dumps(list(mysql), cls=DateEncoder, ensure_ascii=False)
        number = Test_Case_Data.objects.all().count()
        data = {
            "code": 200,  # 成功的状态码
            "msg": "success",  # 提示信息
            "totalCount": number,  # 总条数（表格中用到）
            "data": json.loads(test)  # 返回数据
        }
        print(data)
        # 返回json数据
        return JsonResponse(data, safe=False)


class TestdoEdit(FormView):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = (request.body).decode('utf-8')
            data = json.loads(name)
            number = Mysql_data.objects.all().count()
            Test_case_name = data['Test_case_name']
            Test_case_url = data['Test_case_url']
            Test_case_json = data['Test_case_json']
            system_type = data['system_type']
            # 判断是否有id传入，有就是编辑，没有就是新增
            Key = 'pk' in data.keys()
            # True就是编辑，Flase就是新增
            if Key == True:
                ORM_data = Test_Case_Data.objects.filter(id=data['pk']).update(Test_case_name=Test_case_name,
                                                                           Test_case_url=Test_case_url,
                                                                           system_type=system_type,
                                                                           Test_case_json=Test_case_json)
                try:
                    ORM_data.save()
                except:
                    print('test')
            else:
                ORM_data = Test_Case_Data(Test_case_name=Test_case_name,
                                      Test_case_url=Test_case_url,
                                      system_type=system_type,
                                      interface_date=datetime.datetime.now(),
                                      Test_case_json=Test_case_json)
                try:
                    ORM_data.save()
                except:
                    print('test')
            return JsonResponse({
                "code": 200,
                "msg": "success",
                "totalCount": number,  # 总条数（表格中用到）
                "data": data
            })


class TestdoDelete(FormView):
    def post(self, request, *args, **kwargs):
        name = (request.body).decode('utf-8')
        data = json.loads(name)
        number = Test_Case_Data.objects.all().count()
        if len(data) == 1:
            data_id = data['ids']
            del_obj = Test_Case_Data.objects.get(id=data_id)
            del_obj.delete()
            # 为序列化json做准备，因为json是不可序列化 所以必须加values
            Case_Data = Test_Case_Data.objects.all().values('pk', 'Test_case_name', 'Test_case_url', 'system_type',
                                                         'interface_date', 'Test_case_json')
            # 将获取到的数据进行list为序列化做准备
            test = json.dumps(list(Case_Data), cls=DateEncoder, ensure_ascii=False)
        else:
            print(data)

        return JsonResponse({
            "code": 200,
            "msg": "success",
            "totalCount": number,  # 总条数（表格中用到）
            "data": json.loads(test)})


class SelectData(FormView):
    def post(self, request, *args, **kwargs):
        name = (request.body).decode('utf-8')
        data = json.loads(name)
        number = Test_Case_Data.objects.all().count()
        print(data)
        Select_Sys_data = Test_Case_Data.objects.filter(system_type=data['value']).values()
        Sys_data = json.dumps(list(Select_Sys_data), cls=DateEncoder, ensure_ascii=False)
        print('BI系统', json.loads(Sys_data))

        return JsonResponse({
            "code": 200,
            "msg": "success",
            "totalCount": number,  # 总条数（表格中用到）
            "data": json.loads(Sys_data)})