import math
from Offer import Offer

class Franchise:
    # Salary Cap for every NBA Franchise
    __cap = 65.0

    def __init__(self, id, name):
        # ID for the franchise
        self.__id = id
        # name of the franchise
        self.___franName = name
        # empty list of players assigned to the franchise
        self.__players = []

    def addPlayer(self, player):
        # add a player to the array players
        self.__players.append(player)

    def getID(self):
        return self.__id

    def getName(self):
        return self.___franName

    def getPlayers(self):
        return self.__players

    def getFreePosition(self):
        engPos = []
        for p in self.__players:
            engPos.append(p.getPos())
        avaPos = []
        for pos in [1,2,3,4,5]:
            if pos not in engPos:
                avaPos.append(pos)
        return avaPos


    def __str__(self):
        # returns a string to represent a franchise object
        # first the name of the franchise
        # then the names of their players
        output = self.___franName + "\n"
        for player in self.__players:
            output += str(player) + ", "
        return output

    def getTeamValue(self):
        numplayers = len(self.__players)
        sumoff = 0
        sumdef = 0
        for p in self.__players:
            sumoff = sumoff + p.getOffRating()*p.getOffRating()
            sumdef = sumdef + p.getDefRating()*p.getDefRating()
        meanoff = math.sqrt((1/numplayers)*sumoff)
        meandef = math.sqrt((1/numplayers)*sumdef)
        return math.sqrt(meanoff*meandef)

    def evaluateBestTeam(self, freeAgents):
        workingTeam  = []
        # add our players to the array
        for p in self.__players:
            tmp = []
            tmp.append(p)
            workingTeam.append(tmp)

        # add all free agents who play a position which is not fulfilled right now
        for pos in self.getFreePosition():
            tmp = []
            for p in freeAgents:
                if p.getPos() == pos:
                    tmp.append(p)
            workingTeam.append(tmp)
        maxvalue = 0.0
        team = []
        for p1 in workingTeam[0]:
            for p2 in workingTeam[1]:
                for p3 in workingTeam[2]:
                    for p4 in workingTeam[3]:
                        for p5 in workingTeam[4]:
                            if p1.getWage()+p2.getWage()+p3.getWage()+p4.getWage()+p5.getWage() <= Franchise.__cap:
                                offr = math.sqrt( 1/5*(p1.getOffRating()*p1.getOffRating() +
                                             p2.getOffRating()*p2.getOffRating() +
                                             p3.getOffRating()*p3.getOffRating() +
                                             p4.getOffRating()*p4.getOffRating() +
                                             p5.getOffRating()*p5.getOffRating())
                                                  )
                                defr = math.sqrt( 1/5*(p1.getDefRating() * p1.getDefRating() +
                                                 p2.getDefRating() * p2.getDefRating() +
                                                 p3.getDefRating() * p3.getDefRating() +
                                                 p4.getDefRating() * p4.getDefRating() +
                                                 p5.getDefRating() * p5.getDefRating())
                                                  )
                                teamvalue = math.sqrt(defr*offr)
                                if teamvalue > maxvalue:
                                    maxvalue = teamvalue
                                    team = [p1,p2,p3,p4,p5]
        offer = Offer(self)
        for p in team:
            if p not in self.__players:
                p.addOffer(offer)
        return team