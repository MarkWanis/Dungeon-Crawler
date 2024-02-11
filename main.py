'''
To-Do List:
Add floor 3
restock


Status Effects:
Poison - Damage every round
Fire - Damage reduction
Ice - Freeze
Electric - Paralyze
Pixie - Asleep


Armor Tiers:
Rusted
Chainmail
Iron 
Diamond
Mythril
Ancient


Sword Tiers:
Broken
Sharpened
Steel
Diamond
Mythril
Ancient

'''

import time
import random
import math

#########################################################
#Colors
#########################################################

red = "\033[0;31m"
green = "\033[0;32m"
brightYellow = "\033[0;93m"
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
invisible='\033[08m'
reverse='\033[07m'
reset='\033[0m'

################################################################################
#Global Variables
################################################################################

shopItems = {
    "Quantity": {
        "Poison Powder": 100,
        "Sleep Powder": 100,
        "Raw Meat": 10,
        "Slightly Cooked Meat": 5,
        "Frost Powder": 100,
        "Steak": 5,
        "Phoenix Powder": 100,
    },
    "Cost": {
        "Poison Powder": 2,
        "Sleep Powder": 2,
        "Raw Meat": 3,
        "Slightly Cooked Meat": 7,
        "Frost Powder": 5,
        "Steak": 15,
        "Phoenix Powder": 5,
    }
}


shopEquipment = {
    "Quantity": {
        "Sharpened Sword": 1,
        "Chainmail Helmet": 1,
        "Chainmail Chestplate": 1,
        "Chainmail Leggings": 1,
        "Chainmail Boots": 1,
        "Steel Sword": 1,
        "Iron Helmet": 1,
        "Iron Chestplate": 1,
        "Iron Leggings": 1,
        "Iron Boots": 1
    },
    "Cost": {
        "Sharpened Sword": 8,
        "Chainmail Helmet": 4,
        "Chainmail Chestplate": 8,
        "Chainmail Leggings": 6,
        "Chainmail Boots": 4,
        "Steel Sword": 20,
        "Iron Helmet": 16,
        "Iron Chestplate": 20,
        "Iron Leggings": 18,
        "Iron Boots": 16
    }
}


equipmentStats = {
    "Cracked Sword": 2,
    "Rusted Helmet": 1,
    "Rusted Chestplate": 2,
    "Rusted Leggings": 2,
    "Rusted Boots": 1,
    "Sharpened Sword": 5,
    "Chainmail Helmet": 3,
    "Chainmail Chestplate": 5,
    "Chainmail Leggings": 4,
    "Chainmail Boots": 3,
    "Steel Sword": 11,
    "Iron Helmet": 9,
    "Iron Chestplate": 11,
    "Iron Leggings": 10,
    "Iron Boots": 9
}
    
    
userStats = {
    "Sword": "Cracked Sword",
    "Attack Damage": 2,
    "Level": 1,
    "EXP": 0,
    "Helmet": "Rusted Helmet",
    "Chestplate": "Rusted Chestplate",
    "Leggings": "Rusted Leggings",
    "Boots": "Rusted Boots",
    "Gold": 10,
    "Max Health": 18,
    "Current Health": 18,
    "Status": "None"
}


userBag = {
    "Poison Powder": 2,
    "Sleep Powder": 2,
    "Raw Meat": 2,
    "Slightly Cooked Meat": 0,
    "Frost Powder": 0,
    "Steak": 0,
    "Phoenix Powder": 0,
}


userEquipment = {
    "Broken Sword": 1,
    "Rusted Helmet": 1,
    "Rusted Chestplate": 1,
    "Rusted Leggings": 1,
    "Rusted Boots": 1,
    "Sharpened Sword": 0,
    "Chainmail Helmet": 0,
    "Chainmail Chestplate": 0,
    "Chainmail Leggings": 0,
    "Chainmail Boots": 0,
    "Steel Sword": 0,
    "Iron Helmet": 0,
    "Iron Chestplate": 0,
    "Iron Leggings": 0,
    "Iron Boots": 0
}


unlockedItems = {
    "Shop": ["Poison Powder", "Sleep Powder", "Raw Meat", "Slightly Cooked Meat"],
    "Bag": ["Poison Powder", "Sleep Powder", "Raw Meat", "Slightly Cooked Meat", "Steak"]
}


unlockedEquipment = {
    "Shop": ["Sharpened Sword", "Chainmail Helmet", "Chainmail Chestplate", "Chainmail Leggings", "Chainmail Boots"],
    "Bag": ["Cracked Sword", "Rusted Helmet", "Rusted Chestplate", "Rusted Leggings", "Rusted Boots", "Sharpened Sword", "Chainmail Helmet", "Chainmail Chestplate", "Chainmail Leggings", "Chainmail Boots"]
}


healingItems = {
    "Raw Meat": 3,
    "Slightly Cooked Meat": 7,
    "Steak": 15
}


statusItems = {
    "Poison Powder": "Poison",
    "Sleep Powder": "Pixie",
    "Frost Powder": "Ice",
    "Phoenix Powder": "Fire"
}


enemyTypes = {
    "Floor 1": {
        "Normal": 7,
        "Rock": 1,
        "Electric": 1,
        "Fire": 1
    },
    "Floor 2": {
        "Normal": 1,
        "Rock": 2,
        "Electric": 1,
        "Fire": 3,
        "Ice": 1,
        "Poison": 1,
        "Pixie": 1
    },
}


armor = ["Rusted Helmet", "Rusted Chestplate", "Rusted Leggings", "Rusted Boots", "Chainmail Helmet", "Chainmail Chestplate", "Chainmail Leggings", "Chainmail Boots", "Iron Helmet", "Iron Chestplate", "Iron Leggings", "Iron Boots"]

################################################################################
#Helper Functions
################################################################################
    
#This function checks if the value passed is between the min and max (max inclusive)
def validNumber(value, min, max):
    if value.isdigit() == False:
        slowPrint("\nThat is not a number!")
        return False
    
    if int(value) not in range(min, max + 1):
        slowPrint("\nThat number is not in the specified range!")
        return False
        
    return True
    
#This function returns who is alive - "Both", "Player", "Enemy"
def bothAlive(playerHealth, enemyHealth):
    if playerHealth <= 0:
        slowPrint("\nOh no! You've been defeated by the enemy! After you awake from unconsciousness, you find yourself in the same place you were before you discovered the enemy.")
        return "Enemy"
        
    if enemyHealth <= 0:
        slowPrint("\nYou've defeated the enemy!")
        return "Player"
        
    return "Both"
    
#This function heals the given health the given amount
def heal(currentHealth, maxHealth, healAmount):
    currentHealth += healAmount
    if currentHealth > maxHealth:
        currentHealth = maxHealth
    return currentHealth
    
#This resets the player current health and status back to normal
def resetPlayerStats():
    userStats["Current Health"] = userStats["Max Health"]
    userStats["Status"] = "None"
    
#This funtion looks at the given status and status counter to see if the turn should be skipped
def checkSkipTurn(status, statusCounter, name):
    if status != "Asleep" and status != "Frozen" and status != "Paralyzed":
        return [False, status]

    randomNum = random.randint(1, 100)
    
    if status == "Asleep":
        if statusCounter == 0 and randomNum <= 25:
            if name == "Player":
                slowPrint("\nYou woke up!")
            else:
                slowPrint("\nThe enemy woke up!")
            return [False, "None"]
    
        elif statusCounter == 1 and randomNum <= 50:
            if name == "Player":
                slowPrint("\nYou woke up!")
            else:
                slowPrint("\nThe enemy woke up!")
            return [False, "None"]
    
        elif statusCounter >= 2:
            if name == "Player":
                slowPrint("\nYou woke up!")
            else:
                slowPrint("\nThe enemy woke up!")
            return [False, "None"]
    
        if name == "Player":
            slowPrint("\nYou are fast asleep!")
        else:
            slowPrint("\nThe enemy is fast asleep!")
    
    elif status == "Frozen":
        if randomNum <= 40:
            if name == "Player":
                slowPrint("\nYou are unfrozen!")
            else:
                slowPrint("\nThe enemy is unfrozen!")
            return [False, "None"]
        
        if name == "Player":
            slowPrint("\nYou are frozen and unable to move!")
        else:
            slowPrint("\nThe enemy is frozen and unable to move!")
    
    elif status == "Paralyzed":
        if randomNum <= 25:
            if name == "Player":
                slowPrint("\nYou are paralyzed and unable to move!")
            else:
                slowPrint("\nThe enemy is paralyzed and unable to move!")
    
        else:
            return [False, status]
    
    return [True, status]
    
#This function randomly choosed one enemy type out of the given types
def chooseEnemyType(floor):
    randomNum = random.randint(1, sum(enemyTypes[floor].values()))
    
    for keyElement in [*enemyTypes[floor]]: #Iterates through all enemy types on the floor
        if randomNum <= enemyTypes[floor][keyElement]: #Returns enemy type if randomNum>=value at the given enemy type
            return keyElement
        randomNum -= enemyTypes[floor][keyElement] #Subtracts the value if it is not
    
#This function restocks the shop to its original quantity
def restockShop():
    shopItems = {
        "Quantity": {
            "Poison Powder": 100,
            "Sleep Powder": 100,
            "Raw Meat": 10,
            "Slightly Cooked Meat": 5,
            "Frost Powder": 100,
            "Steak": 5,
            "Phoenix Powder": 100,
        },
        "Cost": {
            "Poison Powder": 2,
            "Sleep Powder": 2,
            "Raw Meat": 3,
            "Slightly Cooked Meat": 7,
            "Frost Powder": 5,
            "Steak": 15,
            "Phoenix Powder": 9,
        }
    }
    
################################################################################
#Evaluate Functions
################################################################################

#This function evaluates attack damage and health
def evaluateStats():
    evaluateHealth()
    userStats["Attack Damage"] = equipmentStats[userStats["Sword"]]
    
#This function adds the given exp to the player's exp and checks if they level up
def evaluateLevel(exp):
    userStats["EXP"] += exp
    
    while userStats["EXP"] >= (userStats["Level"]**2 + 9):
        slowPrint("\nYou leveled up!")
        userStats["EXP"] -= userStats["Level"]**2 + 9
        userStats["Level"] += 1
        evaluateHealth()
        slowPrint(f"\nYour Max Health: {userStats['Max Health']}")
        
#This function takes the given base damage and returns the adjusted amount
def determineDamage(baseDamage, status):
    randNum = random.randint(1, 20)
    
    if randNum == 1:
        slowPrint("\nThe attack missed!")
        return 0
        
    if randNum >= 19:
        slowPrint("\nCritical Hit!")
        baseDamage = baseDamage * 2
        
    if status == "Burned":
        baseDamage /= baseDamage
        
    return round(baseDamage)
    
#This function evaluates how much health the user has
def evaluateHealth():
    userStats["Max Health"] =  10 + equipmentStats[userStats["Helmet"]] + equipmentStats[userStats["Chestplate"]] + equipmentStats[userStats["Leggings"]] + equipmentStats[userStats["Boots"]] + 2 * userStats["Level"]
    userStats["Current Health"] =  10 + equipmentStats[userStats["Helmet"]] + equipmentStats[userStats["Chestplate"]] + equipmentStats[userStats["Leggings"]] + equipmentStats[userStats["Boots"]] + 2 * userStats["Level"]
    
################################################################################
#Print Functions
################################################################################

#This function prints the given string slowly
def slowPrint(string):
    for char in string:
        print(char, end='', flush=True)
        time.sleep(.005)
    print()
    
#This prints the options for the dungeon floor
def printDungeonFloorOptions():
    slowPrint("\nYour Options:\n\n1) Go to Shop\n2) Continue through Dungeon\n3) Fight the Boss")    
    
#This prints the equipment for the shop
def printShopEquipment():
    slowPrint("\nYour Options:\n\n0) Exit Equipment Shop")
    for index, equipment in enumerate(unlockedEquipment["Shop"]):
        slowPrint(f"{index + 1}) {equipment}: {shopEquipment['Quantity'][equipment]}")
        slowPrint(f"   Cost: {shopEquipment['Cost'][equipment]}")
        if "Sword" in equipment:
            slowPrint(f"   Attack Damage: {equipmentStats[equipment]}")
        elif equipment in armor:
            slowPrint(f"   Defense: {equipmentStats[equipment]}")
            
#This prints the items for the shop
def printShopItems():
    slowPrint("\nYour Options:\n\n0) Exit Item Shop")
    for index, item in enumerate(unlockedItems["Shop"]):
        slowPrint(f"{index + 1}) {item}: {shopItems['Quantity'][item]}")
        slowPrint(f"   Cost: {shopItems['Cost'][item]}")
        
#This prints the options for the shop
def printShopOptions():
    slowPrint("\nYour Options:\n\n0) Exit Shop\n1) Items\n2) Equipment")
    
#This prints out the enemy's full stats
def printEnemyStats(stats):
    slowPrint(f"Max Health: {stats['Max Health']}")
    slowPrint(f"Attack Damage: {stats['Attack Damage']}")
    slowPrint(f"Type: {stats['Type']}")
    
#This prints out the player's full stats
def printPlayerStats():
    slowPrint(f"\nMax Health: {userStats['Max Health']}")
    slowPrint(f"{userStats['Sword']}: {equipmentStats[userStats['Sword']]} Attack Damage")
    slowPrint(f"{userStats['Helmet']}: {equipmentStats[userStats['Helmet']]} Defense")
    slowPrint(f"{userStats['Chestplate']}: {equipmentStats[userStats['Chestplate']]} Defense")
    slowPrint(f"{userStats['Leggings']}: {equipmentStats[userStats['Leggings']]} Defense")
    slowPrint(f"{userStats['Boots']}: {equipmentStats[userStats['Boots']]} Defense")
    slowPrint(f"Poison Powder: {userBag['Poison Powder']}")
    slowPrint(f"Sleep Powder: {userBag['Sleep Powder']}")
    slowPrint(f"Total Gold: {userStats['Gold']}")
   
#This prints out the given person's health and status 
def printHealthStatus(currentHealth, maxHealth, status):
    if (currentHealth / maxHealth) >= (2 / 3):
        slowPrint(f"\nHealth: {green}{currentHealth}{reset} / {maxHealth}")

    elif (currentHealth / maxHealth) >= (1 / 3):
        slowPrint(f"\nHealth: {brightYellow}{currentHealth}{reset} / {maxHealth}")

    elif (currentHealth / maxHealth) < (1 / 3):
        slowPrint(f"\nHealth: {red}{currentHealth}{reset} / {maxHealth}")

    slowPrint(f"Status: {status}")
    
#This function prints out the user's bag
def printBag():
    slowPrint("\nYour Bag: \n")
    slowPrint("0) Exit Bag")
    for index, item in enumerate(unlockedItems["Bag"]):
        slowPrint(f"{index + 1}) {item}: {userBag[item]}")
        
#This function prints out the user's fight options   
def printFightOptions():
    slowPrint("\nYour Options:\n\n1) Attack\n2) Open Bag\n3) Run Away")
        
################################################################################
#Game Functions
################################################################################

#This function starts a fight with the given enemy
def enemyFight(enemyStats):
    printEnemyStats(enemyStats)
    
    playerStatusCounter = 0
    enemyStatusCounter = 0
    
    while True: #Continues fight until one person dies
        #Player's Turn
        printFightOptions()
        slowPrint("\nSelect an option: ")
        userChoice = input("")
        
        if not validNumber(userChoice, 1, 3):
            continue
        
        userChoice = int(userChoice)
        
        #Checks for status turn skip for player
        playerSkipTurn, userStats["Status"] = checkSkipTurn(userStats["Status"], playerStatusCounter, "Player")
        
        if not playerSkipTurn:
            if userChoice == 1: #Attack
                slowPrint("\nYou attacked the enemy!")
                attackDamage = determineDamage(userStats["Attack Damage"], userStats["Status"])
                slowPrint(f"\nYou did {attackDamage} damage!")
                enemyStats["Current Health"] -= attackDamage
                
            elif userChoice == 2: #Open Bag
                userChoice = openBag(enemyStats)
                
                if not userChoice:
                    continue
                
                if userChoice == "Poison Powder":
                    slowPrint("\nYou used Poison Powder.\n\nThe enemy was poisoned!")
                    enemyStats["Status"] = "Poisoned"
                    enemyStatusCounter = 0
                    
                elif userChoice == "Sleep Powder": 
                    slowPrint("\nYou used Sleep Powder.\n\nThe enemy fell asleep!")
                    enemyStats["Status"] = "Asleep"
                    enemyStatusCounter = 0
                    
                elif userChoice == "Frost Powder": 
                    slowPrint("\nYou used Frost Powder.\n\nThe enemy was frozen!")
                    enemyStats["Status"] = "Frozen"
                    enemyStatusCounter = 0
                    
                elif userChoice == "Phoenix Powder": 
                    slowPrint("\nYou used Phoenix Powder.\n\nThe enemy was burned!")
                    enemyStats["Status"] = "Burned"
                    enemyStatusCounter = 0
                    
                elif userChoice in [*healingItems]:
                    slowPrint(f"\nYou used {userChoice}.\n\nYou were healed for {healingItems[userChoice]} damage!")
                    userStats["Current Health"] = heal(userStats["Current Health"], userStats["Max Health"], healingItems[userChoice])
                    
                else:
                    print("Enemy Fight Error 2")
                    
            elif userChoice == 3: #Run Away
                slowPrint("\nYou ran away.")
                resetPlayerStats()
                return "Ran Away"
                    
            else:
                print("Enemy Fight Error 1")
                
            #Checks if enemy died
            if bothAlive(userStats["Current Health"], enemyStats["Current Health"]) == "Player":
                resetPlayerStats()
                return "Won"
            
        #Enemy's Turn
        
        #Checks for status turn skip for enemy
        enemySkipTurn, enemyStats["Status"] = checkSkipTurn(enemyStats["Status"], enemyStatusCounter, "Enemy")
            
        if not enemySkipTurn:
            slowPrint("\nThe enemy attacked you!")
            attackDamage = determineDamage(enemyStats["Attack Damage"], enemyStats["Status"])
            slowPrint(f"\nThe enemy did {attackDamage} damage!")
            userStats["Current Health"] -= attackDamage
            
            #Checks if user died
            if bothAlive(userStats["Current Health"], enemyStats["Current Health"]) == "Enemy":
                resetPlayerStats()
                return "Lost"
                
        #Apply all of the enemy type statuses
        if enemyStats["Type"] == "Poison" and userStats["Status"] == "None": 
            if random.randint(1, 10) <= 2:
                slowPrint("\nYou were poisoned by the enemy's toxic barbs!")
                userStats["Status"] = "Poisoned"
        if enemyStats["Type"] == "Fire" and userStats["Status"] == "None":
            if random.randint(1, 10) <= 2:
                slowPrint("\nYou were engulfed by the enemy's flames!")
                userStats["Status"] = "Burned"
        if enemyStats["Type"] == "Ice" and userStats["Status"] == "None":
            if random.randint(1, 10) <= 2:
                slowPrint("\nYou were frozen by the enemy's chilling breath!")
                userStats["Status"] = "Frozen"
        if enemyStats["Type"] == "Pixie" and userStats["Status"] == "None":
            if random.randint(1, 10) <= 2:
                slowPrint("\nYou fell asleep from the enemy's magical pixie dust!")
                userStats["Status"] = "Asleep"
        if enemyStats["Type"] == "Electric" and userStats["Status"] == "None":
            if random.randint(1, 10) <= 2:
                slowPrint("\nYou were paralyzed by the enemy's shocks!")
                userStats["Status"] = "Paralyzed"
            
        #Status effect damages
        if userStats["Status"] == "Poisoned":
            userStats["Current Health"] -= round(userStats["Current Health"]/5)
            slowPrint("\nYou took some damage from the poison.")
        elif enemyStats["Status"] == "Poisoned":
            enemyStats["Current Health"] -= round(enemyStats["Current Health"]/5)
            slowPrint("\nThe enemy took some damage from the poison.")
            
        #This checks if anyone died by status effects
        if bothAlive(userStats["Current Health"], enemyStats["Current Health"]) == "Player":
            resetPlayerStats()
            return "Won"
        if bothAlive(userStats["Current Health"], enemyStats["Current Health"]) == "Enemy":
            resetPlayerStats()
            return "Lost"
            
        #Prints out health and status for both player and enemy
        slowPrint("\nYour Stats:")
        printHealthStatus(userStats["Current Health"], userStats["Max Health"], userStats["Status"])
        slowPrint("\nEnemy Stats:")
        printHealthStatus(enemyStats["Current Health"], enemyStats["Max Health"], enemyStats["Status"])
        
        #Increases status counter if there is a status
        if userStats["Status"] != "None":
            playerStatusCounter += 1
        if enemyStats["Status"] != "None":
            enemyStatusCounter += 1

#This function lets the user choose an item from their bag and returns the item they chose otherwise
def openBag(enemyStats):
    while True:
        printBag()
        slowPrint("\nSelect an item: ")
        itemChoice = input("")
        
        if not validNumber(itemChoice, 0, len(unlockedItems["Bag"])):
            continue
        
        if int(itemChoice) == 0:
            return False
            
        itemChoice = unlockedItems["Bag"][int(itemChoice) - 1]
            
        if userBag[itemChoice] < 1:
            slowPrint("\nYou ran out of that item!")
            continue
        
        if itemChoice in [*statusItems] and enemyStats["Status"] != "None":
            slowPrint("\nYou can't apply a second status condition onto the enemy!")
            continue
        
        if itemChoice in [*statusItems] and (statusItems[itemChoice] in enemyStats["Type"] or "Rock" in enemyStats["Type"]):
            slowPrint("\nThe enemy is immune to that status!")
            continue
        
        userBag[itemChoice] -= 1
        
        return itemChoice
        
#This function looks through the given list and rewards the player based off of it
def rewardPlayer(rewards):
    slowPrint("\nYour Rewards:\n")
    rewardNum = 1
    
    for keyElement in [*rewards["Items"]]: #Adds items
        itemsGained = 0
        
        for i in range(rewards["Items"][keyElement]["Amount"]): 
            randomNum = random.randint(1, 10)
            
            if randomNum <= rewards["Items"][keyElement]["Chance"]:
                userBag[keyElement] += 1
                itemsGained += 1
                
        if itemsGained > 0:
            slowPrint(f"{rewardNum}) {keyElement}: {itemsGained}")
            rewardNum += 1
            
    goldGained = 0
    
    for i in range(rewards["Gold"]["Amount"]): 
        randomNum = random.randint(1, 10)
        
        if randomNum <= rewards["Gold"]["Chance"]:
            userStats["Gold"] += 1
            goldGained += 1
            
    if goldGained > 0:
        slowPrint(f"{rewardNum}) Gold: {goldGained}")
        rewardNum += 1
                
                
    slowPrint(f"{rewardNum}) EXP: {rewards['EXP']}")
    evaluateLevel(rewards["EXP"])
    
#This function lets the player buy items and equipment
def shop():
    slowPrint("\nHello adventurer! What will you be buying today?")
    while True:
        printShopOptions()
        slowPrint("\nSelect an option: ")
        userChoice = input("")
        
        if not validNumber(userChoice, 0, 2):
            continue
        
        userChoice = int(userChoice)
        
        if userChoice == 0: #Exit shop
            break
            
        if userChoice == 1: #Item shop
            while True:
                slowPrint(f"\nTotal Gold: {userStats['Gold']}")
                printShopItems()
                slowPrint("\nSelect an item: ")
                itemChoice = input("")
                
                if not validNumber(itemChoice, 0, len(unlockedItems["Shop"])):
                    continue
                
                if int(itemChoice) == 0:
                    break
                
                itemChoice = unlockedItems["Shop"][int(itemChoice) - 1]
                
                if userStats["Gold"] < shopItems["Cost"][itemChoice]:
                    slowPrint("\nSorry mate! You don't have enough gold to buy that!")
                    continue
                
                if shopItems["Quantity"][itemChoice] <= 0:
                    slowPrint("\nSorry mate! I ran out of that!")
                    continue
                
                slowPrint(f"\nYou bought {itemChoice}.")
                userStats["Gold"] -= shopItems["Cost"][itemChoice]
                shopItems["Quantity"][itemChoice] -= 1
                userBag[itemChoice] += 1
                
        if userChoice == 2: #Equipment shop
            while True:
                slowPrint(f"\nTotal Gold: {userStats['Gold']}")
                printShopEquipment()
                slowPrint("\nSelect an equipment: ")
                equipmentChoice = input("")
                
                if not validNumber(equipmentChoice, 0, len(unlockedEquipment["Shop"])):
                    continue
                
                if int(equipmentChoice) == 0:
                    break
                
                equipmentChoice = unlockedEquipment["Shop"][int(equipmentChoice) - 1]
                
                if userStats["Gold"] < shopEquipment["Cost"][equipmentChoice]:
                    slowPrint("\nSorry mate! You don't have enough gold to buy that!")
                    continue
                
                if shopEquipment["Quantity"][equipmentChoice] <= 0:
                    slowPrint("\nSorry mate! I ran out of that!")
                    continue
                
                slowPrint(f"\nYou bought {equipmentChoice}.")
                userStats["Gold"] -= shopEquipment["Cost"][equipmentChoice]
                shopEquipment["Quantity"][equipmentChoice] -= 1
                userStats[equipmentChoice.split(" ")[-1]] = equipmentChoice
                userEquipment[equipmentChoice] = 1
                evaluateStats()
                
    slowPrint("\nYou left the shop.")

################################################################################
#Dungeon Floor 1
################################################################################
        
slowPrint("Hello adventurer. You wake up finding yourself in a dark, damp dungeon. You gather what items you can scavenge around you from the skeletons and look for a way out. You discover that your only option is to climb the dungeon floors and escape to the surface. Will you be able to make it? Only time will tell.")
slowPrint("\nStarting Items:")
printPlayerStats()

while True:
    printDungeonFloorOptions()
    slowPrint("\nSelect an option: ")
    userChoice = input("")
    
    if not validNumber(userChoice, 1, 3):
        continue
    
    userChoice = int(userChoice)

    if userChoice == 1: #Shop
        shop()
        
    elif userChoice == 2: #Dungeon
        enemyType = chooseEnemyType("Floor 1")
        slowPrint(f"\nYou encounter a ferocious {enemyType} Goblin!")
        slowPrint(f"\n{enemyType} Goblin's Stats:\n")
        if enemyFight({"Max Health": 10, "Current Health": 10, "Attack Damage": 3, "Status": "None", "Type": enemyType}) == "Won":
            rewardPlayer({
                "Items": {"Raw Meat": {"Chance": 7, "Amount": 3}, "Slightly Cooked Meat": {"Chance": 4, "Amount": 2}}, 
                "Gold": {"Chance": 8, "Amount": 4},
                "EXP": 4
            })
        
    elif userChoice == 3: #Boss
        slowPrint("\nYou walk into the ominious dark room and hear an unpleasant amount of bone crunching. You focus your eyes to they other side of the room and see a large, boisterous goblin busily devouring what seems to be the last adventurer who walked in here. You yell to him and in return he roars back with all of his might. 'You dare challenge me?' he bellows. 'You will soon regret that foolish decision!'")
        slowPrint("\nYou challenge the mighty Goblin King!")
        slowPrint("\nGoblin King's Stats:\n")
        if enemyFight({"Max Health": 50, "Current Health": 50, "Attack Damage": 5, "Status": "None", "Type": "Normal"}) == "Won":
            rewardPlayer({
                "Items": {"Raw Meat": {"Chance": 8, "Amount": 2}, "Slightly Cooked Meat": {"Chance": 8, "Amount": 4}, "Steak": {"Chance": 9, "Amount": 2}}, 
                "Gold": {"Chance": 7, "Amount": 20},
                "EXP": 20
            })
            slowPrint("\nWith the Goblin King defeated, you continue upward to the next level of the dungeon.")
            break
        
    else:
        print("Floor 1 Error")
        
################################################################################
#Dungeon Floor 2
################################################################################

unlockedItems["Shop"].extend(["Frost Powder", "Steak"])
unlockedItems["Bag"].extend(["Frost Powder", "Steak"])
unlockedEquipment["Shop"].extend(["Steel Sword", "Iron Helmet", "Iron Chestplate", "Iron Leggings", "Iron Boots"])
unlockedEquipment["Bag"].extend(["Steel Sword", "Iron Helmet", "Iron Chestplate", "Iron Leggings", "Iron Boots"])
restockShop()

slowPrint("\nOnce you climb the precarious ladder, you look around and see the same things you saw on the first floor. But one major thing stands out. In the distance, you see countless amounts of demons of several varieties. They don't look too friendly, so for now you stand back, but you know that you will need to confront them eventually.")
        
while True:
    printDungeonFloorOptions()
    slowPrint("\nSelect an option: ")
    userChoice = input("")
    
    if not validNumber(userChoice, 1, 3):
        continue
    
    userChoice = int(userChoice)

    if userChoice == 1: #Shop
        shop()
        
    elif userChoice == 2: #Dungeon
        enemyType = chooseEnemyType("Floor 2")
        slowPrint(f"\nYou encounter a terrifying {enemyType} Demon!")
        slowPrint(f"\n{enemyType} Demon's Stats:\n")
        if enemyFight({"Max Health": 20, "Current Health": 20, "Attack Damage": 7, "Status": "None", "Type": enemyType}) == "Won":
            rewardPlayer({
                "Items": {"Raw Meat": {"Chance": 5, "Amount": 2}, "Slightly Cooked Meat": {"Chance": 7, "Amount": 3}, "Steak": {"Chance": 4, "Amount": 2}}, 
                "Gold": {"Chance": 8, "Amount": 8},
                "EXP": 10
            })
        
    elif userChoice == 3: #Boss
        slowPrint("\nYou step into the dimly lit castle and pass by the barely lit sconces. You begin to approach a colossal double door and feel belittled by its prescence. The doors creak viciously as you push on them, and you see a demon sprawling across a throne. 'I see you have chosen death.' Her immense and unsettling voice reverberates across the empty walls. 'Such a pity to see another human go to waste.' She steps off her throne and grabs her pointed scepter. The battle starts.")
        slowPrint("\nDemon Queen's Stats:\n")
        if enemyFight({"Max Health": 70, "Current Health": 70, "Attack Damage": 12, "Status": "None", "Type": "Fire & Poison"}) == "Won":
            rewardPlayer({
                "Items": {"Raw Meat": {"Chance": 8, "Amount": 2}, "Slightly Cooked Meat": {"Chance": 8, "Amount": 4}, "Steak": {"Chance": 9, "Amount": 2}}, 
                "Gold": {"Chance": 7, "Amount": 20},
                "EXP": 20
            })
            slowPrint("\nWith the Demon Queen defeated, you continue upward to the next level of the dungeon.")
            break
        
    else:
        print("Floor 2 Error")