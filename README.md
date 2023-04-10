# dendritic :deciduous_tree:

### Описание
**dendritic** - это проект реализация древовидного меню на Django.

Доступный функционал:
- редактирование меню через стандартную админку Django;
- вставка необходимого меню на любой нужной странице по названию.

  ```
  {% load menu_tags %}
  
  ...
  
  {% draw_menu 'menu_name' %}
  ```

### Инструкция по развертыванию

Клонировать репозиторий:

```
git clone https://github.com/Tacostrophe/dendritic.git
```
Все нижеперечисленные действия выполнять из dendritic/

В репозитории создать и активировать виртуальное окружение:
```
python3 -m venv /path/to/new/virtual/environment
```
```
source /path/to/new/virtual/environment/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запуск проекта:
```
python3 manage.py runserver
```

<sub>Всегда рад замечаниям и советам</sub>
