Генерация UUID по правилам ЦБ РФ
================================

Реализация SWIG интерфейса библиотеки uuid от ЦБ РФ для Python

Библиотека uuid загружена с официального сайта ЦБ РФ (https://cbr.ru/ckki/assignment_unique_id/)


Установка:
-----------
С помощью pip install
::

    pip install uuid_cbr

Пример использования:
---------------------
::

    >>>  import uuid_cbr as uuuid
    >>>  print(uuuid.uuid())
    e4028fe0-2c49-11eb-98b1-6d42da06be14-6

