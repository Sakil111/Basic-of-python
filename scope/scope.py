# local scope
def drink_potion():
    potion_strength=2
    print(potion_strength)
drink_potion()

# global scope

player_health=5
def game():
    def drink_postion():
        potion_strength=2
        print(player_health)
    drink_postion()
game()

# Modifying global scope
enemies=1
def increase_enemies():
    print(f"number of enemies {enemies}")
    return enemies+1
increase_enemies()
print(f"number of enemies {enemies}")

# Global constatnt
# we wite this global constatnt in the uppercase so that we can understatnd this variable is not changeable
PI=3.1416
def cal():
    PI
cal()