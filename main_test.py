import Rheology


def reo(_fann):
    rh = Rheology.Rheology(_fann)
    reo_res = rh.reo()
    # sns_res = rh.sns_1()
    print(f'Значение PV:\t {reo_res[0]}')
    print(f'Значение YV:\t {reo_res[1]:.2f}')
    # print('Значение СНС: ', sns_res[0], '/', sns_res[1])


while True:
    print('')
    choise = input('Для теста введите "t", для ввода введите "w" :').lower()
    print('')

    # Функция для тестирования
    if choise == 't':
        _fann = {'600 prm': 100, '300 prm': 81, '200 prm': 72, '100 prm': 62, '6 prm': 48, '3 prm': 47}
        reo(_fann)


    # Функция для работы
    elif choise == 'w':
        _fann = {'600 prm': 0, '300 prm': 0, '200 prm': 0, '100 prm': 0, '6 prm': 0, '3 prm': 0}
        for i in _fann:
            while True:
                try:
                    _fann[i] = int(input(f'Введите значение для {i}:'))
                    break
                except ValueError:
                    print('')
                    print('Вводить можно только целые значения')
                    #_fann[i] = int(input(f'Введите значение для {i}:'))

        print('')
        reo(_fann)
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






