class WhoPy:
    '''This is a WhoPy class'''
    listOfWhoPy =[] #Here we weill memorize all of us!

    def __init__(self, myName):
        '''This is the initialization function'''

        WhoPy.listOfWhoPy.append(self)
        self.name = myName
        print('badummm... {} was just created!'.format(self.name))

    def sayHello(self):
        print('Hi! My name is {} and I\'m a python code!'.format(self.name))


# And here is flat code
# Lets create list of names
print('Let\'s create someone!')

names = ['Adam', 'Ewa', 'Zdzich', 'Julia']

# Let's create a WhoPy objects for each name!

for currentName in names:
    aNewWhoPyObject = WhoPy(currentName)

# And now let's ask everybody who they are?
print('And now let\'s ask everybody who they are?')
for who in WhoPy.listOfWhoPy:
    print('Who are you?')
    who.sayHello()
    print('\n')
