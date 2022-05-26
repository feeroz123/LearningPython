class Car:
    """
    Car models a car with tires and engine
    """

    def __init__(self, engine, tires):
        """
        When a new instance of this Class is created, this '__init__(self)' method (Dunder method) gets called.
        """
        self.engine = engine
        self.tires = tires

    def description(self):
        print(f"A car with an {self.engine} engine,and {self.tires} tires")

