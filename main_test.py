# import Rheology
#
#
# rh = Rheology.Rheology()

# constants

# rh.rpm_600 = 100
# rh.rpm_300 = 81
# rh.rpm_200 = 72
# rh.rpm_100 = 62
# rh.rpm_6 = 48
# rh.rpm_3 = 47
# rh.sns_10s = 10
# rh.sns_10m = 35
#
# fann = ['600 prm', '300 prm', '200 prm', '100 prm', '6 prm', '3 prm', 'sns 10s', 'sns 10m']
# rh_func = [rh.rpm_600, rh.rpm_300, rh.rpm_200, rh.rpm_100, rh.rpm_6, rh.rpm_3, rh.sns_10s, rh.sns_10m]

# for i in range(8):
#     print('Введите показание шкалы вискозиметра при ' + fann[i] + ': ', end='')
#     # тут ловим ошибку если вовдится не число
#     while True:
#         try:
#             value = rh_func[i]
#             input_value = int(input())
#             break
#         except ValueError:
#             print('Введите число')
#             print('Введите показание шкалы вискозиметра при ' + i + ': ', end='')

# rh.rpm_600 = int(input('Введите значение 600 prm: '))
# rh.rpm_300 = int(input('Введите значение 300 prm: '))
# rh.rpm_200 = int(input('Введите значение 200 prm: '))
# rh.rpm_100 = int(input('Введите значение 100 prm: '))
# rh.rpm_6 = int(input('Введите значение 6 prm: '))
# rh.rpm_3 = int(input('Введите значение 3 prm: '))
# rh.sns_10s = int(input('Введите значение СНС 10 с: '))
# rh.sns_10m = int(input('Введите значение СНС 10 м: '))


# fann = {'600 prm': '0', '300 prm': 0, '200 prm': 0, '100 prm': 0, '6 prm': 0, '3 prm': 0, 'sns 10s': 0, 'sns 10m': 0}
#
# for i in fann:
#     fann[i] = int(input('Введите значение для ' + i + ':'))
#
# reo_res = rh.reo()
# sns_res = rh.sns_1()
# print('Значение PV: ', reo_res[0])
# print('Значение YV: ', reo_res[1])
# print('Значение СНС: ', sns_res[0], '/', sns_res[1])

class Rheology:

    def __init__(self, *args):

        self.rpm_600 = fann['600 prm']
        self.rpm_300 = fann['300 prm']

    def visc(self):
        PV = self.rpm_600 - self.rpm_300
        return PV

fann = {'600 prm': 0, '300 prm': 0, '200 prm': 0, '100 prm': 0, '6 prm': 0, '3 prm': 0, 'sns 10s': 0, 'sns 10m': 0}

for i in fann:
    fann[i] = int(input('Введите значение для ' + i + ':'))

rh = Rheology()
print(rh.visc())
