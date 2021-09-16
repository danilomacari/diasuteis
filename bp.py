from datetime import datetime as dt
import datetime
import csv


# with open('c:\\pp\\bd\\hBR.csv') as f:
with open('.hBR.csv') as f:
    reader = csv.reader(f)
    feriadosAux = list(reader)

feriados = []
for item in feriadosAux:
    feriado = dt.strptime(item[0], '%d/%m/%Y')
    if feriado.weekday() < 5:
        feriados.append(feriado)


def du(inicio, fim):

    #    inicio = '15/09/2021'
    #    fim = '15/05/2055'
    di = dt.strptime(inicio, '%d/%m/%Y')
    df = dt.strptime(fim, '%d/%m/%Y')
    diff = df.date()-di.date()
    semanasInteiras = diff.days//7
    edt = di+datetime.timedelta(days=semanasInteiras*7)

    if (edt.weekday() > df.weekday()):
        result = (df.date()-edt.date()).days+5*semanasInteiras-2
    else:
        result = (df.date()-edt.date()).days+5*semanasInteiras

    naoUteis = sum(i > di and i <= df for i in feriados)
    result = result-naoUteis
    return result


def somadu(inicio, ndu):
    result = dt.strptime(inicio, '%d/%m/%Y')
    for i in range(ndu):
        result = result+datetime.timedelta(days=1)
        while(result.weekday() == 5 or result.weekday() == 6 or result in feriados):
            result = result+datetime.timedelta(days=1)
    return result


print(somadu('09/09/2021', 83))

'''
x = dt.strptime('07/09/2021', '%d/%m/%Y')
print('sabado? ' + str(x.weekday() == 5))
print('domingo? ' + str(x.weekday() == 6))
print('feriado? ' + str(x in feriados))


with open('c:\\pp\\bd\\teste.csv') as f:
    reader = csv.reader(f)
    dtsaux = list(reader)


dts = []
for item in dtsaux:
    print(du('15/09/2021', item[0]))
'''
