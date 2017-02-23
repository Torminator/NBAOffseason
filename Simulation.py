from Franchise import Franchise
from Player import Player
import csv

def noDoubleOffer(freeAgents):
    for p in freeAgents:
        if p.getLengthOffers() > 1:
            return False
    return True

if __name__ == '__main__':

    # List for the franchises and a list for the free agents this offseason
    franchises = []
    freeAgents = []

    # Read the franchise from a csv file and add the franchise to the list
    file = open("franchise.csv")
    reader = csv.reader(file)
    for row in reader:
        franchises.append(Franchise(row[0], row[1]))
    file.close()

    # Read the players csv file and add the player either to the free agents list
    # or it adds the player to a team
    file = open("players.csv")
    reader = csv.reader(file)
    for row in reader:
        tmpplayer = Player(row[0], int(row[1]), int(row[2]), float(row[3]), float(row[4]))
        if int(row[5]) == 0:
            freeAgents.append(tmpplayer)
        else:
            for f in franchises:
                if f.getID() == row[5]:
                    f.addPlayer(tmpplayer)
                    continue
    file.close()

    # Find the best five players for every team
    # if two teams are interested in one player increases his wage
    loopCount = 0
    while True:
        for f in franchises:
            team = f.evaluateBestTeam(freeAgents)
        if noDoubleOffer(freeAgents):
            break
        else:
            for p in freeAgents:
                if p.getLengthOffers() > 1:
                    if p.incWage():
                        freeAgents.remove(p)
                if p.getLengthOffers() < 1:
                    p.decWage()
                p.resetOffers()
        loopCount = loopCount + 1
        if loopCount > 1000:
            print("Error: No convergence")
            exit()

    # Add every player to his new team
    for p in freeAgents:
        if p.getLengthOffers() == 1:
            p.getSingleOffer().getFranchise().addPlayer(p)

    file = open("result.csv", "w")
    for f in franchises:
        string = f.getName()
        for p in f.getPlayers():
            string += ";" + p.getName() + ";" + str(p.getWage()).replace(".", ",")
        string += "\n"
        file.write(string)
