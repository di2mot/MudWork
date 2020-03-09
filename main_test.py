import Rheology

'''
reo() - на данный момент основная функция расчёта
реологических параметров бурового рствора
'''


def reo(_fann, model):
    rh = Rheology.Rheology(_fann)
    reo_res = rh.reo(model)
    return reo_res
    # sns_res = rh.sns_1()


def beautyTable(reo_res):
    max_lenth = 0
    for i in reo_res:
        if len(i) >= max_lenth:
            max_lenth = len(i)

    for res in reo_res:
        print(res.replace('_', ' ').capitalize().ljust(
            max_lenth + 5), f'{reo_res[res]:.4f}')


def stop():

    print('\nДля заверщения работы введите "s", \
    для продолжения нажмите "Enter"\n')
    next_choise = input('Введите: ').lower()
    if next_choise == 's':
        print('Ввод завершён')
        return exit()


def main():
    '''
    Здесь находится логика отвечающая за взаимодействие в "программе"
Писутствует два варианта, для тестирования и для непосредственного
ввода значений.
Для тестирования достаточно ввести "t"
Для ввода значений нужно ввести "w"
Для остановки работы и вохода "s"
    '''

    while True:

        choise = input(
            '\nДля теста введите "t", для ввода введите "w": ').lower()

        # Функция для тестирования
        if choise == 't':
            _fann = {'600 prm': 100, '300 prm': 81, '200 prm': 72,
                     '100 prm': 62, '6 prm': 48, '3 prm': 47}
            beautyTable(_fann)
            print('')

            # отправляем заначения, получаем результат
            model = 'pl'
            reo_res = reo(_fann, model)
            beautyTable(reo_res)

            stop()

        # Функция для работы
        elif choise == 'w':
            _fann = {'600 prm': 0, '300 prm': 0, '200 prm': 0,
                     '100 prm': 0, '6 prm': 0, '3 prm': 0}
            for i in _fann:
                while True:
                    try:
                        _fann[i] = int(input(f'Введите значение для {i}: '))
                        break
                    except ValueError:
                        print('\nВводить можно только целые значения\n')

            # оотправляем заначения, получаем результат
            text = '\nВыберите реологическую модель:\n\
            bh - Bingham Plastic Model (Not work)\n\
            pl - Power Law Model\n\
            hb - Herschel-Bulkley Model  \n\
            Ввод: '

            while True:
                try:
                    model = str(input(text))
                    reo_res = reo(_fann, model)
                    beautyTable(reo_res)
                    stop()
                    break
                except ValueError:
                    print('\nВводить можно только текст\n')



        elif choise == 's':
            print('\nРабота завершена')
            break

        else:
            print('Неверный ввод')


if __name__ == '__main__':
    main()
