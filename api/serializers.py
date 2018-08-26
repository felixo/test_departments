from rest_framework_json_api import serializers
from manage.models import Department, Workers
from rest_framework_json_api.relations import ResourceRelatedField


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('title',)


class WorkersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workers
        fields = ('department', 'fio', 'phone', 'sellery')