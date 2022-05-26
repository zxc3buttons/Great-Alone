# SITE
simple html site with non-using data store, but quite pretty in design

i use django as fraimwork to run my site
what else...

the command for run the server is 'python manage.py runserver'

so, all dependencies are in requirements.txt

and my site will expands with time, but now it is simply html-css-and-some-js web-page

and you can enjoy being alone on it, read some quotes and at all enjoy peace and quiete...

in the future i want to realize database, make pasrser of qoutes and add other html pages


# GreatAlone
## Общее описание проекта
Веб-сайт **«GreatAlone»** предназначен ведения личного блога разработчиков сайта, а также для отдыха от городской суеты.
Пользователи в интернете могут оставлять отзывы сайту в виде анонимного обращения<br>
Среди функций **«GreatAlone»** можно выделить:
1. Отображение случайно выбранных Хокку
2. Добавление, удаление, редактирование записей о новом проекте на сайт (со стороны разработчика)
3. Отсавка обращения разработчикам (со стороны пользователей)

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
  <img src="./webapp/static/logo.svg">
</a>
<br>
<br><br>
К главным зависимостям, использующимся в проекте можно отнести Spring Boot для Java, упрощающий разработку веб-приложений. Также сюда можно отнести Lombok для расшире
ния функциональности языка Java. Thymeleaf - шаблонизатор, позволяющий связывать HTML5 и XML с веб-приложением уровня Spring MVC. В проекте также используется система управления базами данных PostgreSQL.

---

## Как запустить проект
Для запуска проекта понадобится JAVA с с версией 11 и выше, а также сборщик проектов Maven. В файл pom.xml необходимо перенести зависимости приведенные в листинге выше. Нужные зависимости загрузятся автоматически, после чего вы сможете запустить проект через любую среду разработки. Для этого необходимо найти файл ниже и выполнить инструкцию -> Run:
```java
@SpringBootApplication
public class FiresideApplication {
	public static void main(String[] args) {
		SpringApplication.run(FiresideApplication.class, args);
	}
}
```
Помимо этого запустить проект можно непосредственно с помощью Maven:
```bash
./mvnw spring-boot:run
```
Также если у вас нет Maven, Spring, Postgres, но при этом есть Docker существует возможность запустить проект через него, для этого необходимо склонировать репозиторий к себе, перейти в каталог src/main/docker после чего ввести команду:
<img src="https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png" width="500px" height="400px">
```docker
docker-compose up
```
