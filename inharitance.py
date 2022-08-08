#sengil inheritiance
#THE COMMUNITATION IN B/W parant and chaild
#multiple inheritince
#the commmunitation in b/w one parante nd more than one children
#multi level
#the communitation in b/w more than one parent and more than one childern
#hybride
#the combinition of single and multiple inheritiance
#hyrarchial
#it is tree level like structure it contains more than one level parent and child
class Person :
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):

            print(self.firstname,self.lastname)

x = Person("Cse","pfsd")
x.printname()
