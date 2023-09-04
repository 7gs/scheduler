import random

def createWeek(managers):

    global opponents
    
    week = []
    templist = managers.copy()

    for x in range (1, int(len(managers) / 2) + 1):
        
        unmatched = True

        team1 = random.choice(templist)
        templist.remove(team1)
        
        while unmatched:

            team2 = random.choice(templist)

            if team2 not in opponents[team1]:

                opponents[team1].append(team2)
                opponents[team2].append(team1)
                templist.remove(team2)
                week.append([team1, team2])
                unmatched = False

            else:
                
                # Break the loop if its a dead-end 
                check = all(item in opponents[team1] for item in templist)
            
                if check:

                    min = 100

                    for team in opponents:

                        if len(opponents[team]) < min:
                            min = len(opponents[team])

                    for team in opponents:
                        if len(opponents[team]) > min:
                            opponents[team] = opponents[team][:-1]        

                    return False, []

    return True, week


# Initialize dictionary of each team's opponents, include their rival to prevent rival being selected for non-rivalry weeks
opponents = {
    "Tom": ["Eric"],
    "Eric": ["Tom"],
    "Andy": ["Doug"],
    "Doug": ["Andy"],
    "Charlie": ["Dave"],
    "Dave": ["Charlie"],
    "Matt": ["Mike"],
    "Mike": ["Matt"],
    "Craig": ["Tommy"],
    "Tommy": ["Craig"],
    "Julien": ["Brad"],
    "Brad": ["Julien"]
}

# Pull a list of managers from the dictionary keys
managers = []
for key in opponents.keys():
    managers.append(key)

weeks = len(managers) - 2
games = []
schedule = []

count = 0
schedule = []

# Loop to call the create week function the appropriate amount of times
while count < weeks:

    new_week = createWeek(managers)

    if new_week[0] is True:
        print("Week " + str((count + 1)))
        print(new_week[1])
        count += 1