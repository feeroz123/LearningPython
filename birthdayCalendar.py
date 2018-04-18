# When you run your program it should ask the user to enter a name, and return the birthday of that person back to them

calendar = {"Feeroz":"15/02/1986", "Hina":"10/11/1987", "Huma":"12/08/1991", "Nisha":"13/06/1984"}

print("We have birthday dates of Feeroz, Hina, Huma and Nisha")
uname = input("Whose birthday do you want? Enter name: ")

print(calendar[uname])