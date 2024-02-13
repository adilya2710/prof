import csv


def g(fio):
    s = 'ЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁйцукенгшщзхъфывапролджэчсмитьбюё '
    p = 67
    m = 10**9 + 9
    pwr = 1
    h = 0
    for c in fio:
        h = h + ((s.index(c) + 1) * pwr) % m
        pwr = (pwr * p) % m
    return h

with open('students.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    answer = list(reader)
print(answer)
for i in range(len(answer)):
    if answer[i][0] == 'id':
        answer[i][0] = 'id_has'
    else:
        answer[i][0] = str(g(answer[i][1]))
print(answer)

with open('students_neww.csv', 'w', newline ) as file2:


