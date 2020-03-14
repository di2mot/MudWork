#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Rheology
from plot import logplot
import colorama
from colorama import Fore, Back, Style



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
    :param reo_res: dict
    '''
    max_lenth = 0
    for i in reo_res:
        if len(i) >= max_lenth:
            max_lenth = len(i)
    print()
    for res in reo_res:
        print(res.replace('_', ' ').capitalize().ljust(
            max_lenth + 5), f'{reo_res[res]:.4f}')


def test():
    _fann = {'600': 100, '300': 81, '200': 72,
             '100': 62, '6': 48, '3': 47}
    tile = {'1': 'Herschel-Bulkley Model', '2': 'Power Law Model',
            '3': 'Bingham Plastic Model'}
    # rh = Rheology.Rheology()
    # reo_res = rh.hbModel(_fann)
    beautyTable(_fann)
    logplot(_fann, tile['1'])

    # отправляем заначения, получаем результат
    # model = 'pl'
    # reo_res = reo(_fann, model)
    # beautyTable(reo_res)
    stop()


def work():
    rh = Rheology.Rheology()
    _fann = {'600': 0, '300': 0, '200': 0,
             '100': 0, '6': 0, '3': 0}
    tile = {'1':'Herschel-Bulkley Model', '2':'Power Law Model',
                  '3':'Bingham Plastic Model'}
    for i in _fann:
        while True:
            try:
                _fann[i] = float(input(f'Введите значение для {i} prm: '))
                break
            except ValueError:
                print('\nВводить можно только целые значения\n')

    # оотправляем заначения, получаем результат
    text = '\nВыберите реологическую модель:\n\
    \t1 - [Herschel-Bulkley Model]  \n\
    \t2 - [Power Law Model]\n\
    \t3 - [Bingham Plastic Model (Not work)]\n\
    \t0 - Для воврата в меню.\n\
    \tВвод: '

    while True:
        model = input(text)
        if model == '1':
            reo_res = rh.hbModel(_fann)
            beautyTable(reo_res)
            logplot(_fann, tile[model])
            stop()
            break

        elif model == '2':
            reo_res = rh.powerLowModel(_fann)
            beautyTable(reo_res)
            logplot(_fann, tile[model])
            stop()
            break

        elif model == '3':
            pass

        elif model == '0':
            main()
        else:
            print('Вы ввели неправильное значение\n')



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
