
while True:
    try:
        num = int(input("Enter a number: "))
    except TypeError:
        print("Type mismatch. Try again.")
        continue
    except:
        print("Error occured. Try again.")
        continue
    else:
        print(f"Square of {num} is {num*num}")
        break
    finally:
        print("All done")

print ("Task successful")