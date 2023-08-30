def zamien(*x, szukane, zamiana, ilosc = -1, start=-1):
    ret = ""
    start-=1
    for ciag in x:
        strTmp = str(ciag)
        for slowo in strTmp.split(' '):
            indexZnajdz =-1
            while True:
                indexZnajdz = slowo.find(szukane, indexZnajdz+1) if indexZnajdz > -2 else -2
                if indexZnajdz == -1: indexZnajdz = -2
                if indexZnajdz >=0 and (ilosc == -1 or ilosc > 0) and start<=-1:
                    slowo = slowo[:indexZnajdz] + zamiana + slowo[indexZnajdz+len(szukane):]
                    ilosc -= 1 if ilosc > 0 else 0

                elif start>-1 and indexZnajdz >= 0:
                    start-=1
                    continue
                else: break
            ret += slowo + ' '
    return ret


ciag = 45665758833
mStr = zamien(ciag, " To kolejny przypadek", 5672213, "Dalsze 66566 wiadomości", szukane='6', zamiana='1')
print(mStr)
