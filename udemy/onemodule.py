import twomodule
import LearningPython.udemy.mypackage.threemodule

print('I am one module')

twomodule.two_method()
LearningPython.udemy.mypackage.threemodule.three_method()

if __name__ == "__main__":
    print('Running the one module directly')
else:
    print('Imported the one module')