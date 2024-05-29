Проект по БД
В рамках проекта вам необходимо получить данные о компаниях и вакансиях с сайта hh.ru, спроектировать таблицы в БД PostgreSQL и загрузить полученные данные в созданные таблицы.

Для работы потребуется
Создайте виртуальное окружение:
python3 -m venv venv
Активируйте виртуальное окружение:
source venv/Scripts/activate
В папке проекта src cоздайте database.ini конфигурационный файл с вашими параметрами подключения к БД.
Пример файла:

[postgresql]
host=localhost
user=postgres
password=123456789
port=5432
