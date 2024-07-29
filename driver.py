class Driver:
    def __init__(self, driverNo, team):
        self.driverNo = driverNo
        self.team = team
        self.total_points = 0;
    
    def add_Points(self, points):
        self.total_points += points
        