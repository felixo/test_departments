# test_departments
Интерфейс для управления сущностями с использования JSON API.

## Описание
Данный интерфейс реализован с использованием django json api.
Интерфейс позволяет управлять Департаментами и Сотрудниками: смотреть, удалять и добавлять объекты.

## Инструкци для запуска.
Вам понадобится python3 и pip3
1. Создайте виртуальное окружение для проекта.
 ```console
 user@ubuntu: virtualenv -p python3 departments
 ```
 
 2. Активируйте созданное окружение.
 ```console
 user@ubuntu: . /path/to/env/departments/bin/activate
 ```
 
 3. Создайте директорию под проект и перейдите в нее. А затем скачайте проект с github.
 ```console
 user@ubuntu: git clone https://github.com/felixo/test_departments
 ```
 
 4. Перейдите в папку проекта и установите зависимости.
 ```console
 user@ubuntu: pip install requirements.txt
 ```
 
 5. Создайте миграцию, а затем проведите ее.
 ```console
 user@ubuntu: python manage.py makemigrations
 user@ubuntu: python manage.py migrate
 ```
 
 6. Запустите проект. 
 ```console
 user@ubuntu: python manage.py runserver
 ```
 
 7. Проект запущен. Открыть интерфейс можно по адресу http://127.0.0.1:8000/
 
