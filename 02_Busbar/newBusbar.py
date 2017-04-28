

# Czy to działa?

print('Tak')

class przewodnik:
    '''To jest nasza pierwsza klasa'''

    def __init__(self, dlugosc, wysokosc, grubosc, sigma=58e6):

        self.l = dlugosc*1e-3
        self.h = wysokosc*1e-3
        self.g = grubosc*1e-3
        self.sigma = sigma

        self.A = self.g * self.h
        self.R = self.l / (self.A * self.sigma)

        self.collingA = 2*(self.g + self.h) * self.l

        print('Udało się!')

    def __str__(self):
        return 'jestem przewodnikiem i mam R={} i A={}'.format(round(self.R, 8), self.A)

    def __repr__(self):
        return 'jestem przewodnikiem i mam R={} i A={}'.format(round(self.R, 8), self.A)


    # Definiujemy metody obiektów
    def getPowerLoss(self, current):
        '''Ta metoda zwraca strty mocy dla danej wartosci prądu = current'''
        return self.R * current**2

    def getTemp(self, stratyMocy, Htc=4, Tambient=20):
        '''Ta metoda zwraca tmperature szyny '''
        return stratyMocy /(self.collingA * Htc) + Tambient



print(przewodnik)

obiekt = przewodnik(1000, 100, 10, 25e6)
szyna = przewodnik(1000,40,10)

print('########################')
print(obiekt)
print(szyna)

print('########################')

print(szyna.getTemp(szyna.getPowerLoss(1000)))

mojeSzyny = [10,20,100,100,30,40,50,10,10,90,234,999]

listaSzyn =[]

for wysokosc in mojeSzyny:
    listaSzyn.append(przewodnik(1000,wysokosc,10))

print(listaSzyn)

for szyna in listaSzyn:
    print(szyna.getTemp(szyna.getPowerLoss(2000)))

# for i in range(0,len(listaSzyn),1):
#     zmiennatemp = listaSzyn[i].getTemp(listaSzyn[i].getPowerLoss(2000))
#     print(zmiennatemp)
