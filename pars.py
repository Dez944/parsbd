mes = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
       'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
tsts = []
resl = []
dat = []

t = open('res.txt','w')
with open('tstbd.mrd', errors = 'ignore') as tlog:
    for i in tlog:
        if 'Test  :' in i:
            t.write((tst := (i[i.find('Test  :'):])[8:43].strip()))
            t.write('\n')
            tsts.append(tst)

        if (d := 'Date:') in i:
            d = i[i.find(d):].strip()
            dt = mes.index(d1 := d[9:12])+1
            t.write((rd := f'{d[:8]}.{dt}.{d[13:]}'))
            t.write('\n')
            dat.append(rd)
            f = True

        if 'Result: ' in i and f:
            t.write((res := (i[i.find(' Result:'):])[0:15].strip()))
            t.write('\n')
            resl.append(res)
            f = False
