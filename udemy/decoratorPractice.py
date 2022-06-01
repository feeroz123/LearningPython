def decorator_func(input_func):
    def decorator():
        print('This is a decorator function')
        input_func()
        print('The function has been decorated')
    return decorator


@decorator_func    # To pass the 'welcome' function as an argument to the 'decorator_func' function
def welcome():
    print('\tHello friend')


welcome()
