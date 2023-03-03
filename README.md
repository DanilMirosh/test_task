# Тестовое задание - Меню в Django

## Описание задания:

### Сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:

Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6 )Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по-заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8)На отрисовку каждого меню требуется ровно 1 запрос к БД
 Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
 {% draw_menu 'main_menu' %}

### Используемые технологии

Django
Подготовка к запуску проекта

Создайте виртуальную среду Python с помощью Poetry
Установите пакеты django, django-environ и psycopg2-binary.
В дальнейшем используйте инструмент Poetry для установки зависимостей Python.
Примените миграции

```python manage.py makemigrations```

`python manage.py migrate`

Создайте суперпользователя:

`python manage.py createsuperuser`

Запуск проекта с тестовыми данными

Выполните команды:

`python manage.py loaddata test_db.json`

`python manage.py runserver`

Перейдите на страницу http://127.0.0.1:8000/ , чтобы увидеть меню
Запуск проекта

Измените файл base.html вместо 'Производители банкоматов' напишите название основного меню, которое вам надо
Выполните команду:

`python manage.py runserver`

В браузере перейдите на сраницу администратора http://127.0.0.1:8000/admin/

Перейдите в закладку - Пункты меню
Добавьте новый пункт меню(название д.б. такое же, как в файле base.html) без указания родительской категории
Если необходимо далее можете добавлять новые пункты меню с любым названием, только основным родителем д.б. первый пункт меню
Перейдите на страницу http://127.0.0.1:8000/ , чтобы увидеть меню
Пример:

В base.html указан 'Производители банкоматов', переходим в админку добавляем новое меню 'Производители банкомата'. Далее можем добавить новое меню 'Unilever' родительской категорией, которого будет 'Производители банкомата'. Можем еще добавить меню 'Бренды' родительской категорией, которого будет 'Unilever' и т.д.

Автор:

Мирошниченко Данил  -  https://github.com/DanilMirosh/test_task