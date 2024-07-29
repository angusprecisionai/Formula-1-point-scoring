from driver import Driver
from team import Team


drivers = [Driver(1, Team.RBR),
           Driver(11, Team.RBR),
           Driver(55, Team.FER),
           Driver(16, Team.FER),
           Driver(63, Team.MER),
           Driver(44, Team.MER),
           Driver(81, Team.MCL),
           Driver(4, Team.MCL),
           Driver(14, Team.ASM),
           Driver(18, Team.ASM),
           Driver(3, Team.RB),
           Driver(22, Team.RB),
           Driver(20, Team.HAS),
           Driver(27, Team.HAS),
           Driver(31, Team.ALP),
           Driver(10, Team.ALP),
           Driver(2, Team.WIL),
           Driver(23, Team.WIL),
           Driver(77, Team.SAU),
           Driver(24, Team.SAU),
           Driver(38, Team.FER),]

drivers_name = {
    1: "Verstappen",
    11: "Perez",
    55: "Sainz",
    16: "Leclerc",
    63: "Russell",
    44: "Hamilton",
    81: "Piastri",
    4 : "Norris",
    14: "Alonso",
    18: "Stroll",
    3: "Ricciardo",
    22: "Tsunoda",
    20: "Magnussen",
    27: "Hülkenberg",
    31: "Ocon",
    10: "Gasly",
    2: "Sargeant",
    23: "Albon",
    77: "Bottas",
    24: "Zhou",
    38: "Bearman"
}

def driverFromDriverNumber(driver_number):
    for driver in drivers:
        if driver.driverNo == driver_number:
            return driver
    return None

def nameFromDriverNo(driverNo):
    return drivers_name[driverNo]
