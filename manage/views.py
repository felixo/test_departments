from django.views.generic import TemplateView
from manage.models import Department
from api.views import WorkerksView


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
        context['report'] = self.get_report(WorkerksView.as_view({'get': "list"})(self.request).data)
        return context

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