from datetime import date


""" Asks user's data """
name = input("Hello!  What is your name?  ")

while True:
    year_of_birth = input("What year were you born?  ")
    try:
        year_of_birth = int(year_of_birth)
    except ValueError:
        continue
    else:
        break

""" Milestones to compute """
milestones = [5, 10, 16, 18, 21, 22, 24, 25, 50, 75, 100]

""" Renders results """
if year_of_birth + 100 < date.today().year:
    print("WOW, {}! You are roughly {} years old, Old Timer!".format(name, date.today().year - year_of_birth))
elif year_of_birth > date.today().year:
    print("Congratulations!  {} will be born soon presumably in the year of {}!".format(name, year_of_birth))
elif year_of_birth < date.today().year:
    for milestone in milestones:
        if year_of_birth + milestone > date.today().year:
            print("{}, you will turn {} in {}".format(name, milestone, str(year_of_birth + milestone)))
