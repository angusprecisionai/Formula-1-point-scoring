BAH = [1, 11, 55, 16, 63, 4, 44, 81, 14, 18, 24, 20, 3, 22, 23, 27, 31, 10, 77, 2]
SDA = [1, 11, 16, 81, 14, 63, 38, 4, 44, 27, 23, 20, 31, 2, 22, 3, 77, 24, 18, 10]
AUS = [55, 16, 4, 81, 11, 18, 22, 14, 27, 20, 23, 3, 10, 77, 24, 31, 63, 44, 1, 2]
JAP = [1, 11, 55,  16, 4, 14, 63, 81, 44, 22, 27, 18, 20,77, 31, 10, 2, 24, 3, 23]
CHN = [1, 4, 11, 16, 55, 63, 14, 81, 44, 27, 31, 23, 10, 24, 18, 20, 2, 3, 22, 77]
MIA = [4, 1, 16, 11, 55, 44, 22, 63, 14, 31, 27, 10, 81, 24, 3, 77, 18, 23, 20, 2]
EMR = [1, 4, 16, 81, 55, 44, 63, 11, 18, 22, 27, 20, 3, 31, 24, 10, 2, 77, 14, 23]
MON = [16, 81, 55, 4, 63, 1, 44, 22, 23, 10, 14, 3, 77, 18, 2, 24, 31, 11, 27, 20]
CAN = [1, 4, 63, 44, 81, 14, 18, 3, 10, 31, 27, 20, 77, 22, 24, 55, 23, 11, 16, 2]
SPN = [1, 4, 44, 63, 16, 55, 81, 11, 10, 31, 27, 14, 24, 18, 3, 77, 20, 23, 22, 2]
AUT = [63, 81, 55, 44, 1, 27, 11, 20, 3, 10, 16, 31, 18, 22, 23, 77, 24, 14, 2, 4]
GBR = [44, 1, 4, 81, 55, 27, 18, 14, 23, 22, 2, 20, 3, 16, 77, 31, 11, 24, 63, 10]
HUN = [81, 4, 44, 16, 1, 55, 11, 63, 22, 18, 14, 3, 27, 23, 20, 77, 2, 31, 24, 10]
BEL = [44, 81, 16, 1, 4, 55, 11, 14, 31, 3, 18, 23, 10, 20, 77, 22, 2, 27, 24, 63]
CHN_sprint = [1, 44, 11,16,55,4,81,63,24,20,3,77,31,18,10,22,23,2,27,14]
MIA_sprint = [1, 16, 11,3,55,81,27,22,10,2,24,63,23,77,31,44,14,20,18,4]
AUT_sprint = [1, 81, 4,63,55,44,16,11,20,18,31,10,22,3,14,2,23,77,27,24]

class Race:
    def __init__(self, name, gp_results, fastest_lap_winner, sprint_results):
        self.name = name
        self.gp_results = gp_results
        self.fastest_lap_winner = fastest_lap_winner
        self.sprint_results = sprint_results;


all_races = [Race("Bahrain", BAH, 1, None),
             Race("Saudi Arabia", SDA, 16, None),
             Race("Australia", AUS, 16, None),
             Race("Japan", JAP, 1, None),
             Race("China", CHN, 14, CHN_sprint),
             Race("Miami", MIA, 81, MIA_sprint),
             Race("Emilia-Romagna", EMR, 63, None),
             Race("Monaco", MON, 44, None),
             Race("Canada", CAN, 44, None),
             Race("Spain", SPN, 4, None),
             Race("Austria", AUT, 14, AUT_sprint),
             Race("Great Britain", GBR, 55, None),
             Race("Hungary", HUN, 63, None),
             Race("Belgium", BEL, 11, None)]
    
        