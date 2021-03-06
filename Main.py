#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Rheology
from plot import logplot
import colorama
from colorama import Fore, Back, Style
import const
import configparser
import os
import time


def reo(_fann, model):
    '''
    reo() - на данный момент основная функция расчёта
    реологических параметров бурового рствора
    '''
    rh = Rheology.Rheology(_fann)
    reo_res = rh.reo(model)
    return reo_res
    # sns_res = rh.sns_1()


def beautyTable(reo_res):
    '''
    небольшая функция для красивового выовда значений
    max_lenth - хранит набиольшую длинну строки
    Используя ljust() - функция выравнивает поо левому краю
    :param reo_res: dict
    '''
    max_lenth = 0
    for i in reo_res:
        if len(i) >= max_lenth:
            max_lenth = len(i)
    print()

    for res in reo_res:
        yield res.replace('_', ' ').capitalize().ljust(
            max_lenth + 5), f'{reo_res[res]:.4f}'

def seve(data, filename='default'):
    '''
    Функция для записи полученных результатов в файл
    :return: true
    '''
    try:
        if filename is 'default':
            filename = time.strftime("%d-%m-%Y-%H.%M.%S", time.localtime())
        with open(filename, 'w') as new:
            text = beautyTable(data)
            for i in text:
                new.write(i)
        return True
    except Exception as e:
        print(f'\nХм, странная ошибка типа: {e}')


def load(filename):
    '''
    Функция для чтения исходных данных с файла
    :return: trye
    '''

    pass

def test():
    '''
    Тестовая функция для отработки
    :return: - ничего
    '''



    _fann = {'600': 100, '300': 81, '200': 72,
             '100': 62, '6': 48, '3': 47}

    text = configparser.ConfigParser()
    text.read_file('text.ini')

    title = text.get('main', u'text')
    print(title)

    title = {'1': 'Herschel-Bulkley Model', '2': 'Power Law Model',
            '3': 'Bingham Plastic Model'}

    # rh = Rheology.Rheology()
    # reo_res = rh.hbModel(_fann)
    test = beautyTable(_fann)

    for i in text:
        print(*i)
        
    logplot(_fann, title['1'])

    # отправляем заначения, получаем результат
    # model = 'pl'
    # reo_res = reo(_fann, model)
    # beautyTable(reo_res)
    stop()


def work():
    '''
    _fann - словарь в который вносим покаания шкалы вискозиметра
    :return: - ничего, функция управля.щая и только отправляет другим функциям
    '''
    rh = Rheology.Rheology()
    _fann = {'600': 0, '300': 0, '200': 0,
             '100': 0, '6': 0, '3': 0}

    data = {}
    # вводим показания шкалы вискозиметра в словарь
    for i in _fann:
        while True:
            try:
                _fann[i] = float(input(f'Введите значение для {i} prm: '))
                break
            except ValueError:
                print('\nВводить можно только целые значения\n')
    '''
    Выбираем реологическую модель по которой будем работа, см const.py
    '''
    # оотправляем заначения, получаем результат
    while True:
        # model - выбираем реологическую модель
        model = input(const.text)

        if model == '1':
            rh.hbModel(_fann)
            break


        elif model == '2':
            rh.powerLowModel(_fann)
            break

        elif model == '3':
            pass

        elif model == '0':
            return
        else:
            print('Вы ввели неправильное значение\n')
    # предлагаем расчитать потри давления и т.д.
    while True:
        choise = input(const.text_hydr)
        if choise == '1':
            for i in const.hydr:
                while True:
                    try:
                        data[i] = float(input(const.hydr[i] + ': '))
                        break
                    except:
                        print('Неверное значение')

            rh.hydro(data)
            break
        elif choise == '0':
            return
        else: print(const.errore)

    text = beautyTable(rh._dict)
    for i in text:
        print(*i)

    logplot(_fann, const.tile[model])
    return True




def stop():

    print('\n\tДля продолжения нажмите "Enter"\n\
\t0 - Для заверщения работы введите')
    next_choise = input('Введите: ').lower()
    if next_choise in {'s', '0'}:
        print('Ввод завершён')
        return exit()


def main():

    colorama.init()
    '''
    Здесь находится логика отвечающая за взаимодействие в "программе"
Писутствует два варианта, для тестирования и для непосредственного
ввода значений.
Для тестирования достаточно ввести "1"
Для ввода значений нужно ввести "2"
Для остановки работы и вохода "s"/"0"
    '''
    print()
    print(Fore.RED + '\n\t _     _             |¯|  |¯|      |¯|                   |¯|      ')
    print(Fore.RED +'\t| \   / |  _   _   __| |  | |      | |  ______   _____   | |___   ')
    print(Fore.RED +'\t|  \ /  | | | | | |    |  | |  /\  | | |  __  | |  __ \  |  __ \  ')
    print(Fore.RED +'\t|   V   | | | | | | || |  | \ /  \ / | | |  | | | |__) | | |__) | ')
    print(Fore.RED +'\t| |\ /| | | |_| | | || |   \ V /\ V /  | |__| | |  _  /  |  _  /  ')
    print(Fore.RED +'\t|_| V |_| |_____| |____|    \_/  \_/   |______| |_| \__\ |_| \__\ ')

    colorama.init()
    while True:
        print(Fore.GREEN +'\n\tДля выбора режима введите одну из цыфр:\n \
\n\t1 - [Test] Запуск тестово функции.\
\n\t2 - [Work] Запуск рабочй модели.\
\n\t0 - [Exit] Выход из приложения.')

        choise = input(
            '\nВведите: ').lower()

        # Функция для тестирования
        if choise == '1':
            test()

        # Функция для работы
        elif choise == '2':
            work()

        elif choise in ('s', '0'):
            print('\nРабота завершена')
            exit()

        else:
            print('Неверный ввод')


if __name__ == '__main__':
    main()
