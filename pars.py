mes = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
       'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
tsts = []

with open('4242.txt') as tlog:
    for i in tlog:
        if 'Result:' in i:
            print(res := (i[i.find('Result:'):])[0:15])
        if (d := 'Date:') in i:
            d = str(i[i.find(d):])
            dt = mes.index(d1 := d[9:12])+1
            print(f'{d[:8]}.{dt}.{d[13:]}')
        if 'Test  :' in i:
            print(tst := (i[i.find('Test  :'):])[0:43].strip())
            tsts.append(tst[8:43])

print(tsts)

