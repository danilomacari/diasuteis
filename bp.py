from datetime import datetime as dt
import datetime
import csv


with open('c:\\pp\\bd\\hBR.csv') as f:
    reader = csv.reader(f)
    feriadosAux = list(reader)

feriados = []
for item in feriadosAux:
    feriado = dt.strptime(item[0], '%d/%m/%Y')
    if feriado.weekday() < 5:
        feriados.append(feriado)


def du(inicio, fim):
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
    # m eh negativo se ndu < 0
    m = int(ndu/abs(ndu))
    for i in range(abs(ndu)):
        result = result+datetime.timedelta(days=1*m)
        while(result.weekday() == 5 or result.weekday() == 6 or result in feriados):
            result = result+datetime.timedelta(days=1*m)
    return result
