# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 2026

Copy of original random class generator file created by jaker

@author: tbaer7
"""


import random

# ALL LISTS/DICTIONARIES OF CLASS ITEMS

# List containing all Specialist Operators
specialists=['Ajax', 'Torque', 'Battery', 'Reaper', 'Spectre', 'Ruin', 'Outrider', 'Prophet', 'Firebreak', 'Zero', 'Crash', 'Nomad', 'Seraph', 'Recon']
# List containing all Primary Weapons
primaries = [['ICR-7','Rampart 17', 'KN-57', 'VAPR-XKG', 'Maddox RFB', 'SWAT RFT', 'Grav', 'Peacekeeper', 'AN-94', 'Doublecross'], ['MX9', 'GKS', 'Spitfire', 'Cordite','Saug 9MM', 'Daemon 3XB', 'Switchblade X9','VMP', 'MicroMG 9MM'], ['Auger DMR', 'ABR 223', 'Swordfish', 'S6 Stingray', 'M16' ], ['Titan','Hades', 'VKM 750', 'Tigershark'], ['Paladin HB50', 'Outlaw', 'SDM', 'Koshka', 'Vendetta', 'Locus', 'Havelina AA50']]
# List containing all Secondary Weapons
secondaries=[['RK7 Garrison', 'Strife', 'Mozu', 'Kap 45'], ['MOG 12', 'Argus', 'Rampage', 'SG12'], ['Hellion Salvo'], ['Ballistic Knife', 'Reaver C86'], ['Combat Knife']]
# Dictionary containing all Optics for each Primary Weapon
optics=    {'ICR-7': ['Reflex', 'Recon','Holographic', 'Dual Zoom', 'Threat Detector', 'NVIR'],
                'Rampart 17': ['Reflex', 'Recon','Holographic', 'Dual Zoom', 'Threat Detector'],
                'KN-57': ['Reflex', 'Recon','Holographic', 'ELO'],
                'VAPR-XKG': ['Reflex', 'Recon','ELO','NVIR'],
                'Maddox RFB': ['Reflex', 'Holographic', 'Dual Zoom', 'ELO'],
                'SWAT RFT': ['Reflex', 'Holographic', 'NVIR', 'Threat Detector'],
                'Grav': ['Reflex', 'Recon', 'NVIR'],
                'Peacekeeper': ['Reflex', 'Threat Detector', 'NVIR', 'ELO'],
                'AN-94': ['Reflex', 'Dual Zoom', 'Threat Detector', 'NVIR'],
                'Doublecross': ['Reflex', 'Holographic', 'Threat Detector'],
                'MX9': ['Reflex', 'Holographic', 'ELO', 'NVIR'],
                'GKS': ['Reflex', 'Recon', 'Dual Zoom', 'NVIR'],
                'Spitfire': ['Reflex', 'Dual Zoom', 'Holographic', 'ELO'],
                'Cordite': ['Reflex', 'Threat Detector', 'Holographic', 'ELO'],
                'Saug 9MM': ['Reflex', 'Holographic', 'Threat Detector', 'ELO'],
                'Daemon 3XB': ['Reflex', 'ELO', 'Holographic', 'Compact Scope'],
                'Switchblade X9': ['Reflex', 'ELO'],
                'VMP': ['Reflex', 'ELO', 'Holographic', 'NVIR'],
                'MicroMG 9MM': ['Reflex', 'Holographic', 'ELO'],
                'Auger DMR': ['Reflex', 'Recon', 'Holographic', 'Dual Zoom', 'Threat Detector', 'NVIR'],
                'ABR 223': ['Reflex', 'Recon', 'Holographic', 'ELO', 'NVIR'],
                'Swordfish': ['Reflex', 'Recon', 'Holographic', 'Dual Zoom', 'Threat Detector', 'NVIR'],
                'S6 Stingray': ['Reflex', 'Holographic', 'Dual Zoom', 'Threat Detector', 'NVIR'],
                'M16': ['Reflex', 'Recon', 'Holographic', 'NVIR'],
                'Titan': ['Reflex', 'Recon', 'Holographic', 'Dual Zoom', 'Threat Detector', 'NVIR'],
                'Hades': ['Reflex', 'Dual Zoom', 'Holographic', 'Threat Detector', 'ELO'],
                'VKM 750': ['Reflex', 'Recon', 'Holographic', 'Dual Zoom', 'NVIR'],
                'Tigershark': ['Reflex', 'ELO', 'Holographic', 'Threat Detector'],
                'Paladin HB50': ['Recon', 'Dual Zoom', 'Threat Detector', 'Holographic', 'Iron Sights', 'NVIR'],
                'Outlaw': ['Recon', 'Iron Sights', 'Threat Detector', 'Reflex'],
                'SDM': ['Dual Zoom', 'Holographic', 'Threat Detector', 'Iron Sights', 'NVIR'],
                'Koshka': ['Recon', 'Iron Sights', 'ELO', 'NVIR'],
                'Vendetta': ['Dual Zoom', 'Holographic', 'Iron Sights', 'NVIR'],
                'Locus': ['Recon', 'Iron Sights', 'ELO', 'Threat Detector', 'Reflex', 'NVIR'],
                'Havelina AA50': ['Holographic', 'Iron Sights', 'Dual Zoom', 'Recon', 'Threat Detector'],
                'Strife': ['Reflex'],
                'RK7 Garrison': ['Reflex', 'ELO'],
                'Mozu': ['Compact Scope'],
                'Kap 45': ['Reflex'],
                'MOG 12': ['ELO'],
                'SG12': ['Reflex'],
                'Rampage': ['Reflex'],
                'Argus': ['Reflex', 'ELO'],
                'Hellion Salvo': ['Fast Lock'],
                'Combat Knife': None,
                'Ballistic Knife': None,
                'Reaver C86': ['Compact Scope']}

    # Dictionary containing all Attachments by weapon
# Dictionary containing all Attachments for each Weapon (Primary and Secondary)
attachments={'ICR-7': ['Grip', 'FMJ', 'Quickdraw', 'Laser Sight', 'Grip II', 'Long Barrel'],
            'Rampart 17': ['High Caliber', 'High Caliber II', 'FMJ', 'FMJ 2', 'Long Barrel', 'Grip', 'Fast Mags'],
            'KN-57': ['Hybrid Mags', 'Quickdraw', 'Laser Sight', 'Grip', 'Stock', 'Extended Mags', 'Rapid Fire', 'Suppressor'],
            'VAPR-XKG': ['Suppressor', 'Long Barrel', 'Stock', 'Fast Mags', 'Rapid Fire', 'High Caliber', 'Stock II'],
            'Maddox RFB': ['Laser Sight', 'Fast Mags', 'Quickdraw', 'Stock', 'Laser Sight II', 'Fast Mags II', 'Quickdraw II'],
            'SWAT RFT': ['Quickdraw', 'Fast Mags', 'FMJ', 'Long Barrel', 'Stock', 'Extended Mags', 'High Caliber', 'Suppressor'],
            'Grav': ['Grip', 'Long Barrel', 'FMJ', 'Extended Mags', 'Stock', 'Grip II', 'Suppressor', 'Laser Sight', 'Quickdraw'],
            'Peacekeeper': ['Stock', 'Quickdraw', 'Grip', 'Suppressor', 'Stock II', 'Quickdraw II', 'Rapid Fire', 'Hybrid Mags'],
            'AN-94': ['Grip', 'Stock', 'Hybrid Mags', 'Long Barrel', 'Laser Sight', 'Quickdraw', 'High Caliber', 'Suppressor'],
            'Doublecross': ['Extended Mags', 'Laser Sight', 'FMJ', 'Long  Barrel', 'Grip', 'Extended Mags II', 'Laser Sight II', 'High Caliber', 'Stock'],
            'MX9': ['Suppressor', 'Hybrid Mags', 'Long Barrel', 'FMJ', 'Laser Sight', 'Stock', 'Rapid Fire', 'High Caliber'],
            'GKS' :['Grip', 'Quickdraw', 'Long Barrel','Extended Mags', 'Grip II', 'Suppressor', 'Long Barrel II'],
            'Spitfire': ['Laser Sight', 'Extended Mags', 'Fast Mags', 'FMJ', 'Laser Sight II', 'Quickdraw', 'Stock'],
            'Cordite': ['Extended Mags', 'Laser Sight', 'FMJ', 'Long Barrel', 'Grip', 'Rapid Fire', 'FMJ II'],
            'Saug 9MM': ['Stock', 'Fast Mags', 'Quickdraw', 'Grip', 'Stock II', 'Fast Mags II', 'Suppressor'],
            'Daemon 3XB': ['High Caliber', 'Steady Grip', 'Fast Mags', 'Rapid Fire', 'High Caliber II', 'Laser Sight', 'Hybrid Mags', 'Suppressor'],
            'Switchblade X9': ['Quickdraw', 'Rapid Fire', 'Stabilizer', 'Stock', 'Hybrid Mags', 'Quickdraw II', 'Rapid Fire II', 'Grip', 'Laser Sight', 'FMJ'],
            'VMP': ['Laser Sight', 'Stock', 'Fast Mags', 'Long Barrel', 'Grip', 'Quickdraw', 'Extended Mags', 'Suppressor'],
            'MicroMG 9MM': ['Extended Mags', 'Laser Sight', 'FMJ', 'Steady Grip', 'Rapid Fire', 'Extended Mags II', 'Laser Sight II', 'FMJ II', 'Grip'],
            'Auger DMR': ['High Caliber', 'FMJ', 'Long Barrel', 'Laser Sight', 'High Caliber II', 'FMJ II', 'Fast Mags'],
            'ABR 223': ['Laser Sight', 'Quickdraw', 'Stock', 'Extended Mags', 'Laser Sight II', 'Grip', 'Stock II', 'Suppressor'],
            'Swordfish': ['Quickdraw', 'Suppressor', 'FMJ', 'Long Barrel', 'Quickdraw II', 'Hybrid Mags', 'High Caliber'],
            'S6 Stingray': ['Stock', 'Suppresssor', 'Long Barrel', 'Hybrid Mags','Quickdraw', 'Grip', 'Laser Sight', 'Rapid Fire'],
            'M16': ['High Caliber', 'Grip', 'Extended Mags', 'Stock', 'Suppressor', 'High Caliber', 'Grip II', 'Fast Mags', 'Quickdraw', 'FMJ'],
            'Titan': ['Extended Mags', 'FMJ', 'Quickdraw', 'Stock', 'Extended Mags II', 'FMJ II'],
            'Hades': ['Laser Sight', 'Steady Grip', 'FMJ', 'Hybrid Mags', 'Laser Sight II', 'Suppressor', 'Rapid Fire'],
            'VKM 750': ['High Caliber', 'Grip', 'Extended Mags', 'Fast Mags', 'High Caliber II', 'Quickdraw', 'Rapid Fire'],
            'Tigershark': ['Stock', 'Laser Sight', 'FMJ', 'Fast Mags', 'Stock II', 'Grip', 'High Caliber', 'Suppressor'],
            'Paladin HB50': ['High Caliber', 'FMJ', 'Stabilizer','Sight Loader', 'High Caliber II', 'FMJ II', 'Stabilizer', 'Stabilizer II'],
            'Outlaw': ['Rapid Fire', 'Suppressor', 'High Caliber', 'Stock', 'Quickdraw', 'Grip', 'Stabilizer', 'Hybrid Mags'],
            'SDM': ['Grip', 'Extended Mags', 'FMJ', 'High Caliber', 'Grip II', 'Extended Mags II', 'Stabilizer', 'Laser Sight'],
            'Koshka': ['Quickdraw', 'Laser Sight', 'Fast Mags', 'FMJ', 'Quickdraw II', 'Laser Sight II', 'Stock', 'High Caliber'],
            'Vendetta': ['Stock','Sight Loader', 'Quickdraw', 'Grip', 'Stock II', 'Extended Mags', 'FMJ', 'Suppressor'],
            'Locus': ['Fast Mags', 'FMJ', 'Stock', 'Stabilizer', 'Extended Mags', 'Rapid Fire', 'Suppressor'],
            'Havelina AA50': ['High Caliber', 'Grip', 'Extended Mags', 'FMJ', 'High Caliber II', 'Stabilizer', 'Speed Loader', 'Stock'],
            'Strife': ['Suppressor', 'FMJ', 'Long Barrel', 'Quickdraw', 'Laser Sight', 'FMJ II', 'Extended Mags'],
            'RK7 Garrison': ['Extended Mags', 'Laser Sights', 'Grip', 'Rapid Fire', 'Extended Mags II', 'Laser Sight II', 'Suppressor'],
            'Mozu': ['High Caliber', 'Long Barrel', 'Speed Loader', 'Stabilizer', 'Stock', 'Long Barrel II', 'Quickdraw'],
            'Kap 45': ['Rapid Fire', 'Fast Mags', 'FMJ', 'Grip', 'Rapid Fire II', 'Hybrid Mags', 'High Caliber', 'Stock'],
            'MOG 12': ['Long Barrel', 'Fast Mags', 'Rapid Fire', 'Stock', 'Barrel Choke', 'Speed Loader', 'Quickdraw'],
            'SG12': ['Extended Mags','Laser Sight', 'Steady Grip', 'Max Load', 'Extended Mags II'],
            'Rampage': ['Stock', 'Quickdraw', 'Grip', 'Hybrid Mags', 'Stock II', 'Quickdraw II', 'Grip II', 'Max Load'],
            'Argus': ['Quickdraw', 'Long Barrel', 'Fast Mags', 'Rapid Fire', 'Stock', 'Suppressor', 'Extended Mags'],
            'Hellion Salvo': ['Rocket Cache', 'Fast Loader', 'High Explosive'],
            'Combat Knife': None,
            'Ballistic Knife': ['Extra Blades', 'Fast Reload', 'Gas Powered'],
            'Reaver C86': ['Stock', 'Extended Mags', 'Titanium Bolts']}
# Dictionary containing all Operator Mods by Primary Weapon
primaryOperatorMods = {'VAPR-XKG': 'Bayonet',
                'Maddox RFB': 'Echo Fire',
                'GKS': 'Quad Shot',
                'Spitfire': 'Wild Fire',
                'Cordite': 'Belt-Feed',
                'Saug 9MM': 'Dual Wield',
                'Auger DMR': 'Double Tap',
                'ABR 223': 'Repeater',
                'Swordfish': 'Penta Burst',
                'S6 Stingray': 'Impact Blast',
                'Titan': 'Oppressor',
                'Hades': 'Cross Bar',
                'VKM 750': 'Fat Barrel',
                'Tigershark': 'Burst Rush',
                'Outlaw': 'Bolt Cylinder',
                'Koshka': 'Strelok',
                'Vendetta': 'Bipod'}
# Dictionary containing all Operator Mods by Secondary Weapon
secondaryOperatorMods={'Strife': 'Stiletto Knife',
                'Mozu': 'Skull Splitter',
                'MOG 12': 'Dragon Breath',
                'SG12': 'Strobe Light',
                'Ballistic Knife': 'Dual Wield'}
# List containing all Gears
gear = ['Stim Shot', 'Acoustic Sensor', 'Body Armor', 'Equipment Charge', 'COMSEC Device']
# List containing all Perk 1s
Perk1=['Scavenger ', 'Engineer ', 'Flak Jacket ', 'Tactical Mask ']
# List containing all Perk 2s
Perk2=['Leightweight ', 'Skulker ', 'Cold Blooded ', 'Gung Ho ', 'Dexterity ']
# List containing all Perk 3s
Perk3=['Ghost ', 'Team Link ', 'Dead Silence ', 'Tracker ']
# List containing all Equipments
equipment = ['Trophy System', 'Combat Axe', 'Frag', 'Molotov', 'Concussion']
# List containing all Scorestreaks
streaks = ["Dart", "RC-XD", "UAV", "Care Package", "Counter-UAV", "Lightning Strike", "Sentry","Hellstorm", "Drone Squad", "Sniper's Nest", "Mantis", "Thresher", "Attack Chopper", "Strike Team", "Gunship"]
# List containing all Wildcards
wildcards = ['Overkill', 'Primary Gunfighter 1', 'Primary Operator Mod', 'Perk 1 Gluttony', 'Perk 2 Gluttony', 'Perk 3 Gluttony', 'Underkill', 'Secondary Gunfighter 1', 'Secondary Operator Mod', 'Perk 1 Greed', 'Perk 2 Greed', 'Perk 3 Greed']
# Dictionary containing names of functions for each Wildcard
wildcard_methods = {
        'Overkill': 'overkillFunct',
        'Underkill': 'underkillFunct',
        'Primary Gunfighter 1': 'primaryGunfighter1Funct',
        'Primary Gunfighter 2': 'primaryGunfighter2Funct',
        'Primary Gunfighter 3': 'primaryGunfighter3Funct',
        'Secondary Gunfighter 1': 'secondaryGunfighter1Funct',
        'Secondary Gunfighter 2': 'secondaryGunfighter2Funct',
        'Secondary Gunfighter 3': 'secondaryGunfighter3Funct',
        'Perk 1 Gluttony': 'perk1GluttonyFunct',
        'Perk 2 Gluttony': 'perk2GluttonyFunct',
        'Perk 3 Gluttony': 'perk3GluttonyFunct',
        'Perk 1 Greed': 'perk1GreedFunct',
        'Perk 2 Greed': 'perk2GreedFunct',
        'Perk 3 Greed': 'perk3GreedFunct',
        'Primary Operator Mod': 'primaryOperatorModFunct',
        'Secondary Operator Mod': 'secondaryOperatorModFunct'
    }
# Dictionary containing how many items will be added to the Class by Wildcard
wildcardMinimums = {'Overkill': 3, 'Primary Gunfighter 1': 5, 'Primary Operator Mod': 4, 'Perk 1 Gluttony': 4,
                        'Perk 2 Gluttony': 4, 'Perk 3 Gluttony': 4, 'Underkill': 3, 'Secondary Operator Mod': 4,
                        'Primary Gunfighter 2': 2, 'Primary Gunfighter 3': 2, 'Secondary Gunfighter 2': 2,
                        'Secondary Gunfighter 3': 2, 'Perk 1 Greed': 3, 'Perk 2 Greed': 3, 'Perk 3 Greed': 3,
                        'Secondary Gunfighter 1': 5}
# Lists containing Wildcards that are incompatible with selected Wildcard
removeForGluttony1 = ['Perk 2 Gluttony', 'Perk 3 Gluttony', 'Perk 2 Greed', 'Perk 3 Greed']
removeForGluttony2 = ['Perk 1 Gluttony', 'Perk 3 Gluttony', 'Perk 1 Greed', 'Perk 3 Greed']
removeForGluttony3 = ['Perk 1 Gluttony', 'Perk 2 Gluttony', 'Perk 1 Greed', 'Perk 2 Greed']
removeForGreed1 = ['Perk 2 Gluttony', 'Perk 3 Gluttony']
removeForGreed2 = ['Perk 1 Gluttony', 'Perk 3 Gluttony']
removeForGreed3 = ['Perk 1 Gluttony', 'Perk 2 Gluttony']


class rcg:
    # Initialize attributes of the class
    def __init__(self):
       
        self.pick10 = random.randint(0,10)

        self.primary = None
        self.primaryOptic = None
        self.primaryAttachments = []
        self.primaryOperatorMod = None
        self.secondary = None
        self.secondaryOptic = None
        self.secondaryAttachments = []
        self.secondaryOperatorMod = None
        self.perk1 = []
        self.perk2 = []
        self.perk3 = []
        self.gear = None
        self.equipment = None
        self.wildcards = []
        self.specialist = None
        self.scorestreaks = []
    
    # Define function to pick scorestreaks
    def scorestreaksFunct(self):
        self.scorestreaks = random.sample(streaks, 3)
        return self.scorestreaks
    
    # Define function to pick specialist
    def specialistFunct(self):
        self.specialist = random.choice(specialists)
        return self.specialist
    
    # Define function to pick equipment
    def equipmentFunct(self):
        if self.pick10 == 1:
            amount = 1
            self.equipment = random.choice(equipment)
            self.pick10 -= amount
        if self.pick10 > 1:
            self.equipment = random.choice(equipment)
            if self.equipment in ('Trophy System','Combat Axe','Concussion'):
                amount = random.randint(1,2) 
            else:
                amount = 1
            self.pick10 -= amount
            self.equipment = f'{amount} {self.equipment}'
            if amount == 2:
                self.equipment += 's'
        return self.equipment
    
    # Define function to pick gear
    def gearFunct(self):
        if self.pick10 >= 1:
            self.gear = random.choice(gear)
            self.pick10 -= 1
        return self.gear

    ###### PRIMARY WEAPON FUNCTIONS

    # Define function to pick primary weapon    
    def primaryFunct(self):
        if self.primary == None:
            if self.pick10 > 0:
                a = random.randint(0, len(primaries)-1)
                b = primaries[a]
                c = random.randint(0, len(b)-1)
                self.primary = b[c]
                self.pick10 -= 1
        return self.primary
    
    # Define function to pick primary weapon optic
    def primaryOpticFunct(self):
        if self.primary in ('Ballistic Knife', 'Combat Knife'):
            return self.primaryOptic
        if self.pick10 >= 1 and self.primary != None:
            self.primaryOptic = random.choice(optics[self.primary])
            self.pick10 -= 1
        return self.primaryOptic
    
    # Define function to pick primary weapon attachments
    def primaryAttachmentsFunct(self):
        if self.primary == 'Combat Knife':
            return self.primaryAttachments
        if self.pick10 >= 2 and self.primary != None: 
            num_attachments = random.randint(0,2)
            self.primaryAttachments = random.sample(attachments[self.primary], num_attachments)
            self.pick10 -= num_attachments
        elif self.pick10 >= 1 and self.primary != None:
            num_attachments = random.randint(0,1)
            self.primaryAttachments = random.sample(attachments[self.primary], num_attachments)
            self.pick10 -= num_attachments
        return self.primaryAttachments
    
    ###### SECONDARY WEAPON FUNCTIONS

    # Define function to pick secondary weapon
    def secondaryFunct(self):
        if self.secondary == None:
            if self.pick10 > 0:
                d = random.randint(0, len(secondaries)-1)
                e = secondaries[d]
                f = random.randint(0, len(e)-1)
                self.secondary = e[f]
                self.pick10 -= 1
        return self.secondary
    
    # Define function to pick secondary weapon optic
    def secondaryOpticFunct(self):
        if self.secondary in ('Ballistic Knife', 'Combat Knife'):
            return self.secondaryOptic
        if self.pick10 >= 1 and self.secondary != None:
            self.secondaryOptic = random.choice(optics[self.secondary])
            self.pick10 -= 1
        return self.secondaryOptic
    
    # Define function to pick secondary weapon attachments
    def secondaryAttachmentsFunct(self):
        if self.secondary == 'Combat Knife':
            return self.secondaryAttachments
        if self.pick10 >= 1 and self.secondary != None: 
            num_attachments = random.randint(0,1)
            self.secondaryAttachments = random.sample(attachments[self.secondary], num_attachments)
            self.pick10 -= num_attachments
        return self.secondaryAttachments
    
    ###### PERK FUNCTIONS
    
    # Define function to pick perk 1
    def perk1Funct(self):
        if self.perk1 == None:
            if self.pick10 >= 1:
                self.perk1 = random.choice(Perk1)
                self.pick10 -= 1
        return self.perk1
    
    # Define function to pick perk 2
    def perk2Funct(self):
        if self.perk2 == None:
            if self.pick10 >= 1:
                self.perk2 = random.choice(Perk2)
                self.pick10 -= 1
        return self.perk2
    
    # Define function to pick perk 3
    def perk3Funct(self):
        if self.perk3 == None:
            if self.pick10 >= 1:
                self.perk3 = random.choice(Perk3)
                self.pick10 -= 1
        return self.perk3
    
    ###### WILDCARD FUNCTIONS

    # Define function to choose wildcards
    def wildcardsFunct(self):
        global wildcards
        # Choose how many Wildcards will be in the Class
        numOfWildcards = random.randint(0, 3)

        # Choose numbers representing indices of Wildcards in "wildcards" 
        tacotuesday = random.sample(range(0, len(wildcards)), numOfWildcards)
        sortedTacos = sorted(tacotuesday)

        # List of Wildcards to add to the Class
        chosenWildcards = []

        # Lists containing Wildcards that are incompatible with selected Wildcard
        removeForGluttony1 = ['Perk 2 Gluttony', 'Perk 3 Gluttony', 'Perk 2 Greed', 'Perk 3 Greed']
        removeForGluttony2 = ['Perk 1 Gluttony', 'Perk 3 Gluttony', 'Perk 1 Greed', 'Perk 3 Greed']
        removeForGluttony3 = ['Perk 1 Gluttony', 'Perk 2 Gluttony', 'Perk 1 Greed', 'Perk 2 Greed']
        removeForGreed1 = ['Perk 2 Gluttony', 'Perk 3 Gluttony']
        removeForGreed2 = ['Perk 1 Gluttony', 'Perk 3 Gluttony']
        removeForGreed3 = ['Perk 1 Gluttony', 'Perk 2 Gluttony']

        # "x" represents how many items each Wildcard in the Class adds?
        x = []
        # Sum of number of items added from all wildcards
        wildcardCost = 0

        # for each number (representing the index of a Wildcard) 
        for yur in sortedTacos:

            wildcards = ['Overkill', 'Primary Gunfighter 1', 'Primary Operator Mod', 'Perk 1 Gluttony', 'Perk 2 Gluttony','Perk 3 Gluttony', 'Underkill', 'Secondary Gunfighter 1', 'Secondary Operator Mod', 'Perk 1 Greed','Perk 2 Greed', 'Perk 3 Greed']
            # Rechoose index number?
            yur = random.randint(0, len(wildcards)-1)
            # Add Wildcard to the Class
            chosenWildcards.append(wildcards[yur])
            # Update number of items added from Wildcard
            wildcardCost += wildcardMinimums[chosenWildcards[-1]]
            # Add number of items the Wildcard adds to the list
            x.append(wildcardMinimums[chosenWildcards[-1]])
            # "flip" represents ??
            flip = 0
            
            
            if len(chosenWildcards) == 2 and (chosenWildcards.count('Primary Gunfighter 1') +
            chosenWildcards.count('Overkill') +
            chosenWildcards.count('Underkill') +
            chosenWildcards.count('Primary Operator Mod') +
            chosenWildcards.count('Primary Gunfighter 2') == 2):
                self.pick10 += 1
                flip = 1
            if len(chosenWildcards) == 3 and (chosenWildcards.count('Primary Gunfighter 1') +
            chosenWildcards.count('Underkill') +
            chosenWildcards.count('Overkill') +
            chosenWildcards.count('Primary Operator Mod') +
            chosenWildcards.count('Primary Gunfighter 2') +
            chosenWildcards.count('Primary Gunfighter 3') == 3):
                self.pick10 += 1
                flip = 1
            if len(chosenWildcards) == 2 and (chosenWildcards.count('Secondary Gunfighter 1') +
            chosenWildcards.count('Overkill') +
            chosenWildcards.count('Underkill') +
            chosenWildcards.count('Secondary Operator Mod') + 
            chosenWildcards.count('Secondary Gunfighter 2') == 2):
                self.pick10 += 1
                flip = 1
            if len(chosenWildcards) == 3 and (chosenWildcards.count('Secondary Gunfighter 1') +
            chosenWildcards.count('Overkill') +
            chosenWildcards.count('Underkill') +
            chosenWildcards.count('Secondary Operator Mod') + 
            chosenWildcards.count('Secondary Gunfighter 2') +
            chosenWildcards.count('Secondary Gunfighter 3') == 3):
                self.pick10 += 1
                flip = 1
            if len(chosenWildcards) == 2 and (chosenWildcards.count('Perk 1 Greed') + 
            chosenWildcards.count('Perk 1 Gluttony') == 2 ): 
                self.pick10 +=1
                flip = 1
            if len(chosenWildcards) == 3 and (chosenWildcards.count('Perk 1 Greed') + 
            chosenWildcards.count('Perk 1 Gluttony') == 2 ): 
                self.pick10 += 1
                flip = 1
            if len(chosenWildcards) == 2 and (chosenWildcards.count('Perk 2 Greed') + 
            chosenWildcards.count('Perk 2 Gluttony') == 2 ): 
                self.pick10 += 1
                flip = 1
            if len(chosenWildcards)==3 and (chosenWildcards.count('Perk 2 Greed') + 
            chosenWildcards.count('Perk 2 Gluttony') == 2 ): 
                self.pick10 += 1
                flip = 1
            if len(chosenWildcards) == 2 and (chosenWildcards.count('Perk 3 Greed') + 
            chosenWildcards.count('Perk 3 Gluttony') == 2 ): 
                self.pick10 += 1
                flip = 1
            if len(chosenWildcards) == 3 and (chosenWildcards.count('Perk 3 Greed') + 
            chosenWildcards.count('Perk 3 Gluttony') == 2 ): 
                self.pick10 += 1
                flip = 1
            
            if x[-1] > self.pick10:
                if chosenWildcards:
                    chosenWildcards.pop()
                    wildcards.pop(yur)
                    wildcardCost -= x[-1]
                    x.pop()
                    self.pick10 -= flip
                continue
            else:
                self.pick10 = self.pick10 - x[-1]
                
            if 'Overkill' in chosenWildcards[-1]:
                wildcards.remove('Underkill')
            elif 'Underkill' in chosenWildcards[-1]:
                wildcards.remove('Overkill')

            if 'Primary Gunfighter 1' in chosenWildcards[-1]:
                wildcards.append('Primary Gunfighter 2')
            elif 'Primary Gunfighter 2' in chosenWildcards[-1]:
                wildcards.append('Primary Gunfighter 3')

            if 'Secondary Gunfighter 1' in chosenWildcards[-1]:
                wildcards.append('Secondary Gunfighter 2')
            elif 'Secondary Gunfighter 2' in chosenWildcards[-1]:
                wildcards.append('Secondary Gunfighter 3')

            if 'Perk 1 Greed' in chosenWildcards[-1]:
                wildcards = [n for n in wildcards if n not in removeForGreed1]
            if 'Perk 2 Greed' in chosenWildcards[-1]:
                wildcards = [w for w in wildcards if w not in removeForGreed2]
            if 'Perk 3 Greed' in chosenWildcards[-1]:
                wildcards = [m for m in wildcards if m not in removeForGreed3]

            if 'Perk 1 Gluttony' in chosenWildcards[-1]:
                wildcards = [o for o in wildcards if o not in removeForGluttony1]
            if 'Perk 2 Gluttony' in chosenWildcards[-1]:
                wildcards = [p for p in wildcards if p not in removeForGluttony2]
            if 'Perk 3 Gluttony' in chosenWildcards[-1]:
                wildcards = [q for q in wildcards if q not in removeForGluttony3]

            wildcards = [v for v in wildcards if v not in chosenWildcards]
            random.shuffle(wildcards)

            if self.pick10 == 0:
                break
        
        for wildcard in chosenWildcards:
            method_name = wildcard_methods[wildcard]
            method = getattr(rcg, method_name)
            result = method(self)

        self.wildcards = chosenWildcards
        return self.wildcards


    # Define function to pick primary weapon attachments with primary gunfighter 1 wildcard
    def primaryGunfighter1Funct(self):
        if self.primary == None:
            a = random.randint(0, len(primaries)-1)
            b = primaries[a]
            c = random.randint(0, len(b)-1)
            self.primary = b[c]
        self.primaryAttachments = random.sample(attachments[self.primary], 3)
        return self.primary, self.primaryAttachments
    
    # Define function to pick primary weapon attachments with primary gunfighter 2 wildcard
    def primaryGunfighter2Funct(self):
        if len(attachments[self.primary]) >= 4:
            self.primaryAttachments = random.sample(attachments[self.primary], 4)
            return self.primaryAttachments
        else:
            print("ERROR ERROR ERROR NOT ENOUGH ATTACHMENTS")
    
    # Define function to pick primary weapon attachments with primary gunfighter 3 wildcard
    def primaryGunfighter3Funct(self):
        if len(attachments[self.primary]) >= 5:
            return random.sample(attachments[self.primary], 5)
        else:
            print("ERROR ERROR ERROR NOT ENOUGH ATTACHMENTS")
            
    # Define function to pick secondary weapon attachments with secondary gunfighter 1 wildcard
    def secondaryGunfighter1Funct(self):
        if self.secondary == None:
            a =random.randint(0, len(secondaries)-1)
            b = secondaries[a]
            c = random.randint(0, len(b)-1)
            self.secondary = b[c]
        self.secondaryAttachments = random.sample(attachments[self.secondary], 2 if len(attachments[self.secondary]) > 1 else 0)    # may not need if statement once other pick10 logic is implemented
        return self.secondary, self.secondaryAttachments
    
    # Define function to pick secondary weapon attachments with secondary gunfighter 2 wildcard
    def secondaryGunfighter2Funct(self):
        self.secondaryAttachments = random.sample(attachments[self.secondary], 3 if len(attachments[self.secondary]) > 2 else 0)    # may not need if statement once other pick10 logic is implemented
        return self.secondary, self.secondaryAttachments
    
    # Define function to pick secondary weapon attachments with secondary gunfighter 3 wildcard
    def secondaryGunfighter3Funct(self):
        self.secondaryAttachments = random.sample(attachments[self.secondary], 4 if len(attachments[self.secondary]) > 3 else 0)    # may not need if statement once other pick10 logic is implemented
        return self.secondary, self.secondaryAttachments
    
    # Define function to pick perk 1s with perk 1 gluttony wildcard
    def perk1GluttonyFunct(self):
        Perk1=['Scavenger ', 'Engineer ', 'Flak Jacket ', 'Tactical Mask ']
        gluts1 = random.sample(Perk1, 3)
        self.perk1 = gluts1[0]
        self.perk2 = gluts1[1]
        self.perk3 = gluts1[2]
        Perk1 = [u for u in Perk1 if u not in gluts1]
        return self.perk1, self.perk2, self.perk3
    
    # Define function to pick perk 2s with perk 2 gluttony wildcard  
    def perk2GluttonyFunct(self):
        Perk2=['Leightweight ', 'Skulker ', 'Cold Blooded ', 'Gung Ho ', 'Dexterity ']
        gluts2 = random.sample(Perk2, 3)
        self.perk1 = gluts2[0]
        self.perk2 = gluts2[1]
        self.perk3 = gluts2[2]
        Perk2 = [u for u in Perk2 if u not in gluts2]
        return self.perk1, self.perk2, self.perk3
    
    # Define function to pick perk 3s with perk 3 gluttony wildcard
    def perk3GluttonyFunct(self):
        Perk3=['Ghost ', 'Team Link ', 'Dead Silence ', 'Tracker ']
        gluts3 = random.sample(Perk3, 3)
        self.perk1 = gluts3[0]
        self.perk2 = gluts3[1]
        self.perk3 = gluts3[2]
        Perk3 = [u for u in Perk3 if u not in gluts3]
        return self.perk1, self.perk2, self.perk3
    
    # Define function to pick perk 1s with perk 1 greed wildcard
    def perk1GreedFunct(self):
        Perk1=['Scavenger ', 'Engineer ', 'Flak Jacket ', 'Tactical Mask ']
        if self.perk1 == []:
            self.perk1 = random.sample(Perk1, 2)
        else:
            random1 = random.randint(0, len(Perk1)-1)
            self.perk1 = self.perk1 + 'and ' + (Perk1[random1])
        return self.perk1
    
    # Define function to pick perk 2s with perk 2 greed wildcard
    def perk2GreedFunct(self):
        Perk2=['Leightweight ', 'Skulker ', 'Cold Blooded ', 'Gung Ho ', 'Dexterity ']
        if self.perk2 == []:
            self.perk2 = random.sample(Perk2, 2)
        else:
            random2 = random.randint(0, len(Perk2)-1)
            self.perk2 = self.perk2 + 'and ' + (Perk2[random2])
        return self.perk2
    
    # Define function to pick perk 3s with perk 3 greed wildcard
    def perk3GreedFunct(self):
        Perk3=['Ghost ', 'Team Link ', 'Dead Silence ', 'Tracker ']
        if self.perk3 == []:
            self.perk3 = random.sample(Perk3, 2)
        else:
            random3 = random.randint(0, len(Perk3)-1)
            self.perk3 = self.perk3 + 'and ' + (Perk3[random3])
        return self.perk3
    
    # Define function to pick primary and secondary weapons with overkill wildcard
    def overkillFunct(self):
        a = random.randint(0, len(primaries)-1)
        b = primaries[a]
        c = random.randint(0, len(b)-1)
        self.primary = b[c]
        a = random.randint(0, len(primaries)-1)
        b = primaries[a]
        c = random.randint(0, len(b)-1)
        self.secondary = b[c]
        while self.secondary == self.primary:
             a = random.randint(0, len(primaries)-1)
             b = primaries[a]
             c = random.randint(0, len(b)-1)   
        return self.primary, self.secondary

    # Define function to pick primary and secondary weapons with underkill wildcard
    def underkillFunct(self):
        d = random.randint(0, len(secondaries)-1)
        e = secondaries[d]
        f = random.randint(0, len(e)-1)
        self.primary= e[f]
        d = random.randint(0, len(secondaries)-1)
        e = secondaries[d]
        f = random.randint(0, len(e)-1)
        self.secondary= e[f]
        while self.primary == self.secondary:
            d = random.randint(0, len(secondaries)-1)
            e = secondaries[d]
            f = random.randint(0, len(e)-1)
        return self.primary, self.secondary
    
    # Define function to pick primary weapon operator mod
    def primaryOperatorModFunct(self):
        if self.primary not in list(primaryOperatorMods.keys()):
            self.primary = random.choice(list(primaryOperatorMods.keys()))
        self.operatorMod1 = primaryOperatorMods[self.primary]
        return self.primary, self.operatorMod1
    
    # Define function to pick secondary weapon operator mod
    def secondaryOperatorModFunct(self):
        if self.secondary not in list(secondaryOperatorMods.keys()):
            self.secondary = random.choice(list(secondaryOperatorMods.keys()))
        self.operatorMod2 = secondaryOperatorMods[self.secondary]
        return self.secondary, self.operatorMod2
    
    ###### SPEND REMAINING ITEMS
    def spendRemainingPick10(self):
        slots = [
            'primary', 'secondary', 'primaryOptic', 'secondaryOptic',
            'primaryAttachments', 'secondaryAttachments',
            'perk1', 'perk2', 'perk3',
            'gear', 'equipment'
        ]

        made_progress = True

        while self.pick10 > 0 and made_progress:
            made_progress = False  
            random.shuffle(slots)  

            for slot in slots:
                if self.pick10 <= 0:
                    break

                current_value = getattr(self, slot)
                if current_value not in (None, [], ''):
                    continue  

                before = self.pick10

                if slot in ('perk1', 'perk2', 'perk3'):
                    setattr(self, slot, random.choice(eval(slot.capitalize())))
                    self.pick10 -= 1

            
                elif slot in ('primaryAttachments', 'secondaryAttachments'):
                    weapon_attr = slot.replace('Attachments', '')
                    weapon = getattr(self, weapon_attr)

                    if weapon in (None, 'Combat Knife'):
                        continue

                    max_attachments = min(2, self.pick10)
                    num_attachments = random.randint(1, max_attachments)
                    chosen_attachments = random.sample(attachments[weapon], num_attachments)
                    setattr(self, slot, chosen_attachments)
                    self.pick10 -= num_attachments

                elif slot in ('primaryOptic', 'secondaryOptic'):
                    weapon_attr = slot.replace('Optic', '')
                    weapon = getattr(self, weapon_attr)

                    if weapon in (None, 'Combat Knife', 'Ballistic Knife'):
                        continue

                    setattr(self, slot, random.choice(optics[weapon]))
                    self.pick10 -= 1

                elif slot in ('primary', 'secondary'):
                    weapon_groups = primaries if slot == 'primary' else secondaries
                    weapon_list = random.choice(weapon_groups)
                    weapon = random.choice(weapon_list)
                    setattr(self, slot, weapon)
                    self.pick10 -= 1

                elif slot == 'gear':
                    chosen_gear = random.choice(gear)
                    setattr(self, slot, chosen_gear)
                    self.pick10 -= 1

                elif slot == 'equipment':
                    items = ['Trophy System', 'Combat Axe', 'Frag', 'Molotov', 'Concussion']
                    item = random.choice(items)

                    if item in ('Trophy System', 'Combat Axe', 'Concussion'):
                        amount = random.randint(1, min(2, self.pick10))
                    else:
                        amount = 1

                    equipment_text = f"{amount} {item}" + ("s" if amount == 2 else "")
                    setattr(self, slot, equipment_text)
                    self.pick10 -= amount

                # Track progress 
                if self.pick10 < before:
                    made_progress = True

            # Safety check s
            if not made_progress:
                break

        return self

def generate_class():
    
    # Initialize class
    jake_rcg = rcg()

    #num_items = self.pick10

    # Choose wildcards
    jake_rcg.wildcards = jake_rcg.wildcardsFunct()

    # Fill rest of class
    jake_rcg = jake_rcg.spendRemainingPick10()

    ## Choose scorestreaks
    jake_rcg.scorestreaks = jake_rcg.scorestreaksFunct()

    # Choose specialist
    jake_rcg.specialist = jake_rcg.specialistFunct()

    return {
        #"Number of Items": #num_items,
        "Primary Weapon": jake_rcg.primary,
        "Primary Optic": jake_rcg.primaryOptic,
        "Primary Attachments": jake_rcg.primaryAttachments,
        "Primary Operator Mod": jake_rcg.primaryOperatorMod,
        "Secondary Weapon": jake_rcg.secondary,
        "Secondary Optic": jake_rcg.secondaryOptic,
        "Secondary Attachments": jake_rcg.secondaryAttachments,
        "Secondary Operator Mod": jake_rcg.secondaryOperatorMod,
        "Perk 1": jake_rcg.perk1,
        "Perk 2": jake_rcg.perk2,
        "Perk 3": jake_rcg.perk3,
        "Gear": jake_rcg.gear,
        "Equipment": jake_rcg.equipment,
        "Wildcards": jake_rcg.wildcards,
        "Specialist": jake_rcg.specialist,
        "Scorestreaks": jake_rcg.scorestreaks
    }






#MIGHT STILL HAVE ISSUE WITH pick10 GETTING ADDED 1 INCORRECTLY WITH WILDCARDS
#SECONDARIES WITHOHUT ENOUGH ATTACHMENTS/KNIFE DON'T WORK WITH ATTACHMENTS
#ORDER OF WILDCARDS IS MESSED UP, UNDERKILL OVERWRITES PRIMARY OPERATOR MOD
#NO OPTICS ARE RETURNING AT ALL!


#########################################     BUGS     ################################################33
# no other class needed just need to feed class named rcg

# issues with how wildcards remove incompatible ones from potential list



#Infinite Looping
#ValueError: sample larger than population or is negative in [183] line 570 result = method(), in line 482 in secondaryGunfighter1Funct self.secondaryAttachments = random.sample(attachments{self.secondary],3)
#If you get perk 1 greed then gluttony, it will just do 3 perks instead of 3 and then the 4th being in the original perk number
#Primary/secondary gunfighter 2 and 3 don't need to adjust pick 10 by one because their value is already 2 instead of 3 like gunfighter 1.
#Pick10 gets inflated when two synergistic wildcards are selected, but pick10 is not big enough to accommodate the second wildcard - it keeps the plus 1 though.