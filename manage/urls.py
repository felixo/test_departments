from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.BaseView.as_view(), name='index'),
    url(r'^departments', views.DepartmentList.as_view(), name='departments'),
    url(r'^report', views.ReportList.as_view(), name='report'),
    url(r'^workers', views.WorkerList.as_view(), name='workers'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)