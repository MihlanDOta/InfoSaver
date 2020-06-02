#InfoSaver Python Libary
#2020 MihlanDOta coopyright
#Made by MihlanDOta

import os

global InfosaverAppname
InfosaverAppname = ''

global InfoSaverdebugMessage
InfoSaverdebugMessage = True

if os.path.exists("infosaver"):
    os.chdir("infosaver")
else:
    print("Infosaver folder did not found! Creating...")
    os.mkdir("infosaver")
    os.chdir("infosaver")

class saver():
    def setAppName(AppName):
        global InfosaverAppname
        if InfosaverAppname == '':
            InfosaverAppname = AppName
        else:
            print("Name has already been set!")


    def saveInfo(base, name, value):
        if InfosaverAppname == '':
            print("App name not set! Failed")
            return 'Failed'

        if os.path.exists(InfosaverAppname + "AND" + base + "AND" + name + ".infdata"):
            print("Key " + "'" + name + "'" + " is already exists! Failed")
            return 'Failed'


        try:
            svdata = open(InfosaverAppname + "AND" + base + "AND" + name + '.infdata', 'w')
            svdata.write(value)
            svdata.close()
            return 'Success'
        except:
            return 'Failed'



    def readInfo(base, name):
        if InfosaverAppname == '':
            print("App name not set! Failed")
            return 'Failed'

        if not os.path.exists(InfosaverAppname + "AND" + base + "AND" + name + ".infdata"):
            print("Key " + "'" + name + "'" + " did not found! Failed")
            return 'Failed'

        try:
            svdata = open(InfosaverAppname + "AND" + base + "AND" + name + '.infdata', 'r')
            for data in svdata:
                retdata = data
            svdata.close()
            return retdata
        except:
            return 'Failed'

    def editInfo(base, name, newValue):
        if InfosaverAppname == '':
            print("App name not set! Failed")
            return 'Failed'

        if not os.path.exists(InfosaverAppname + "AND" + base + "AND" + name + ".infdata"):
            print("Key " + "'" + name + "'" + " did not found! Failed")
            return 'Failed'

        try:
            svdata = open(InfosaverAppname + "AND" + base + "AND" + name + '.infdata', 'w')
            svdata.write(newValue)
            svdata.close()
            return 'Success'
        except:
            return 'Failed'

    def clearInfo(base, name):
        if InfosaverAppname == '':
            print("App name not set! Failed")
            return 'Failed'

        if not os.path.exists(InfosaverAppname + "AND" + base + "AND" + name + ".infdata"):
            print("Key " + "'" + name + "'" + " did not found! Failed")
            return 'Failed'

        try:
            svdata = open(InfosaverAppname + "AND" + base + "AND" + name + '.infdata', 'w')
            svdata.write("")
            svdata.close()
            return 'Success'
        except:
            return 'Failed'

    def deleteInfo(base, name):
        if not os.path.exists(InfosaverAppname + "AND" + base + "AND" + name + ".infdata"):
            print("Key " + "'" + name + "'" + " did not found! Failed")
            return 'Failed'

        try:
            os.remove(InfosaverAppname + "AND" + base + "AND" + name + '.infdata')
            return 'Success'
        except:
            return 'Failed'
