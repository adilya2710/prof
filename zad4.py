import csv
import random

with open('students.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=',')
    answer = list(reader)
print(answer)

def password():
    s = 'QWERTYUIOPASDFGHJKLXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    while(True):
        pas = ''
        for i in range(8):
            pas = pas + random.choice(s)
        a = 0
        b = 0
        c = 0
        for i in range(len(pas)):
            if 'A' <= pas[i] <= 'Z':
                a += 1
            if 'a' <= pas[i] <= 'z':
                b += 1
            if '0' <= pas[i] <= '9':
                c += 1
        if a != 0 and b != 0 and c != 0:
            return pas

for i in range(len(answer)):
    if answer[i][1] == 'Name':
        answer[i].append('login')
    else:
        sp = answer[i][1].split()
        otv = sp[0] + '_' + sp[1][0] + sp[2][0]
        answer[i].append(otv)
        answer[i].append(password())

with open('student_password.csv', 'w', newline = '') as file2:
    writer = csv.writer(file2)
    itog = writer.writerows(answer)