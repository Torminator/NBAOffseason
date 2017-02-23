class Player:

    __wageInc = 0.5
    __wageDec = 0.25
    __minWage = 1
    __maxWage = 26.5

    def __init__(self, name, offr, defr, wage, pos):
        # his first and lastname = name
        self.__name = name
        # his offensive rating = offr
        self.__offr = offr
        # his defensive rating = defr
        self.__defr = defr
        # his wage = wage
        self.__wage = wage
        # his position (1=PG, 2=SG, 3=SF, 4=PF, 5=C)
        self.__pos = pos
        # to count how many teams are interested
        self.__offers = []

    def getName(self):
        return self.__name

    def getPos(self):
        return self.__pos

    def getOffRating(self):
        return self.__offr

    def getDefRating(self):
        return self.__defr

    def getWage(self):
        return self.__wage

    def addOffer(self, offer):
        self.__offers.append(offer)

    def getSingleOffer(self):
        return self.__offers[0]

    def getLengthOffers(self):
        return len(self.__offers)

    def resetOffers(self):
        self.__offers = []

    def incWage(self):
        self.__wage = min(self.__wage + Player.__wageInc, Player.__maxWage)
        if(self.__wage == Player.__maxWage):
            max = 0
            for offer in self.__offers:
                tmvalue = offer.getFranchise().getTeamValue()
                if tmvalue > max:
                    max = tmvalue
                    bestTeam = offer.getFranchise()
            bestTeam.addPlayer(self)
            return True
        else:
            return False


    def decWage(self):
        self.__wage = max(self.__wage - Player.__wageDec, Player.__minWage)

    def __str__(self):
        # string function returns only the player's name
        return self.__name + " " + str(self.__wage)