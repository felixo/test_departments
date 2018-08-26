from rest_framework_json_api.views import ModelViewSet, Response
from manage.models import Department, Workers
from api.serializers import DepartmentSerializer, WorkersSerializer
from django.http import Http404

class DepartmentView(ModelViewSet):
    queryset = Department.objects.all().order_by('id')
    serializer_class = DepartmentSerializer

    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        department = self.get_object(pk)
        department.delete()
        return Response(status=204)

    def get_queryset(self):
        if self.request.method == 'POST':
            print('start')
            q_filter = self.request.POST.get('filter', None)
            print(q_filter)
            if q_filter:
                print('here')
                return self.queryset.filter(title__icontains=q_filter)
        return self.queryset


class WorkerksView(ModelViewSet):
    queryset = Workers.objects.all().order_by('id')
    serializer_class = WorkersSerializer

    def get_object(self, pk):
        try:
            return Workers.objects.get(pk=pk)
        except Workers.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        worker = self.get_object(pk)
        worker.delete()
        return Response(status=204)

    def get_queryset(self):
        if self.request.method == 'POST':
            print('start')
            q_filter = self.request.POST.get('filter', None)
            print(q_filter)
            if q_filter:
                print('here')
                return self.queryset.filter(title__icontains=q_filter)
        return self.queryset