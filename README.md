Final project TeachMeSkills (QA Python) by Andrei Hlebko

Всем необходимо будет разработать фреймворк, который будет проверять написанные для вашей группы тест кейсы. Тесты должны быть разработаны на pytest, использую Page Objects, conftest. Дополнительные действия типа коннекта к БД можно делать в отдельном файле (хелперах) или в conftest. Запуск тестов должен происходить в Jenkins с формированием отчета в Allure.

MacOS/Mint

Скачиваем и устанавливаем приложение

git clone https://github.com/thejungwon/docker-webapp-django.git
cd docker-webapp-django
docker-compose up

Переходим по ссылке localhost:8000
Приложение отображается

TC_1:
Создать группу в bd 
Открыть приложение (в селениум)
Войти в админку
Проверить, что группа отображается
Изменить название группы через админку
Посмотреть в бд что название группы поменялось



API
URL: https://petstore.swagger.io/#/
Создать пользователя
Залогиниться пользователем
Получить данные пользователя
Сделать log out
Удалить пользователя
