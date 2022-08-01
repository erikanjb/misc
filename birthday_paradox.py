import datetime, random

def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for l in range(numberOfBirthdays):
        #The year is unimportant for our simulation, as long as all birthdays
        #have the same year.
        startOfYear = datetime.date(2001, 1, 1)

        #Get a random day into the year
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    """Return the date object of a birthday that occurs more than once
    in the birthdays list"""
    if len(birthdays) == len(set(birthdays)):
        #all birthdays are unique, so return none
        return None

    #compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
             #Return the matching birthday.
                return birthdayA

#Display the intro:
print("""
The birthday paradox shows us that in a group of N people, the odds that
two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random simulations)
to explore this concept.

""")

#setup a tuple of month names in order:
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
           "Oct", "Nov", "Dec")
#keep asking until the user enters a valid amount. 
while  True:
     print("How many birthdays shall i generate? (Max 100)")
     response = input("> ")
     if response.isdecimal() and (0 < int(response) <= 100):
         numBDays = int(response)
         # User has entered a valid amount.
         break
print()

#Generate and display the birthdays:
print("Here are", numBDays, "birthdays:")
birthdays = getBirthdays(numBDays)
for l, birthday in enumerate(birthdays):
    if l != 0:
        #display a comma for each birthday after the first birthday.
        print(",", end="")
        monthName = MONTHS[birthday.month - 1]
        dateText = "{} {}".format(monthName, birthday.day)
        print(dateText, end = "")
print()
print()

#Determine if there are two birthdays that match.
match = getMatch(birthdays)

#Display the results:
print("In this simulation, ", end = "")
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = "{} {}".format(monthName, match.day)
    print("multiple people have a birthday on", dateText)

else:
    print("there are no matching birthdays.")
print()

#Run through 100,000 simulation:
print("Generating", numBDays, "random birthdays 100,000 times..")
input("Press Enter to begin...")

print("Let\"s run another 100,000 simulations.")
#How many simulations had matching birthdays in them
simMatch = 0
for l in range(100_000):
    #Report on the progress every 10,000 simulations:
    if 1 % 10_000 == 0:
        print(1, "simulation run..")
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print("100,000 simulations run.")

#Display simulation results:
probability = round(simMatch/ 100_000*100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')
        

 
        
        
        
