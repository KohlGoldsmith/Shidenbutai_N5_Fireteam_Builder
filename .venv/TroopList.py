class Troop:
    def __init__(self, name, points, weapon, teamName, teamSizeOne, teamSizeTwo,teamSizeThree, equipment, specialist, core):
        self.name = name
        self.points = points
        self.weapon = weapon
        self.teamName =teamName
        self.teamSizeOne = teamSizeOne
        self.teamSizeTwo = teamSizeTwo
        self.teamSizeThree = teamSizeThree
        self.equipment = equipment
        self.specialist = specialist
        self.core = core
    def __repr__(self):
         return (f"Troop(name={teamTroopList[1]}, points={self.points}, weapon={self.weapon}, "
             f"teamName={self.teamName}, teamSize={self.teamSize}, equipment={self.equipment}, specialiist={self.specialist}, core={self.core})")

fireteamLists= {
    "Duo 1":[],
    "Duo 2":[],
    "Duo 3":[],
    "Harris":[],
    "Core":[]
}

teamTroopList =[Troop("Senku", 9, "Combi Rifle","Senku", 3, 5, None, "", "", True),
              Troop("Senku", 17, "HMG", "Senku", 3, 5, 5, "", "", True),
              Troop("Senku", 11, "Shock MR","Senku", 3, 5, None, "", "", True),
              Troop("Senku", 11, "Combi Rifle","Senku", 3, 5, None, "Commlink +1", "Specialist Op.", True),
              Troop("Senku", 11, "Combi Rifle, Flash Pulse","Senku", 3, 5, None, "", "Forward Observer", True),
              Troop("Senku", 11, "Combi Rifle","Senku", 3, 5, None, "Medkit", "Paramedic", True),
              Troop("Senku", 11, "Combi Rifle","Senku", 3, 5, None, "", "Lieutenant", True),

              Troop("Jizamurai", 21, "Light Shotgun, Pistol, DA CC (PS=5)","Senku", 3, 5, None, "", "", False),
              Troop("Jizamurai", 21, "Light Shotgun, Pistol, DA CC (PS=5)","Senku", 3, 5, None, "", "", False),
              Troop("Jizamurai", 24, "Light Shotgun, Thunderbolt, Pistol, E/M CC (PS=5)","Senku", 3, 5, None, "", "", False),
              Troop("Jizamurai", 24, "Light Shotgun, E/Mitter, Pistol, DA CC (PS=5)","Senku", 3, 5, None, "", "", False),
              Troop("Jizamurai", 22, "SMG, Pistol, DA CC (PS=5)","Senku", 3, 5, None, "", "", False),


             Troop("Hatamoto", 34, "Plasma Carbine, Heavy Pistol, MF & E/M CC (PS=4)","Senku", 3, 5, None, "","NCO", False),
             Troop("Hatamoto", 40, "Red Fury, Heavy Pistol, MF & E/M CC (PS=4)","Senku", 3, 5, None, "","NCO", False),
             Troop("Hatamoto", 41, "Spitfire, Heavy Pistol, MF & E/M CC (PS=4)","Senku", 3, 5, None, "","NCO", False),
             Troop("Hatamoto", 36, "Plasma Carbine, Heavy Pistol, MF & E/M CC (PS=4)","Senku", 3, 5, None, "","Lieutenant +1 Order", False),
             Troop("Hatamoto", 38, "Red Fury, Heavy Pistol, MF & E/M CC (PS=4)","Senku", 3, 5, None, "","Lieutenant +1 Order",  False),
             Troop("Hatamoto", 39, "Spitfire, Heavy Pistol, MF & E/M CC (PS=4)","Senku", 3, 5, None, "","Lieutenant +1 Order", False),

             Troop("Taguraida, JSA TAG Support Pilot", 12, "Light Shotgun, Pistol, DA CC (PS=7)", "Senku", 3, 5, None, "Gizmokit", "Specialist Op.", False),



                         Troop("Jizamurai", 21, "Light Shotgun, Pistol, DA CC (PS=5)","Bushi-tai", 2, 3, 5, "", "", True),
                         Troop("Jizamurai", 21, "Light Shotgun, Pistol, DA CC (PS=5)","Bushi-tai", 2, 3, 5, "", "", True),
                         Troop("Jizamurai", 24, "Light Shotgun, Thunderbolt, Pistol, E/M CC (PS=5)","Bushi-tai", 2, 3, 5, "", "", True),
                         Troop("Jizamurai", 24, "Light Shotgun, E/Mitter, Pistol, DA CC (PS=5)","Bushi-tai", 2, 5, 5, "", "", True),
                         Troop("Jizamurai", 22, "SMG, Pistol, DA CC (PS=5)","Bushi-tai", 2, 3, 5, "", "", True),

                         Troop("Hatamoto", 34, "Plasma Carbine, Heavy Pistol, MF & E/M CC (PS=4)","Bushi-tai", 2, 3, 5, "","NCO", True),
                         Troop("Hatamoto", 40, "Red Fury, Heavy Pistol, MF & E/M CC (PS=4)","Bushi-tai", 2, 3, 5, "","NCO", True),
                         Troop("Hatamoto", 41, "Spitfire, Heavy Pistol, MF & E/M CC (PS=4)","Bushi-tai", 2, 3, 5, "","NCO", True),
                         Troop("Hatamoto", 36, "Plasma Carbine, Heavy Pistol, MF & E/M CC (PS=4)","Bushi-tai", 2, 3, 5, "","Lieutenant +1 Order", True),
                         Troop("Hatamoto", 38, "Red Fury, Heavy Pistol, MF & E/M CC (PS=4)","Bushi-tai", 2, 3, 5, "","Lieutenant +1 Order",  True),
                         Troop("Hatamoto", 39, "Spitfire, Heavy Pistol, MF & E/M CC (PS=4)","Bushi-tai", 2, 3, 5, "","Lieutenant +1 Order", True),

                         Troop("Shizoku FTO", 43, "AP HMG, Chain Rifle, Pistol, AP & DA CC (PS=4)","Bushi-tai", 2, 3, 5, "","", True),
                         Troop("Shizoku FTO", 33, "Heavy Rocket Launcher (+1B), Assault Pistol, AP & DA CC (PS=4)","Bushi-tai", 2, 3, 5,"","", True),
                         Troop("Shizoku", 38, "Heavy Rocket Launcher (+1B), Assault Pistol, AP & DA CC (PS=4)","Bushi-tai", 2, 3, 5, "","Strategic Deployment", False),

                         Troop("Yamabushi FTO", 15, "Chain Rifle, Panzerfaust, Heavy Pistol, DA CC (PS=4)","Bushi-tai", 2, 3, 5,"", "", False),
                         Troop("Yamabushi FTO", 16, "Chain Rifle, Tactical Bow, Heavy Pistol, DA CC (PS=4)","Bushi-tai", 2, 3, 5,"Medkit", "Paramedic", False),

                         Troop("Tanuki", 18, "Boarding Shotgun, Chain-colt, Flash Pulse, Pistol","Sayo", 2, 3, None,"", "CoC", True),
                         Troop("Tanuki", 19, "MULTI, D-Charges, Pistol","Sayo", 2, 3, None,"Gizmokit, Deactivator", "Specialist Op.", True),
                         Troop("Tanuki", 20, "SMG, Pitcher, Discoballer, Pistol","Sayo", 2, 3, None,"Hacking Device", "Hacker", True),
                         Troop("Tanuki", 20, "Boarding Shotgun, Contender, Pistol","Sayo", 2, 3, None,"Medkit", "Paaramedic", True),
                         Troop("Tanuki", 29, "HMG, Pistol","Sayo", 2, 3, None,"MSV L2", "", True),
                         Troop("Tanuki", 27, "MULTI Sniper, Pistol","Sayo", 2, 3, None,"MSV L2", "", True),
                         Troop("Tanuki", 29, "HMG, Pistol","Sayo", 2, 3, None,"MSV L2", "Lieutenant", True),

                         Troop("Jizamurai", 21, "Light Shotgun, Pistol, DA CC (PS=5)","Sayo", 2, 3, None, "", "", True),
                         Troop("Jizamurai", 21, "Light Shotgun, Pistol, DA CC (PS=5)","Sayo", 2, 3, None, "", "", True),
                         Troop("Jizamurai", 24, "Light Shotgun, Thunderbolt, Pistol, E/M CC (PS=5)","Sayo", 2, 3, None, "", "", True),
                         Troop("Jizamurai", 24, "Light Shotgun, E/Mitter, Pistol, DA CC (PS=5)","Sayo", 2, 3, None, "", "", True),
                         Troop("Jizamurai", 22, "SMG, Pistol, DA CC (PS=5)","Sayo", 2, 3, None, "", "", True),

                         Troop("Rui-shi", 23, "Spitfire, Para CC (-3)","Sayo", 2, 3, None, "MSV L2", "", True),
                         Troop("Rui-shi", 21, "Red Fury, Mine Deployer (Shock), Para CC (-3)","Sayo", 2, 3, None, "MSV L1", "", True),

                         Troop("Shizoku", 38, "Heavy Rocket Launcher (+1B), Assault Pistol, AP & DA CC (PS=4)","Sayo", 2, 5, None, "","Strategic Deployment", False),

                         Troop("Aida Swanson FTO", 21, "SMG, Viral Mine, Viral Pistol, Shock CC (PS=7)","Sayo", 2, 5, None, "","Minelayer", False),
                           ]
