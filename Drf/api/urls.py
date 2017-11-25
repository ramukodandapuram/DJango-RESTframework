from django.conf.urls import url
from . import views


urlpatterns =[


		url(r'^api/employees/$',views.GetAllEmployees.as_view()),
		url(r'^api/updateemployee/(?P<Employee_Id>[0-9]+)/$', views.UpdateEmployee.as_view()),
		url(r'^api/insertemployee/$',views.InsertEmployee.as_view()),
		url(r'^api/deleteemployee/(?P<Employee_Id>[0-9]+)/$', views.DeleteEmployee.as_view()),

]
