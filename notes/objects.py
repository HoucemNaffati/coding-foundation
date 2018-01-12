class Human:

    def __init__(self, name):
        self.name = name

    def grunt(self):
        print("Hurrrrrrrr")

    def say_name(self):
        print(self.name)

    def fly(self):
        print('Can\'t fly :(')


class Male(Human):

    def gender(self):
        print('Male')


class Female(Human):

    def gender(self):
        print('Female')


class Superman(Male):

    def fly(self):
        print('Woooosh!')


gil = Superman('Gil')
gil.fly()
