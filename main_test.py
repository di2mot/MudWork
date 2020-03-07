import Rheology


rh = Rheology.Rheology()

# constants

rh.rpm_600 = 100
rh.rpm_300 = 81
rh.rpm_200 = 72
rh.rpm_100 = 62
rh.rpm_6 = 48
rh.rpm_3 = 47
rh.sns_10s = 10
rh.sns_10m = 35

fann = ['600 prm', '300 prm', '200 prm', '100 prm', '6 prm', '3 prm', 'sns 10s', 'sns 10m']
rh_func = [rh.rpm_600, rh.rpm_300, rh.rpm_200, rh.rpm_100, rh.rpm_6, rh.rpm_3, rh.sns_10s, rh.sns_10m]

for i in range(8):
    print('Введите показание шкалы вискозиметра при ' + fann[i] + ': ', end='')
    # тут ловим ошибку если вовдится не число
    while True:
        try:
            value = rh_func[i]
            input_value = int(input())
            break
        except ValueError:
            print('Введите число')
            print('Введите показание шкалы вискозиметра при ' + i + ': ', end='')


print(rh.sns_1())
