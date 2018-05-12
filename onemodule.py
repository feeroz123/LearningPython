import twomodule
import mypackage.threemodule

print('I am one module')

twomodule.two_method()
mypackage.threemodule.three_method()

if __name__ == "__main__":
    print('Running the one module directly')
else:
    print('Imported the one module')