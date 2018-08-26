from django.conf.urls import url
from django.urls import include
from api.views import DepartmentView, WorkerksView
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)

router.register(r'departments', DepartmentView)
router.register(r'workers', WorkerksView)

urlpatterns = [
    #url(r'^departments', DepartmentView.as_view(), name='departemnt_list'),
    url(r'^', include(router.urls)),
    url(r'^delete_dep/(?P<pk>[0-9]+)/', DepartmentView.as_view({'delete': 'delete'}), name='deparment_api'),
    url(r'^filter_dep/', DepartmentView.as_view({'post': 'list'}), name='deparment_filter'),
    url(r'^delete_worker/(?P<pk>[0-9]+)/', WorkerksView.as_view({'delete': 'delete'}), name='delete_worker'),
]