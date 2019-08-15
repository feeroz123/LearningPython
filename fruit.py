class Fruit:

    def __init__(self):
        print("A new fruit has been created.")

    def nutrition(self):
        print("Nutrition of the fruit is Unknown.")

    def fruit_shape(self):
        print("The shape of fruit is Unknown.")


class Mango(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print("A new Mango has been created.")

    def nutrition(self):
        print("Nutrition of the mango is good.")

    def color(self):
        print("The color of mango is yellow.")


apple = Fruit()
mango1 = Mango()

apple.nutrition()
apple.fruit_shape()

mango1.nutrition()
mango1.color()
mango1.fruit_shape()
