CURRENT_GP = 	 [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
NEW_GP =    	 []
CURRENT_SPRINT = [8, 7, 6, 5, 4, 3, 2, 1]
NEW_SPRINT = 	 []

def pointsForPosition(position, race):
    if position > len(race) - 1:
        return 0
    return race[position]
