import turtle
import time
import random
#name = {"ATTACK","DEFENSE","SPEED","HEALTH"}
Bob = {"Name":"Bob","ATK":10,"DEF":6,"SP":7,"HP":100}
John = {"Name":"John","ATK":1,"DEF":8,"SP":5,"HP":100}

#turtle1 = turtle.Turtle()
base_damage = 10

choice = "blank"

def damage_calc(damage,attacker,defender): #used to register an attack
  print(attacker["Name"] + " attacks " + defender["Name"] + "!")
  #Calculates speed percentage
  percent = round((attacker["SP"]/defender["SP"])*100)
  if percent > 95:
    percent = 95
  elif percent < 20:
    percent = 20
  print(str(percent) + "% to hit")
  if random.randint(0,100) < percent: #Runs percent check
    #Calculates damage
    if(attacker["ATK"]<defender["DEF"]): #Applies a debuff if defender has a higher defense than attackers attack
      damage = damage-((damage*defender["DEF"])/100)

    damage = damage+(damage*attacker["ATK"])/100 #Applies attack buff

    if((defender["HP"]-damage) < 0): #checks to see if enemy is dead
      defender["HP"] = 0 #Add victory check
    else: #Applies damage
      defender["HP"] = defender["HP"]-round(damage)
    print(damage)
  else:
    print("miss")
  print( "\n" + Bob["Name"]+ " "+str(Bob["HP"]))
  print(John["Name"]+ " "+str(John["HP"]))
print("You encounter John, destroyer of worlds!")

def enemyai(): #used to decide the enemy's action
  enemy_choice = random.randint(1,2)
  if enemy_choice == 1:
    damage_calc(base_damage,John,Bob)
  else:
    print("The enemy waits")

while (Bob["HP"] > 0) and (John["HP"] > 0): #keeps battle running if both players are alive
  choice = "blank"
  choice = input("Choose your action.\n (Type ATK or RUN)")
  if choice == "ATK":
      damage_calc(base_damage,Bob,John)
      #print("\n" + Bob["Name"]+ " "+str(Bob["HP"]))
      #print(John["Name"]+ " "+str(John["HP"]))
      
  elif choice == "RUN":
      print("You are a weakling")
      break
  enemyai()
  #print( "\n" + Bob["Name"]+ " "+str(Bob["HP"]))
  #print(John["Name"]+ " "+str(John["HP"]))
  print("------------Next Turn!------------")
print("Choice Loop Exited")


wn = turtle.Screen()



wn.mainloop()