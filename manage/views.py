from django.views.generic import TemplateView
from manage.models import Department
from api.views import WorkerksView
from django.db import connection


class BaseView(TemplateView):
    template_name = "manage/index.html"
    json_data = None
    top_menu = [('Главная', True, 'index'), ('Департаменты', False, 'departments'), ('Сотрудники', False, 'workers'), ('Отчет', False, 'report')]
    header = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bread_crumbs'] = [('index', 'Главная')]
        context['menu'] = self.top_menu
        if self.header:
            context['header'] = self.header
        return context


class DepartmentList(BaseView):
    template_name = "manage/department.html"
    json_data = True
    top_menu = [('Главная', False, 'index'), ('Департаменты', True, 'departments'), ('Сотрудники', False, 'workers'), ('Отчет', False, 'report')]
    header = 'Департаменты'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bread_crumbs'].append(('departments', 'Департаменты'))
        return context


class WorkerList(BaseView):
    template_name = "manage/worker.html"
    json_data = True
    top_menu = [('Главная', False, 'index'), ('Департаменты', False, 'departments'), ('Сотрудники', True, 'workers'), ('Отчет', False, 'report')]
    header = 'Сотрудники'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bread_crumbs'].append(('workers', 'Сотрудники'))
        context['departments'] = Department.objects.all()
        return context


class ReportList(BaseView):
    template_name = "manage/report.html"
    json_data = True
    top_menu = [('Главная', False, 'index'), ('Департаменты', False, 'departments'), ('Сотрудники', False, 'workers'), ('Отчет', True, 'report')]
    header = 'Отчет'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bread_crumbs'].append(('report', 'Отчет'))
        context['report'] = self.my_custom_sql()
        return context

    def my_custom_sql(self):
        result_dict = {}
        with connection.cursor() as cursor:
            cursor.execute("""SELECT manage_department.title, 
            (SELECT AVG(manage_workers.sellery) FROM manage_workers WHERE manage_workers.department_id = manage_department.id),
            w.fio, w.phone, w.sellery
            FROM manage_department LEFT JOIN manage_workers w on  manage_department.id = w.department_id""")
            for row in cursor.fetchall():
                dep, avg, fio, phone, sellery = row
                if avg:
                    if dep in result_dict:
                        result_dict[dep]['workers'].append({
                            'fio': fio,
                            'phone': phone,
                            'sellery': sellery
                        })
                        result_dict[dep]['avg'] = avg
                    else:
                        result_dict[dep] = {}
                        result_dict[dep]['workers'] = [{
                            'fio': fio,
                            'phone': phone,
                            'sellery': sellery
                        }]
                        result_dict[dep]['avg'] = avg

        return result_dict

    def get_report(self, data):
        result = {}
        depart = {str(dep.id) : dep.title for dep in Department.objects.all()}
        for obj in data['results']:
            title = depart[obj['department']['id']]
            if title in result:
                result[title]['workers'].append({
                    'fio': obj['fio'],
                    'phone': obj['phone'],
                    'sellery': obj['sellery'],
                })
            else:
                result[title] = { 'workers':[{
                    'fio': obj['fio'],
                    'phone': obj['phone'],
                    'sellery': obj['sellery'],
                }]}
        for title in result.keys():
            total = 0
            for worker in result[title]['workers']:
                total += int(worker['sellery'])
            result[title]['midle'] = int(total / len(result[title]['workers']))
        return result