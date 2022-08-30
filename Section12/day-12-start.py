################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

# Global Scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(potion_strength)
    print(player_health)

drink_potion()

# Global Scope
player_health = 10

#Global Constants should be in Upper Case
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE_ = "@johndaeira"



