#!/usr/bin/python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from collections import OrderedDict
import math

def logplot(data, title = 'Graph'):
    x_data = []
    y_data = []

    # сортируем словарь в обратном порядке
    sorted_dict = OrderedDict(sorted(data.items(), key=lambda x: x[1]))

    # Создаём кортеж для данных и кортеж для обозначений
    for x in sorted_dict:
        x_data.append(int(x))

    # Создаём кортеж для данных и кортеж для обозначений
    for x in sorted_dict:
        y_data.append(sorted_dict[x])

    # x_data = [3, 6, 100, 200, 300, 600]
    # y_data = [47, 48, 62, 72, 81, 100]

    x_lable = [1, 3, 6, 10, 100, 200, 300, 600, 1000]
    y_lable = [1, 3, 5, 10, 50, 100, 150, 200, 1000]

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

    # н знаю почему, но как говорится, без этого не работает
    plt.xticks(x_lable)
    plt.yticks(y_lable)
    #
    # # axis signatures
    ax.set_xticklabels(x_lable)
    ax.set_yticklabels(y_lable)



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

    # Вспомогатльные линии
    # ax.grid(True, which='major', color='#616161', linestyle='-', alpha=0.5)
    ax.grid(True, which='major', color='black', linestyle='-', alpha=0.5)
    ax.grid(True, which='minor', color='#616161', linestyle='dashed', alpha=0.5)

    plt.show()



