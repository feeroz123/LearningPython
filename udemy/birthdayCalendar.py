# When you run your program it should ask the user to enter a name, and return the birthday of that person back to them

calendar = {"Feeroz":"18/09/1981", "Hina":"12/01/1987", "Huma":"02/10/1997", "Nisha":"19/10/1980"}

print("We have birthday dates of Feeroz, Hina, Huma and Nisha")
uname = input("Whose birthday do you want? Enter name: ")

print(calendar[uname])