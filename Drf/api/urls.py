from django.conf.urls import url
from . import views


urlpatterns =[


		url(r'^api/employees/$',views.EmployeesDetails.as_view()),

		url(r'^api/employees/(?P<pk>[0-9]+)/$',views.EmployeeDetailsByID.as_view()),

		url(r'^api/insertemployee/$',views.InsertEmployee.as_view()),

		url(r'^api/updateemployee/(?P<pk>[0-9]+)/$', views.UpdateEmployee.as_view()),
		
		url(r'^api/deleteemployee/(?P<pk>[0-9]+)/$', views.DeleteEmployee.as_view()),

]
