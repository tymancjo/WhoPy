 # This is our busbar python script project

class busbar:
    '''This is main class that will represent busbar object'''

    listOfbusbars = []

    sigma20C = 58e6 # Default conductivity @ 20degC
    thermalRcoef = 3.9e-3 # Default thermal coeff of resistance

    def __init__(self, wysokosc, grubosc, dlugosc, sigma=sigma20C):
        busbar.listOfbusbars.append(self) # We add ourself to the list

        self.wysokosc = wysokosc*1e-3
        self.grubosc = grubosc*1e-3
        self.dlugosc = dlugosc*1e-3
        self.sigma = sigma*1e-3

        self.coolingArea = (2 * self.wysokosc + 2 * self.grubosc) * self.dlugosc

        self.xSec = self.wysokosc * self.grubosc

        self.R = self.dlugosc / (self.xSec*sigma)

    def __str__(self):

        return 'This is conductor bar:\nl={}[m]\nH={}[m]\nW={}[m]\n\nCalculated:\nR={}[ohm]\nArea={}[m^2]'\
        .format(self.dlugosc, self.wysokosc, self.grubosc, self.R, self.coolingArea)

    def powerLosses(self,current=1):
        return self.R * current**2

    def temperature(self, powerLosses, HTC=5, Tamb = 20):
        # Q = A*HTC*(T-Tamb)
        # Q/(A*HTC) + Tamb = T
        return   Tamb + powerLosses / (self.coolingArea * HTC)

    def getCurrent(self, voltage = 1):
        return voltage / self.R

    def getVoltage(self, current = 1000):
        return current * self.R


# Flat part

szyna = busbar(100,10,1000)

print(szyna)
print('Straty mocy dla 2000A to {}[W]'.format(szyna.powerLosses(2000)))
print('temperatura dla 2000A i htc=3.75 w 20degC to {}[degC]'\
    .format(szyna.temperature(szyna.powerLosses(2000),3.75,20)))

innaszyna = busbar(60,10,1000)

print(innaszyna)
print('i=2000[A]  u= {}[V]'.format(innaszyna.getVoltage(2000)))
