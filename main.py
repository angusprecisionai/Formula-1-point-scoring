from drivers import *
from point_system import *
from race_results import all_races
from team_rank import *

for race in all_races:
    fastest_lap_driver = driverFromDriverNumber(race.fastest_lap_winner)
    fastest_lap_driver_position = race.gp_results.index(race.fastest_lap_winner)
    
    if fastest_lap_driver_position < 10:
        fastest_lap_driver.add_Points(1)
    
    if race.sprint_results != None:
        for pos in range(0, len(race.sprint_results) -1):
            driver = driverFromDriverNumber(race.sprint_results[pos])
            points = pointsForPosition(pos, CURRENT_SPRINT)
            driver.add_Points(points)
            
    for pos in range(0, len(race.gp_results) -1):
        driver = driverFromDriverNumber(race.gp_results[pos])
        points = pointsForPosition(pos, CURRENT_GP)
        driver.add_Points(points)
        
        
sorted_drivers = sorted(drivers, key=lambda driver: driver.total_points, reverse=True)

headers = ["Driver", "Points", "Team"]
print(f"{headers[0]:<10} {headers[1]:<5} {headers[2]:<15}")
for driver in sorted_drivers:
    print(f"{nameFromDriverNo(driver.driverNo):<10} {str(driver.total_points):<5} {driver.team:<15}")
    
print()

team_standings = []

for team in Team:
    team_drivers = filter(lambda d: d.team == team, sorted_drivers)
    team_points = 0
    for driver in team_drivers:
        team_points += driver.total_points
    team_standings.append(TeamRank(team, team_points))
    
sorted_teams = sorted(team_standings, key=lambda team: team.points, reverse=True)

for team in sorted_teams:
    print(str(team.team) + " " + str(team.points))
    
