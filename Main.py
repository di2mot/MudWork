import Rheology
import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np
import math
from collections import OrderedDict


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
    beautyTable(_fann)
    print('')

    # отправляем заначения, получаем результат
    # model = 'pl'
    # reo_res = reo(_fann, model)
    # beautyTable(reo_res)

    lineplot(_fann)
    stop()


def work():
    _fann = {'600': 0, '300': 0, '200': 0,
             '100': 0, '6': 0, '3': 0}
    tile = {'1':'Herschel-Bulkley Model', '2':'Power Law Model',
                  '3':'Bingham Plastic Model'}
    for i in _fann:
        while True:
            try:
                _fann[i] = int(input(f'Введите значение для {i} prm: '))
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
        if model in ('1', '2', '3'):
            reo_res = reo(_fann, model)
            beautyTable(reo_res)

            plot_type = 'log'
            lineplot(_fann, plot_type, tile[model])
            stop()
            break

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


def lineplot(data, plot_type = 'log', title="График"):

    x_data = []
    y_data = []
    x_label = []
    y_label = []

    # Create the plot object
    _, ax = plt.subplots(figsize=(10,4))

    # сортируем словарь в обратном порядке
    sorted_dict = OrderedDict(sorted(data.items(), key=lambda x: x[1]))

    # Создаём кортеж для данных и кортеж для обозначений
    for x in sorted_dict:
        x_label.append(str(x))
        #x_data.append(math.log10(int(x)))
        x_data.append(int(x))

    # Создаём кортеж для данных и кортеж для обозначений
    for x in sorted_dict:
        y_label.append(str(sorted_dict[x]))
        #y_data.append(math.log10(sorted_dict[x]))
        y_data.append(sorted_dict[x])

    print(x_data, y_data, x_label, y_label)
    # Plot the best fit line, set the linewidth (lw), color and
    # transparency (alpha) of the line


    # Label the axes and provide a title
    # ax.loglog()



    #
    # ax.set_title(title)
    # ax.set_xlabel('prm')
    # ax.set_ylabel('Углы')
    # ax.set_xticklabels(x_label)
    # ax.set_yticklabels(y_label)



    ax.plot(x_data, y_data, color='#539caf', alpha=1)
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))

    ax.set_title(title)
    ax.set_xlabel('prm')
    ax.set_ylabel('углы')
    ax.set_yscale('log')
    ax.set_xscale('log')
    # ax.set_xticks(x_data)
    # ax.set_yticks(y_data)
    # ax.set_xticklabels(x_label)
    # ax.set_yticklabels(y_label)



    # plt.xscale('log')
    # plt.yscale('log')
    # plt.yticks(y_data, y_label)
    # plt.xticks(x_data, x_label)

    ax.grid(True)



    plt.grid(True)
    plt.show()


def main():
    '''
    Здесь находится логика отвечающая за взаимодействие в "программе"
Писутствует два варианта, для тестирования и для непосредственного
ввода значений.
Для тестирования достаточно ввести "1"
Для ввода значений нужно ввести "2"
Для остановки работы и вохода "s"/"0"
    '''
    print()
    print('\t _     _             |¯|  |¯|      |¯|                   |¯|      ')
    print('\t| \   / |  _   _   __| |  | |      | |  ______   _____   | |___   ')
    print('\t|  \ /  | | | | | |    |  | |  /\  | | |  __  | |  __ \  |  __ \  ')
    print('\t|   V   | | | | | | || |  | \ /  \ / | | |  | | | |__) | | |__) | ')
    print('\t| |\ /| | | |_| | | || |   \ V /\ V /  | |__| | |  _  /  |  _  /  ')
    print('\t|_| V |_| |_____| |____|    \_/  \_/   |______| |_| \__\ |_| \__\ ')


    while True:
        print('\n\tДля выбора режима введите одну из цыфр:\n \
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
