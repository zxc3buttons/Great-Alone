
# GreatAlone
## Общее описание проекта
Веб-сайт **«GreatAlone»** предназначен ведения личного блога разработчиков сайта, а также для отдыха от городской суеты.
Пользователи в интернете могут оставлять отзывы сайту в виде анонимного обращения<br>
Среди функций **«GreatAlone»** можно выделить:
1. Отображение случайно выбранных Хокку
2. Добавление, удаление, редактирование записей о новом проекте на сайт (со стороны разработчика)
3. Создание обращения для разработчиков (со стороны пользователей)

---

## Описание зависимостей
В проекте используется файл requirements.txt для описания зависимотей проекта, они продублированы ниже<br>
```groovy
alabaster==0.7.12
asgiref==3.5.1
Babel==2.10.1
certifi==2021.10.8
charset-normalizer==2.0.12
colorama==0.4.4
Django==4.0.4
docutils==0.17.1
idna==3.3
imagesize==1.3.0
Jinja2==3.1.2
livereload==2.6.3
MarkupSafe==2.1.1
packaging==21.3
Pygments==2.12.0
pyparsing==3.0.9
pytz==2022.1
requests==2.27.1
six==1.16.0
snowballstemmer==2.2.0
Sphinx==4.5.0
sphinx-autobuild==2021.3.14
sphinxcontrib-applehelp==1.0.2
sphinxcontrib-devhelp==1.0.2
sphinxcontrib-htmlhelp==2.0.0
sphinxcontrib-jsmath==1.0.1
sphinxcontrib-qthelp==1.0.3
sphinxcontrib-serializinghtml==1.1.5
sqlparse==0.4.2
tornado==6.1
tzdata==2022.1
urllib3==1.26.9

setuptools~=57.0.0
beautifulsoup4~=4.11.1
```
<br>
<a href="https://github.com/worldbeater/dta">
  <img src="стек (1).png">
</a>
<br>
<br><br>
Проект разработан на языке Python в программной среде Pycharm. Для создания веб-приложений на этом языке наиболее часто используются фреймворки Django и Flask.
Наша команда решила использовать Django, так как он проще в освоении и обладает большим функционалом, позволяющим быстро и эффективно развернуть веб-сайт.
В Django предусмотрена встроенная база данных SQlite3 вместе с админ-панелью, что очень упрощает и ускоряет разработку сайта. Для контейнеризации использовался docker,
а для удобной работе в команде проект был размещен на GitHub. Касаемо front-end части, были использованы HTML, CSS и JS.

---

## Как запустить проект
Для запуска проекта понадобится Python с с версией 3.10 и выше. Сначала нужно клонировать проект на свой ПК:
```bash
git init
git clone https://github.com/MasterHach/SITE.git
```
Далее, для удобства, нужно подключить виртуальную среду для работы с проектом:
```bash
pip install virtualenv
```
После, в директории SITE нужно выполнить эти команды:
```bash
python -m venv venv
venv\Scripts\activate.bat
```
Когда виртуальное окружение установлено, можно установить в него библиотеки для работы проекта:
```bash
cd mysite
python -m pip install -r requirements.txt
```
После установки зависимостей можно запустить сам сервер:
```bash
python manage.py runserver
```
Также проект можно запустить с помощью системы контейнеризации Docker:
```docker
docker-compose up --build
docker-compose up
```
