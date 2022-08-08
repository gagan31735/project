# SUPER FUNCTION
# SUPER IS A BUILT IN FUNCTION
# SUPER FUNCTION IMPLEMENTS CODE REUSEBELAITY
# THE METHODS DECLARED IN THE PARENT WILL BE AUTOMATICALLY INHERATIED BY THE CHILD CLASS


class Parent:
    def __init__(self, txt):
        self.message = txt

    def printmessage(self):
        print(self.message)


class Child(Parent):
    def __init__(self, txt):
        super().__init__(txt)


x = Child("hello,bro")
x.printmessage()
