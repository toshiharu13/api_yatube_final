# Yatube
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
Социальная сеть блогеров (Проект Яндекс.Практикум)

# Описание
Социальная сеть для публикации личных дневников. Это сайт, на котором можно создать свою страницу. Если на нее зайти, то можно посмотреть все записи автора. Пользователи могут заходить на чужие страницы, подписываться на авторов и комментировать их записи. Автор может выбрать имя и уникальный адрес для своей страницы. Администратор имеет возможность модерировать записи и блокировать пользователей, если начнут присылать спам. Записи можно отправить в группу и посмотреть в ней записи разных авторов.
REST API для проекта на Django, позволяет получать, обновлять, добавлять данные на сайт. Работает с постами, комментариями, подписками, группами (категориями) постов. Аутентификация выполняется посредством получения токена JWT через POST-запрос.



# Системные требования

- [Python 3](https://www.python.org/)
- [Django 3.0.5](https://www.djangoproject.com/)
- [REST API Framework](https://www.django-rest-framework.org/)
- [DRF Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

# установка
Склонировать проект:

      https://github.com/toshiharu13/Yatube_final.git
      
Установить зависимости:

       pip install -r requirements.txt
       
Создать и применить миграции:

      python manage.py makemigrations
      python manage.py migrate
       
Запусить Django сервер:
       
      python manage.py runserver
      
      
# Примеры
Примеры обращения к API:

 - /redoc/ - Документация
 -/token/ - Получить токен
 -/token/refresh/ - Обновить токен
 - /posts/ - Получить список всех публикаций / Создать новую публикацию
 - /posts/{id}/ - Получить публикацию по id / Обновить по id / Удалить по id
 - /posts/{post_id}/comments/ - Получить список комментариев
 - /posts/{post_id}/comments/{comment_id}/ - Получить комментарий по id / Создать комментарий / Обновить / Удалить комментарий
 - /follow/ - Получить список подписчиков / Создать подписку
 - /group/ - Получить список всех групп / Создать группу
