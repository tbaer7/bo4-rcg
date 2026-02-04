# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 17:30:11 2024

@author: jaker
"""

import random
from random import randint

#random_integer = random.randint(1, 10)  # Generates a random integer between 1 and 10 (inclusive)

# List containing all Specialists
specialists=['Ajax', 'Torque', 'Battery', 'Reaper', 'Spectre', 'Ruin', 'Outrider', 'Prophet', 'Firebreak', 'Zero', 'Crash', 'Nomad', 'Seraph', 'Recon']
chosenSpecialist = specialists[random.randint(0,len(specialists)-1)]
#print(chosenSpecialist)

# List of lists containing all Primary Weapons by category (AR, SMG, Tac Rifle, LMG, Sniper Rifle)
primaries = [['ICR-7','Rampart 17', 'KN-57', 'VAPR-XKG', 'Maddox RFB', 'SWAT RFT', 'Grav', 'Peacekeeper', 'AN-94', 'Doublecross'], ['MX9', 'GKS', 'Spitfire', 'Cordite','Saug 9MM', 'Daemon 3XB', 'Switchblade X9','VMP', 'MicroMG 9MM'], ['Auger DMR', 'ABR 223', 'Swordfish', 'S6 Stingray', 'M16' ], ['Titan','Hades', 'VKM 750', 'Tigershark'], ['Paladin HB50', 'Outlaw', 'SDM', 'Koshka', 'Vendetta', 'Locus', 'Havelina AA50']]
#a=random.randint(0,len(primaries)-1)
# = primaries[a]
#c= random.randint(0,len(b)-1)
#print(a,b,c)
#chosenPrimary = b[c]

# List of lists containing all Secondary Weapons by category (Pistol, Shotgun, Rocket Launcher, Special, Melee)
secondaries=[['RK7 Garrison', 'Strife', 'Mozu', 'Kap 45'], ['MOG 12', 'Argus', 'Rampage', 'SG12'], ['Hellion Salvo'], ['Ballistic Knife', 'Reaver C86'], ['Combat Knife']]
#d=random.randint(0,len(secondaries)-1)
#e= secondaries[d]
#f = random.randint(0, len(e)-1)
#print(d,e,f)
#chosenSecondary = e[f]

# Dictionary containing all Optics by weapon
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
             'Combat Knife': [],
             'Ballistic Knife': [],
             'Reaver C86': ['Compact Scope']}

# Dictionary containing all Attachments by weapon
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
             'Combat Knife': [],
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

# List containing all Gears
gear = ['Stim Shot', 'Acoustic Sensor', 'Body Armor', 'Equipment Charge', 'COMSEC Device']
# Choose Gear
chosenGear = gear[random.randint(0,len(gear)-1)]

# List containing all Perk 1s
Perk1=['Scavenger ', 'Engineer ', 'Flak Jacket ', 'Tactical Mask ']
# Choose Perk 1
chosenPerk1 = Perk1[random.randint(0,len(Perk1)-1)]

# List containing all Perk 2s
Perk2=['Leightweight ', 'Skulker ', 'Cold Blooded ', 'Gung Ho ', 'Dexterity ']
# Choose Perk 2
chosenPerk2 = Perk2[random.randint(0,len(Perk2)-1)]

# List containing all Perk 3s
Perk3=['Ghost ', 'Team Link ', 'Dead Silence ', 'Tracker ']
# Choose Perk 3
chosenPerk3 = Perk3[random.randint(0,len(Perk3)-1)]

# "amount" variable indicates how much of the Equipment to use
amount=0

# List containing all Equipments
equipment = ['Trophy System', 'Combat Axe', 'Frag', 'Molotov', 'Concussion']
# Choose Equipment
chosenEquipment = equipment[random.randint(0,len(equipment)-1)]
if chosenEquipment in ('Trophy System','Combat Axe','Concussion'):
    amount = random.randint(1,2) 
else:
    amount = 1


# List containing Scorestreaks in the Class
chosenScorestreaks=[]

# List containing all Scorestreaks
streaks = ["Dart", "RC-XD", "UAV", "Care Package", "Counter-UAV", "Lightning Strike", "Sentry","Hellstorm", "Drone Squad", "Sniper's Nest", "Mantis", "Thresher", "Attack Chopper", "Strike Team", "Gunship"]
# Choose Scorestreaks
scorestreakNumbers=random.sample(range(0,len(streaks)),3)
sortedStreaks = sorted(scorestreakNumbers)
#print(sortedStreaks)
for i in sortedStreaks:
    # Add Scorestreaks to the Class
    chosenScorestreaks.append(streaks[i])

# Choose number of items to be in Class
pick10 = random.randint(0, 10)
#pick10 = 10
print(pick10)

# List containing all Wildcards
wildcards = ['Overkill', 'Primary Gunfighter 1', 'Primary Operator Mod', 'Perk 1 Gluttony', 'Perk 2 Gluttony',
             'Perk 3 Gluttony', 'Underkill', 'Secondary Gunfighter 1', 'Secondary Operator Mod', 'Perk 1 Greed',
             'Perk 2 Greed', 'Perk 3 Greed']

# Dictionary containing how many items will be added to the Class by Wildcard
wildcardMinimums = {'Overkill': 3, 'Primary Gunfighter 1': 5, 'Primary Operator Mod': 4, 'Perk 1 Gluttony': 4,
                    'Perk 2 Gluttony': 4, 'Perk 3 Gluttony': 4, 'Underkill': 3, 'Secondary Operator Mod': 4,
                    'Primary Gunfighter 2': 2, 'Primary Gunfighter 3': 2, 'Secondary Gunfighter 2': 2,
                    'Secondary Gunfighter 3': 2, 'Perk 1 Greed': 3, 'Perk 2 Greed': 3, 'Perk 3 Greed': 3,
                    'Secondary Gunfighter 1': 5}

# Choose how many Wildcards will be in the Class
numOfWildcards = random.randint(0, 3)
#numOfWildcards = 3
print(numOfWildcards)

# Choose numbers representing indices of Wildcards in "wildcards" 
tacotuesday = random.sample(range(0, len(wildcards)), numOfWildcards)
sortedTacos = sorted(tacotuesday)
print(sortedTacos)

print('')

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
    # Rechoose index number?
    yur=random.randint(0,len(wildcards)-1)
    # Add Wildcard to the Class
    chosenWildcards.append(wildcards[yur])
    # Update number of items added from Wildcard
    wildcardCost += wildcardMinimums[chosenWildcards[-1]]
    # Add number of items the Wildcard adds to the list
    x.append(wildcardMinimums[chosenWildcards[-1]])
    print(chosenWildcards)
    print(wildcardCost)
    print(x)
    # "flip" represents ??
    flip=0
    
    
    if len(chosenWildcards)==2 and (chosenWildcards.count('Primary Gunfighter 1') +
    chosenWildcards.count('Overkill') +
    chosenWildcards.count('Underkill') +
    chosenWildcards.count('Primary Operator Mod') +
    chosenWildcards.count('Primary Gunfighter 2') == 2):
        pick10 += 1
        flip=1
    if len(chosenWildcards)==3 and (chosenWildcards.count('Primary Gunfighter 1') +
    chosenWildcards.count('Underkill') +
    chosenWildcards.count('Overkill') +
    chosenWildcards.count('Primary Operator Mod') +
    chosenWildcards.count('Primary Gunfighter 2') +
    chosenWildcards.count('Primary Gunfighter 3') == 3):
        pick10 += 1
        flip=1
    if len(chosenWildcards)==2 and (chosenWildcards.count('Secondary Gunfighter 1') +
    chosenWildcards.count('Overkill') +
    chosenWildcards.count('Underkill') +
    chosenWildcards.count('Secondary Operator Mod') + 
    chosenWildcards.count('Secondary Gunfighter 2') == 2):
        pick10 += 1
        flip=1
    if len(chosenWildcards)==3 and (chosenWildcards.count('Secondary Gunfighter 1') +
    chosenWildcards.count('Overkill') +
    chosenWildcards.count('Underkill') +
    chosenWildcards.count('Secondary Operator Mod') + 
    chosenWildcards.count('Secondary Gunfighter 2') +
    chosenWildcards.count('Secondary Gunfighter 3') == 3):
        pick10 += 1
        flip=1
    if len(chosenWildcards)==2 and (chosenWildcards.count('Perk 1 Greed') + 
    chosenWildcards.count('Perk 1 Gluttony') ==2 ): 
        pick10 +=1
        flip=1
    if len(chosenWildcards)==3 and (chosenWildcards.count('Perk 1 Greed') + 
    chosenWildcards.count('Perk 1 Gluttony') ==2 ): 
        pick10 +=1
        flip=1
    if len(chosenWildcards)==2 and (chosenWildcards.count('Perk 2 Greed') + 
    chosenWildcards.count('Perk 2 Gluttony') ==2 ): 
        pick10 +=1
        flip=1
    if len(chosenWildcards)==3 and (chosenWildcards.count('Perk 2 Greed') + 
    chosenWildcards.count('Perk 2 Gluttony') ==2 ): 
        pick10 +=1
        flip=1
    if len(chosenWildcards)==2 and (chosenWildcards.count('Perk 3 Greed') + 
    chosenWildcards.count('Perk 3 Gluttony') ==2 ): 
        pick10 +=1
        flip=1
    if len(chosenWildcards)==3 and (chosenWildcards.count('Perk 3 Greed') + 
    chosenWildcards.count('Perk 3 Gluttony') ==2 ): 
        pick10 +=1
        flip=1
        
    print(f' pick10 = {pick10}')
    
    if x[-1] > pick10:
        if chosenWildcards:
            chosenWildcards.pop()
            wildcards.pop(yur)
            wildcardCost -= x[-1]
            x.pop()
            pick10 -= flip
        continue
    else:
        pick10 = pick10 - x[-1]
        print(pick10)
        
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

    if pick10 ==0:
        break
    
    print(wildcards)
    
    
print(f' wildcardCost = {wildcardCost}')    
print(f' chosenWildcards = {chosenWildcards}')
print(f' pick10 = {pick10}')



class loadout:
   
    def __init__(self):
        self.primary= None
        self.primaryAttachments =[]
        self.secondary= None
        self.secondaryAttachments = []
        self.equipment=[]
        self.perk1=[]
        self.perk2=[]
        self.perk3=[]
        self.specialist=''
        self.scorestreaks = []
        self.operatorMod1= None
        self.operatorMod2 = None
        
    def fullboat(self):
        pass
        self.specialist = self.specialistFunct()
        self.primary = self.primaryFunct()
        self.secondary = self.secondaryFunct()
        self.perks = [self.perk1Funct(), self.perk2Funct(), self.perk3Funct()]
        self.scorestreaks = self.scorestreaksFunct()
    
    def underkillFunct (self):
        d=random.randint(0,len(secondaries)-1)
        e= secondaries[d]
        f = random.randint(0, len(e)-1)
        self.primary= e[f]
        d=random.randint(0,len(secondaries)-1)
        e= secondaries[d]
        f = random.randint(0, len(e)-1)
        self.secondary= e[f]
        while self.primary == self.secondary:
            d=random.randint(0,len(secondaries)-1)
            e= secondaries[d]
            f = random.randint(0, len(e)-1)
        return self.primary, self.secondary
    
    def overkillFunct (self):
        a=random.randint(0,len(primaries)-1)
        b = primaries[a]
        c= random.randint(0,len(b)-1)
        self.primary = b[c]
        a=random.randint(0,len(primaries)-1)
        b = primaries[a]
        c= random.randint(0,len(b)-1)
        self.secondary = b[c]
        while self.secondary == self.primary:
             a=random.randint(0,len(primaries)-1)
             b = primaries[a]
             c= random.randint(0,len(b)-1)   
        return self.primary, self.secondary
    
    def scorestreaksFunct(self, streaks):
        scorestreakNumbers = random.sample(range(0, len(streaks)), 3)
        sortedStreaks = sorted(scorestreakNumbers)
        for i in sortedStreaks:
            self.scorestreaks.append(streaks[i])
        return self.scorestreaks    
    
    def specialistFunct(self,specialists):
        self.specialist=specialists[random.randint(0,len(specialists)-1)]
        return self.specialist
    
    def primaryOperatorModFunct(self):
        if self.primary not in list(primaryOperatorMods.keys()):
            self.primary = random.choice(list(primaryOperatorMods.keys()))
        self.operatorMod1 = primaryOperatorMods[self.primary]
        return self.primary, self.operatorMod1
    
    def secondaryOperatorModFunct(self):
        if self.secondary not in list(secondaryOperatorMods.keys()):
            self.secondary = random.choice(list(secondaryOperatorMods.keys()))
        self.operatorMod2 = secondaryOperatorMods[self.secondary]
        return self.secondary, self.operatorMod2
    
    
    
            
            
    def perk1Funct(self,pick10):
        self.perk1 = Perk1[random.randint(0,len(Perk1)-1)]
        return self.perk1
    
    def perk2Funct (self,pick10):
        self.perk2 = Perk2[random.randint(0,len(Perk2)-1)]
        return self.perk2
    
    def perk3Funct (self,pick10):    
        self.perk3 = Perk3[random.randint(0,len(Perk3)-1)]
        return self.perk3

    

    def primaryGunfighter1Funct(self):
        if self.primary == None   :
            a=random.randint(0,len(primaries)-1)
            b = primaries[a]
            c= random.randint(0,len(b)-1)
            self.primary = b[c]
        self.primaryAttachments = random.sample(attachments[self.primary], 3)
        return self.primary, self.primaryAttachments
    def primaryGunfighter2Funct (self):
        if len(attachments[self.primary])>=4:
            self.primaryAttachments=random.sample(attachments[self.primary], 4)
            return self.primaryAttachments
        else:
            print("ERROR ERROR ERROR NOT ENOUGH ATTACHMENTS")
    def primaryGunfighter3Funct (self):
        if len(attachments[self.primary])>=5:
            return random.sample(attachments[self.primary], 5)
        else:
            print("ERROR ERROR ERROR NOT ENOUGH ATTACHMENTS")
            
    
    
    def secondaryGunfighter1Funct (self):
        if self.secondary == None:
            a=random.randint(0,len(secondaries)-1)
            b = secondaries[a]
            c= random.randint(0,len(b)-1)
            self.secondary = b[c]
        self.secondaryAttachments = random.sample(attachments[self.secondary], 3)
        return self.secondary, self.secondaryAttachments
    def secondaryGunfighter2Funct (self):
        self.secondaryAttachments = random.sample(attachments[self.secondary], 4)
        return self.secondary, self.secondaryAttachments
    def secondaryGunfighter3Funct (self):
        self.secondaryAttachments = random.sample(attachments[self.secondary], 5)
        return self.secondary, self.secondaryAttachments
    
    def perk1GluttonyFunct(self):
        global Perk1
        gluts1 = random.sample(Perk1, 3)
        self.perk1 = gluts1[0]
        self.perk2 = gluts1[1]
        self.perk3 = gluts1[2]
        Perk1 = [u for u in Perk1 if u not in gluts1]
        return [self.perk1, self.perk2, self.perk3]
        
    def perk2GluttonyFunct(self):
        global Perk2
        gluts2=random.sample(Perk2,3)
        self.perk1=gluts2[0]
        self.perk2=gluts2[1]
        self.perk3=gluts2[2]
        Perk2 = [u for u in Perk2 if u not in gluts2]
        return [self.perk1, self.perk2, self.perk3]
    
    def perk3GluttonyFunct(self):
        global Perk3
        gluts3=random.sample(Perk3,3)
        self.perk1=gluts3[0]
        self.perk2=gluts3[1]
        self.perk3=gluts3[2]
        Perk3=[u for u in Perk3 if u not in gluts3]
        return [self.perk1, self.perk2, self.perk3]
    
    def perk1GreedFunct(self):
        global Perk1
        if self.perk1 == []:
            self.perk1=random.sample(Perk1,2)
        else:
            random1 = randint(0, len(Perk1)-1)
            self.perk1 = self.perk1 + 'and ' + (Perk1[random1])
        return self.perk1
    def perk2GreedFunct(self):
        global Perk2
        if self.perk2 == []:
            self.perk2=random.sample(Perk2,2)
        else:
            random2 = randint(0, len(Perk2)-1)
            self.perk2 = self.perk2 + 'and ' + (Perk2[random2])
        return self.perk2
    def perk3GreedFunct(self):
        global Perk3
        if self.perk3 == []:
            self.perk3=random.sample(Perk3,2)
        else:
            random3 = randint(0, len(Perk3)-1)
            self.perk3 = self.perk3 + 'and ' + (Perk3[random3])
        return self.perk3
    
    
        

        
    


    
# Your initial condition block
###if any(element in chosenWildcards for element in ['Primary Gunfighter 1', 'Primary Operator Mod']):
   # loadout1 = loadout(chosenWildcards)
    #print(loadout1.primaryFunct(pick10))
    
#if 'Primary Gunfighter 2' in chosenWildcards:
    


    
#if any(element in chosenWildcards for element in ['Underkill'])
    
#if 'Perk 1 Greed' in chosenWildcards:
    #perks.append[]
loadout1 = loadout()
    
for wildcard in chosenWildcards:
    method_name = wildcard_methods[wildcard]
    method = getattr(loadout1, method_name)
    result = method()
    print(f'Result of {wildcard}: {result}')
print('')
print('')   
#print(loadout1.primary, loadout1.primaryAttachments, loadout1.secondary, loadout1.secondaryAttachments, loadout1.perk1, loadout1.perk2, loadout1.perk3)
#print(loadout1.overkillFunct())
#print(loadout1.underkillFunct())
#print(loadout1.primaryGunfighter1Funct())
#print(loadout1.primaryGunfighter2Funct())
#print(loadout1.primaryGunfighter3Funct())
#print(loadout1.secondaryGunfighter1Funct())
#print(loadout1.secondaryGunfighter2Funct())
#print(loadout1.secondaryGunfighter3Funct())
#print(loadout1.perk1GluttonyFunct())
#print(loadout1.perk2GluttonyFunct())
#print(loadout1.perk3GluttonyFunct())
#print(loadout1.perk1GreedFunct())
#print(loadout1.perk2GreedFunct())
#print(loadout1.perk3GreedFunct())
#print(loadout1.scorestreaksFunct(streaks))
#print(loadout1.specialistFunct(specialists))
#print(loadout1.secondaryFunct(pick10))
#print(loadout1.gearFunct(pick10))
#print(loadout1.perk1Funct(pick10))
#print(loadout1.perk2Funct(pick10))
#print(loadout1.perk3Funct(pick10))
#print(loadout1.primaryOperatorModFunct())
#print(loadout1.gearFunct())
print('')
print('')
#print(f'Your primary weapon is the {chosenPrimary}')
#print(f'Your secondary is the {chosenSecondary}')
#print(f'Your gear is the {chosenGear}')
#print(f'Your perks are {chosenPerk1}, {chosenPerk2}, and {chosenPerk3}')
#print(f'Your equipment is {amount} {chosenEquipment}')

print('')
print('')
print(pick10)

class rcg:
    
    def __init__(self, loadout):
       
        self.loadout = loadout
    
        self.primary = self.loadout.primary
        self.primaryAttachments = self.loadout.primaryAttachments
        self.primaryOptic = None
        self.secondary = self.loadout.secondary
        self.secondaryAttachments = self.loadout.secondaryAttachments
        self.secondaryOptic = None
        self.gear = None
        self.equipment = None
        self.perk1 = self.loadout.perk1
        self.perk2 = self.loadout.perk2
        self.perk3 = self.loadout.perk3
        self.specialist = self.loadout.specialist
        self.scorestreaks = self.loadout.scorestreaks
        self.operatorMod1 = self.loadout.operatorMod1
        self.operatorMod2 = self.loadout.operatorMod2
        
    def equipmentFunct(self, pick10):
        if pick10 == 0:
            self.equipment = None
        if pick10 == 1:
            amount=1
            equipment = ['Trophy System', 'Combat Axe', 'Frag', 'Molotov', 'Concussion']
            self.equipment = equipment[random.randint(0,len(equipment)-1)]
            pick10 -= amount
        if pick10 >1:
            amount=0
            equipment = ['Trophy System', 'Combat Axe', 'Frag', 'Molotov', 'Concussion']
            self.equipment = equipment[random.randint(0,len(equipment)-1)]
            if self.equipment in ('Trophy System','Combat Axe','Concussion'):
                amount = random.randint(1,2) 
            else:
                amount = 1
            pick10 -= amount
            self.equipment = f'{amount} {self.equipment}'
            if amount==2:
                self.equipment += 's'
        return self.equipment, pick10
    
    def gearFunct(self,pick10):
        if pick10>=1:
            self.gear = random.choice(gear)
            pick10 -= 1
        return self.gear, pick10
        
    def primaryFunct(self,pick10):
        if self.loadout.primary == None:
            if pick10 >0:
                a=random.randint(0,len(primaries)-1)
                b = primaries[a]
                c= random.randint(0,len(b)-1)
                self.primary = b[c]
                pick10 -=1
        return self.primary, pick10
    
    def secondaryFunct(self,pick10):
        if self.secondary == None:
            if pick10>0:
                d=random.randint(0,len(secondaries)-1)
                e= secondaries[d]
                f = random.randint(0, len(e)-1)
                self.secondary = e[f]
                pick10-=1
        return self.secondary, pick10
    
    def primaryOpticFunct (self,pick10):
        if self.primary in ('Ballistic Knife', 'Combat Knife'):
            pick10 = pick10
            return self.primaryOptic, pick10
        if self.primary == None:
            if pick10>=2:
                a=random.randint(0,len(primaries)-1)
                b = primaries[a]
                c= random.randint(0,len(b)-1)
                self.primary = b[c]
                self.primaryOptic = random.choice(optics[self.primary])
                pick10 -=2
        else: 
            if pick10>=1:
                self.primaryOptic = random.choice(optics[self.primary])
                pick10 -=1
        
        return self.primaryOptic, pick10
    
    def secondaryOpticFunct (self,pick10):
        if self.secondary in ('Ballistic Knife', 'Combat Knife'):
            pick10 = pick10
            return self.secondaryOptic, pick10
        if self.secondary == None:
            if pick10>=2:
                a=random.randint(0,len(secondaries)-1)
                b = secondaries[a]
                c= random.randint(0,len(b)-1)
                self.secondary = b[c]
                self.secondaryOptic = random.choice(optics[self.secondary])
                pick10 -=2
        else:
            if pick10>=1:
                self.secondaryOptic = random.choice(optics[self.secondary])
                pick10 -=1
        return self.secondaryOptic, pick10
    
    def primaryAttachmentsFunct (self,pick10):
        if self.primary == 'Combat Knife':
            self.primaryAttachments = None
            return self.primary, self.primaryAttachments, self.primaryOptic, pick10
        if self.primary == None:
            if pick10 >=3:
                a=random.randint(0,len(primaries)-1)
                b = primaries[a]
                c= random.randint(0,len(b)-1)
                self.primary = b[c]
                self.primaryAttachments = random.sample(attachments[self.primary], 2)
                pick10 -=3
            elif pick10 >= 2:
                a=random.randint(0,len(primaries)-1)
                b = primaries[a]
                c= random.randint(0,len(b)-1)
                self.primary = b[c]
                self.primaryAttachments = random.choice(attachments[self.primary])
                pick10 -=2
        else:
            if pick10 >=2: 
                self.primaryAttachments = random.sample(attachments[self.primary], 2)
                pick10 -=2
            elif pick10 >=1:
                self.primaryAttachments = random.choice(attachments[self.primary])
                pick10 -=1
        return self.primary, self.primaryAttachments, self.primaryOptic, pick10
    
    def secondaryAttachmentsFunct (self,pick10):
        if self.secondary == 'Combat Knife':
            self.secondaryAttachments = None
            return self.secondary, self.secondaryAttachments, self.secondaryOptic, pick10
        if self.secondary == None:
            if pick10 >=3:
                a=random.randint(0,len(secondaries)-1)
                b = secondaries[a]
                c= random.randint(0,len(b)-1)
                self.secondary = b[c]
                self.secondaryAttachments = random.sample(attachments[self.secondary], 2)
                pick10 -=3
            elif pick10 >= 2:
                a=random.randint(0,len(secondaries)-1)
                b = secondaries[a]
                c= random.randint(0,len(b)-1)
                self.secondary = b[c]
                self.secondaryAttachments = random.choice(attachments[self.secondary])
                pick10 -=2
        else:
            if pick10 >=2: 
                self.secondaryAttachments = random.sample(attachments[self.secondary], 2)
                pick10 -=2
            elif pick10 >=1:
                self.primaryAttachments = random.choice(attachments[self.secondary])
                pick10 -=1
        return self.secondary, self.secondaryAttachments, self.secondaryOptic, pick10
    
    def perk1Funct (self,pick10):
        if self.perk1 == None:
            if pick10>=1:
                self.perk1 = Perk1[random.randint(0,len(Perk1)-1)]
                pick10 -=1
        return self.perk1, pick10
    
    def perk2Funct (self,pick10):
        if self.perk2 == None:
            if pick10>= 1:
                self.perk2 = Perk2[random.randint(0,len(Perk2)-1)]
                pick10 -=1
        return self.perk2, pick10
    
    def perk3Funct (self,pick10):
        if self.perk3 == None:
            if pick10>= 1:
                self.perk3 = Perk3[random.randint(0,len(Perk3)-1)]
                pick10 -=1
        return self.perk3, pick10
    
#print(loadout1.rcg())

print('                          ')
print('                          ')
jake_rcg = rcg(loadout1)

print(f' Before Etoffement: {pick10}')

print('')
print('')

import random
import random

def spendRemainingPick10(rcg_obj, pick10):
    slots = [
        'primary', 'secondary', 'primaryOptic', 'secondaryOptic',
        'primaryAttachments', 'secondaryAttachments',
        'perk1', 'perk2', 'perk3',
        'gear', 'equipment'
    ]

    made_progress = True

    while pick10 > 0 and made_progress:
        made_progress = False  
        random.shuffle(slots)  

        for slot in slots:
            if pick10 <= 0:
                break

            current_value = getattr(rcg_obj, slot)
            if current_value not in (None, [], ''):
                continue  

            before = pick10
            print(f"Spending pick10 on {slot}...")

            if slot in ('perk1', 'perk2', 'perk3'):
                setattr(rcg_obj, slot, random.choice(eval(slot.capitalize())))
                pick10 -= 1

        
            elif slot in ('primaryAttachments', 'secondaryAttachments'):
                weapon_attr = slot.replace('Attachments', '')
                weapon = getattr(rcg_obj, weapon_attr)

                if weapon in (None, 'Combat Knife'):
                    print(f"Skipped {slot} — no valid weapon.")
                    continue

                max_attachments = min(2, pick10)
                num_attachments = random.randint(1, max_attachments)
                chosen_attachments = random.sample(attachments[weapon], num_attachments)
                setattr(rcg_obj, slot, chosen_attachments)
                pick10 -= num_attachments

            elif slot in ('primaryOptic', 'secondaryOptic'):
                weapon_attr = slot.replace('Optic', '')
                weapon = getattr(rcg_obj, weapon_attr)

                if weapon in (None, 'Combat Knife', 'Ballistic Knife'):
                    print(f"Skipped {slot} — invalid weapon for optic.")
                    continue

                setattr(rcg_obj, slot, random.choice(optics[weapon]))
                pick10 -= 1

            elif slot in ('primary', 'secondary'):
                weapon_groups = primaries if slot == 'primary' else secondaries
                weapon_list = random.choice(weapon_groups)
                weapon = random.choice(weapon_list)
                setattr(rcg_obj, slot, weapon)
                pick10 -= 1

            elif slot == 'gear':
                chosen_gear = random.choice(gear)
                setattr(rcg_obj, slot, chosen_gear)
                pick10 -= 1

            elif slot == 'equipment':
                items = ['Trophy System', 'Combat Axe', 'Frag', 'Molotov', 'Concussion']
                item = random.choice(items)

                if item in ('Trophy System', 'Combat Axe', 'Concussion'):
                    amount = random.randint(1, min(2, pick10))
                else:
                    amount = 1

                equipment_text = f"{amount} {item}" + ("s" if amount == 2 else "")
                setattr(rcg_obj, slot, equipment_text)
                pick10 -= amount

            # Track progress 
            if pick10 < before:
                made_progress = True
                print(f"Remaining pick10 points: {pick10}\n")

        # Safety check s
        if not made_progress:
            print("No progress made this round — stopping loop.")
            break

    return rcg_obj, pick10


def generate_class():

    jake_rcg = rcg(loadout1)

    jake_rcg.primaryGunfighter1Funct()
    jake_rcg.primaryGunfighter2Funct()
    jake_rcg.primaryGunfighter3Funct()

    jake_rcg.secondaryFunct()

    jake_rcg.perk1Funct()
    jake_rcg.perk2Funct()
    jake_rcg.perk3Funct()

    jake_rcg.gearFunct()

    chosenWildcards = jake_rcg.wildcardList
    chosenScorestreaks = jake_rcg.scorestreakList

    return {
        "Primary Weapon": jake_rcg.primary,
        "Primary Attachments": jake_rcg.primaryAttachments,
        "Secondary Weapon": jake_rcg.secondary,
        "Perk 1": jake_rcg.perk1,
        "Perk 2": jake_rcg.perk2,
        "Perk 3": jake_rcg.perk3,
        "Gear": jake_rcg.gear,
        "Wildcards": chosenWildcards,
        "Scorestreaks": chosenScorestreaks
    }



# Example usage:
print('')
jake_rcg, pick10 = spendRemainingPick10(jake_rcg, pick10)
print(f" after Etoffement: {pick10}")


    
#primaryResult, pick10 = jake_rcg.primaryFunct(pick10)
#print(primaryResult, pick10)

#secondaryResult, pick10 = jake_rcg.secondaryFunct(pick10)
#print(secondaryResult, pick10)


#primaryOptic, pick10 = jake_rcg.primaryOpticFunct(pick10)
#print(primaryOptic, pick10)

#secondaryOptic, pick10 = jake_rcg.secondaryOpticFunct(pick10)
#print(secondaryOptic,pick10)


#equipmentResult, pick10 = jake_rcg.equipmentFunct(pick10)
#print(equipmentResult, pick10)

#selectedGear, pick10 = jake_rcg.gearFunct(pick10)
#print(selectedGear, pick10)

#primaryResult, primaryAttachmentList, primaryOptic, pick10 = jake_rcg.primaryAttachmentsFunct(pick10)
#print(primaryResult, primaryAttachmentList, primaryOptic, pick10)

#secondaryResult, secondaryAttachmentList, secondaryOptic, pick10 = jake_rcg.secondaryAttachmentsFunct(pick10)
#print(secondaryResult, secondaryAttachmentList, secondaryOptic, pick10)
        
#Perc1GANG, pick10 = jake_rcg.perk1Funct(pick10)
#print(Perc1GANG, pick10)

#Perc2GANG, pick10 = jake_rcg.perk2Funct(pick10)
#print(Perc2GANG, pick10)

#Perc3GANG, pick10 = jake_rcg.perk3Funct(pick10)
#print(Perc3GANG, pick10)




        #MIGHT STILL HAVE ISSUE WITH pick10 GETTING ADDED 1 INCORRECTLY WITH WILDCARDS
        #SECONDARIES WITHOHUT ENOUGH ATTACHMENTS/KNIFE DON'T WORK WITH ATTACHMENTS
        #ORDER OF WILDCARDS IS MESSED UP, UNDERKILL OVERWRITES PRIMARY OPERATOR MOD
        #NO OPTICS ARE RETURNING AT ALL!
        

print('                                 ')
print('                                 ')
print('                                 ')
print('                                 ')


print(f'Specialist: {chosenSpecialist} \n')

print(f'Primary: {jake_rcg.primary} \n    Optic: {jake_rcg.primaryOptic} \n    Attachments: {jake_rcg.primaryAttachments} \n    Operator Mod: {jake_rcg.operatorMod1}')
print('                                 ')
print(f'Secondary: {jake_rcg.secondary} \n    Optic: {jake_rcg.secondaryOptic} \n    Attachments: {jake_rcg.secondaryAttachments} \n    Operator Mod: {jake_rcg.operatorMod2}')   
print('                                 ') 
print(f'Gear: {jake_rcg.gear}')
print('')
print(f'Equipment: {jake_rcg.equipment}')
print('')
print(f'Perk 1: {jake_rcg.perk1}')
print(f'Perk 2: {jake_rcg.perk2}')
print(f'Perk 3 : {jake_rcg.perk3}')
print('')
print(f'Wildcards: {chosenWildcards}')        
print(f'Scorestreaks: {chosenScorestreaks}')

#########################################     BUGS     ################################################33
# no other class needed just need to feed class named rcg



#Infinite Looping
#ValueError: sample larger than population or is negative in [183] line 570 result = method(), in line 482 in secondaryGunfighter1Funct self.secondaryAttachments = random.sample(attachments{self.secondary],3)
#If you get perk 1 greed then gluttony, it will just do 3 perks instead of 3 and then the 4th being in the original perk number
#Primary/secondary gunfighter 2 and 3 don't need to adjust pick 10 by one because their value is already 2 instead of 3 like gunfighter 1.
#Pick10 gets inflated when two synergistic wildcards are selected, but pick10 is not big enough to accommodate the second wildcard - it keeps the plus 1 though.