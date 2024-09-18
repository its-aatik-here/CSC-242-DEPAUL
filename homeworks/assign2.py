


#Exercise 1

class ScoreCard():
    def __init__(self,score =0 ):
        self.score = score
    def addPoints (self,score =1):
        self.score += score
    def removePoints (self,score =1):
        self.score -= score
    def get_total (self):
        return self.score
    def clearPoints (self):
        self.score = 0
    def __str__(self):
        return f"Scorecard total: {self.score}"
    

#Exercise 2
class VideoGame():
    def __init__(self):
        self.score = ScoreCard()
    def destroy_enemy(self):
        self.score.addPoints(10)
    def take_hit(self):
        self.score.removePoints(5)
    def debuff (self):
        score = self.score.get_total()
        half_score = score / 2
        self.score.removePoints(half_score)
    def point_thief (self):
        score = self.score.get_total()
        self.score.removePoints(score-10)
    def __str__(self):
        return f"player 1 has: {self.score.get_total():.0f} points"
    

#Exercise 3
class citizen ():
    def __init__ (self,name,date_of_birth,passport_number,country):
        self.name = name
        self.date_of_birth = date_of_birth
        self.passport_number = passport_number
        self.country = country
    def get_name(self):
        return self.name
    def get_date_of_birth(self):
        return self.date_of_birth
    def get_passport_number(self):
        return self.passport_number
    def get_country(self):
        return self.country
    def national_anthem(self):
        print ("")


cit = citizen('Brandon H. Meng','2/10/1995','8675309','Germany')
cit.get_name()
cit.get_date_of_birth()
cit.get_passport_number()
cit.get_country()