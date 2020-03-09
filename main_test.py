import Rheology

'''
reo() - на данный момент основная функция расчёта реологических параметров бурового рствора
'''
def reo(_fann):
    rh = Rheology.Rheology(_fann)
    reo_res = rh.reo()
    return reo_res
    # sns_res = rh.sns_1()


'''
Здесь находится логика отвечающая за взаимодействие в "программе"
Писутствует два варианта, для тестирования и для непосредственного ввода значений.
Для тестирования достаточно ввести "t"
Для ввода значений нужно ввести "w"
Для остановки работы и вохода "s"
'''
while True:
    print('')
    choise = input('Для теста введите "t", для ввода введите "w": ').lower()
    print('')

    # Функция для тестирования
    if choise == 't':
        _fann = {'600 prm': 100, '300 prm': 81, '200 prm': 72, '100 prm': 62, '6 prm': 48, '3 prm': 47}
        for i in _fann:
            print(f'{i}:\t{_fann[i]}')
        print('')

        # оотправляем заначения, получаем результат
        model = 'power_low'
        reo_res = reo(_fann, model)
        for res in reo_res:
            print(res, '\t', f'{reo_res[res]:.4f}')

        print('')
        print('Для заверщения работы введите "s", для продолжения нажмите "Enter"')
        next_choise = input('Введите: ').lower()
        if next_choise == 's':
            print('Ввод завершён')
            break

    # Функция для работы
    elif choise == 'w':
        _fann = {'600 prm': 0, '300 prm': 0, '200 prm': 0, '100 prm': 0, '6 prm': 0, '3 prm': 0}
        for i in _fann:
            while True:
                try:
                    _fann[i] = int(input(f'Введите значение для {i}: '))
                    break
                except ValueError:
                    print('')
                    print('Вводить можно только целые значения')

        print('')

        # оотправляем заначения, получаем результат
        reo_res = reo(_fann)
        for res in reo_res:
            print(res, '\t', f'{reo_res[res]:.4f}')

        print('')
        print('Для заверщения работы введите "s", для продолжения нажмите "Enter"')
        next_choise = input('Введите: ').lower()
        if next_choise == 's':
            print('Ввод завершён')
            break

    else:
        print('')
        print('Неверный ввод')
        choise = input('Для теста введите "t", для ввода введите "w"').lower()







