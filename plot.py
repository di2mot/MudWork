#!/usr/bin/python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib import ticker
from collections import OrderedDict
import math
import const

def logplot(data, title = 'Graph', dict = 'default'):
    '''
    logplot - расчитана на работу с 6 скоростями вискозиметров на подобие Fann 800

    Скорости идут от большего к меньшему
    :param data: - на вход принимает словарь вида {'скорость':'показатель шкалы'}
                скорости идут от большего к меньшему (600 -> 3)
    :param title: - название реологической модели
    :return: - ничего не возвращает, жадная функция
    '''

    x_data = []
    y_data = []

    if dict is 'defoult':
        x_data = const.x_data

        for i in x_data:
            y_data.append(data[str(i)])
    elif dict is 'costum':
        # сортируем словарь в обратном порядке
        sorted_dict = OrderedDict(sorted(data.items(), key=lambda x: x[1]))

        # Создаём кортеж для данных и кортеж для обозначений
        for x in sorted_dict:
            x_data.append(int(x))

        # Создаём кортеж для данных и кортеж для обозначений
        for x in sorted_dict:
            y_data.append(sorted_dict[x])
    else:
        print(f'\nНеверный формат входящих данных \n{data}')

    _, ax = plt.subplots(figsize=(9, 5))

    ax.plot(x_data,
            y_data,
            color='#200094',
            alpha=1,
            marker='o',
            markerfacecolor="#ff22aa")
    # задний фон
    rect = ax.patch
    rect.set_facecolor('#bbbabf')
    rect.set_alpha(0.25)

    ax.set_title(title)
    ax.set_xlabel('prm')
    ax.set_ylabel('angles')

    plt.yscale('log')
    plt.xscale('log')

    ax.set_xlim(1, 1000)
    ax.set_ylim(1, 1000)

    # Преобразует значения подписей шкал из логарифмических, в нелогарфифмические
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))
    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter("%d"))



    # добавляем подписи к маркерам
    for i in range(len(y_data)):
        x = x_data[i]
        # тупо что бы было красиво
        if y_data[i] in ('0', '1'):
            add = 1
        elif y_data[i] < 10:
            add = math.ceil(math.log(y_data[i], 10)) * 2
        elif y_data[i] >= 10:
            add = math.ceil(math.log(y_data[i], 10)) * 5
        y = y_data[i] + add

        # отвечает за рисунок
        ax.text(x, y, str(y_data[i]), color='r')

    # Основные линии
    ax.grid(True, which='major', color='black', linestyle='-', alpha=0.5)

    # Вспомогатльные линии
    ax.grid(True, which='minor', color='#616161', linestyle='dashed', alpha=0.5)

    plt.show()

if __name__ == '__main__':
    _fann = {'600': 100, '300': 81, '200': 72,
             '100': 62, '6': 48, '3': 47}
    logplot(_fann)


