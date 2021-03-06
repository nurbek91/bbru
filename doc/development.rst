=================
Методы разработки
=================

.. contents::
   :local:

Документ описывает методы, практики и приемы, применяемые в работе
с кодом.

Совместная разработка c использованием GitHuB
=============================================

Создать публичный форк репозитория. Для этого нужно зайти на страницу
главного репозитория (mainstream) по адресу http://github.com/astoon/bbru
и нажать кнопку "Fork", создав таким образом репозиторий для открытой
публикации своих изменений. Клонировать его на локальную машину::

  $ git clone git@github.com:your_login/bbru.git
  $ cd bbru

Для отслеживания изменений в главном репозитории и синхронизации с ним
по необходимости, нужно добавить его в список дистанционных репозиториев::

  $ git remote add main git://github.com/astoon/bbru.git
  $ git fetch main

Вместо `main` может быть другое произвольное имя. Таким образом,
в локальном репозитории будет зарегистрировано 2 дистанционных: origin
(личный, с которого клонировали) и main.

Далее происходит работа с локальным репозиторием, см. документацию к git.

Для того, чтобы предложить внести свои изменения в mainstream, нужно
сначала сделать их доступными для просмотра (т.е. опубликовать),
вытолкнув их в свой публичный репозиторий. Однако перед этим
рекомендуется синхронизировать свой код с главным репозиторием::

  $ git fetch main
  $ git merge main/master

.. это более безопасный вариант, чем сразу pull

Публикация изменений::

  $ git push origin master

На своей странице проекта нажать кнопку "Pull Request", заполнить форму.

.. где-то здесь нужно про --rebase


Патчи
=====

Можно отсылать патчи по адресу team@bluebream.ru


Действия при обновлении кода
============================

При изменении исходного кода пересобирать проект обычно нет необходимости.
Есть лишь несколько файлов, непосредственно участвующих в сборке приложения::

- setup.py
- buildout.cfg
- versions.cfg
- файлы в директории templates/

Если они обновлены, значит следует пересобрать проект::

  >>> bin/buildout

Всегда нужно запускать конфигуратор Upgrade. Конфигураторы пишутся так,
что их можно запускать многократно - повторная установка компонент
исключается.

В отдельных случаях нужно запускать генерации базы данных. Это можно
увидеть, открыв страницу генераций.


Намылить, смыть, повторить
==========================

Если разработчик не знает, с чего начать - значит нужно начать с написания
тестов. Делается это так:

1. В директории модуля bbru.tests cоздается файл с осмысленным названием
   и расширением `.rst`. В него копируется начальная часть файла `frontpage.rst`
   (подготовка тестового окружения и установка/настройка локального сайта).

2. Далее пишутся необходимые тесты будущего функционала. Важное значение
   имеет описательная составляющая - пишем на русском языке.

3. Одновременно с этим или позже пишутся интерфейсы.

4. Интерфейсы реализуются до тех пор, пока все тесты не пройдут.


Написание тестов
================

1. Когда нужно временно деактивировать тестовый файл, достаточно поставить
   символ `#` перед маркером теста, т.е. `#:doctest:`

2. Кроме доктестов, можно писать и модули с юнит-тестами unittest.TestCase.
   Чтобы тестовый фреймворк z3c.testsetup распознал такой модуль, нужно начать
   файл так::

     """
     :unittest:
     """

     import unittest
     import zope.component

     class Test(unittest.TestCase):
        def test_foo(self):
           # ...
