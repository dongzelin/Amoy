from django.urls import path, include
from rest_framework.routers import DefaultRouter
from polls.views import JustTest
from . import views

# router = DefaultRouter()
# router.register('interface',views.InterfaceViewSet)

urlpatterns = [
    path('/path/<int:id>/', JustTest.as_view()),
    path('TableList/', views.TableList.as_view(), name='TableList'),
    path('TableList/doEdit', views.doEdit.as_view(), name='doEdit'),
    path('TableList/doDelete', views.doDelete.as_view(), name='doDelete'),
    path('MysqlList/', views.MysqlList.as_view(), name='MysqlList'),
    path('MysqlList/mysqldoEdit', views.mysqldoEdit.as_view(), name='mysqldoEdit'),
    path('MysqlList/mysqldoDelete', views.mysqldoDelete.as_view(), name='mysqldoDelete'),
    path('TestCase/', views.TestCase.as_view(), name='TestCase'),
    path('TestCase/TestdoEdit', views.TestdoEdit.as_view(), name='TestdoEdit'),
    path('TestCase/TestdoDelete', views.TestdoDelete.as_view(), name='TestdoDelete'),
    path('TestCase/SelectData', views.SelectData.as_view(), name='SelectData'),
]
