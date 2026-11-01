def kingdomofE():


  import random

  indentspace = '\n'
  class Player:
      def __init__(self, name):
          self.name = name
          self.hp = 100
          self.attack = 10
          self.defense = 5
          self.strength = 1
          self.luck = 1
          self.money = 0
          self.xp = 0
          self.level = 1
          self.weapon = "Sword"
          self.location = "house"  # Start in the house

          # Attack types with their respective max damage and success rates
          self.attack_types = {
              "Slash": {"max_damage": 15+45, "success_rate": 0.8},
              "Stab": {"max_damage": 12+45, "success_rate": 0.9},
              "Smash": {"max_damage": 18+45, "success_rate": 0.7},
              "Fireball": {"max_damage": 25+45, "success_rate": 0.6}
          }

      def is_alive(self):
          return self.hp > 0

      def take_damage(self, damage):
          self.hp -= max(0, damage - self.defense)

      def attack_enemy(self, enemy, attack_type):
          if attack_type not in self.attack_types:
              print("Invalid attack type!")
              return

          attack_stats = self.attack_types[attack_type]
          damage = self.calculate_damage(attack_stats)
          if damage > 0:
              print("[!!!] "+f"{self.name} uses {attack_type} and deals {damage} damage to {enemy.name}!")
              enemy.take_damage(damage)
              print(f"{self.name}'s Health: {self.hp}/{self.hp}")
              print(f"{enemy.name}'s Health: {enemy.hp}/{enemy.max_hp}")
          else:
              print(f"{self.name}'s {attack_type} missed!")

      def calculate_damage(self, attack_stats):
          max_damage = attack_stats["max_damage"]
          success_rate = attack_stats["success_rate"]
          if random.random() <= success_rate:
              return random.randint(1, max_damage)
          else:
              return 0

      def level_up(self):
          if self.xp >= 100 * self.level:
              self.level += 1
              self.xp = 0
              self.attack += 5
              self.defense += 2
              print(indentspace)
              print(f"{self.name} leveled up to level {self.level}!")
              print(f"Attack increased to {self.attack}, Defense increased to {self.defense}.")

      def buy_weapon(self, weapon_name, price):
          if self.money >= price:
              self.weapon = weapon_name
              self.money -= price
              print(indentspace)
              print(f"You bought a {weapon_name} for {price} coins!")
          else:
              print(indentspace)
              print("You don't have enough money to buy that weapon!")

      def display_stats(self):
          print(indentspace)
          print(f"Name: {self.name}")
          print(f"HP: {self.hp}")
          print(f"Attack: {self.attack}")
          print(f"Defense: {self.defense}")
          print(f"Strength: {self.strength}")
          print(f"Luck: {self.luck}")
          print(f"Money: {self.money}")
          print(f"XP: {self.xp}")
          print(f"Level: {self.level}")
          print(f"Weapon: {self.weapon}")
          print(f"Location: {self.location}")

      def upgrade_strength(self):
          if self.money >= 50:
              self.strength += 1
              self.money -= 50
              print(indentspace)
              print(f"You upgraded your strength! Current Strength: {self.strength}")
          else:
              print(indentspace)
              print("You don't have enough money to upgrade your strength.")

      def upgrade_luck(self):
          if self.money >= 50:
              self.luck += 1
              self.money -= 50
              print(indentspace)
              print(f"You upgraded your luck! Current Luck: {self.luck}")
          else:
              print(indentspace)
              print("You don't have enough money to upgrade your luck.")

      ### Scroll up to line 1 to view instructions. 
      ### Not sure why the editor does this, but it keeps ending up here instead of up there.

      def upgrade_hp(self):
          if self.money >= 50:
              self.hp += 10
              self.money -= 50
              print(indentspace)
              print(f"You upgraded your HP! Current HP: {self.hp}")
          else:
              print(indentspace)
              print("You don't have enough money to upgrade your HP.")

  class Enemy:
      def __init__(self, name, hp, attack, xp):
          self.name = name
          self.hp = hp
          self.max_hp = hp
          self.attack = attack
          self.xp = xp

      def is_alive(self):
          return self.hp > 0

      def take_damage(self, damage):
          self.hp -= damage

      def attack_player(self, player):
          damage = random.randint(self.attack // 2, self.attack)
          print(indentspace)
          print("[!!!] "+f"{self.name} attacks {player.name} for {damage} damage!")
          player.take_damage(damage)

  class Location:
      def __init__(self, name, description):
          self.name = name
          self.description = description
          self.enemies = []

      def add_enemy(self, enemy):
          self.enemies.append(enemy)

      def remove_enemy(self, enemy):
          self.enemies.remove(enemy)

      def get_random_enemy(self):
          return random.choice(self.enemies)

      def is_cleared(self):
          return len(self.enemies) == 0

  def explore(player):
      print("You start exploring the surroundings...")
      exploration_reward = random.randint(10, 30)
      player.money += exploration_reward
      print(f"You found {exploration_reward} coins!")

  def print_enemy_ascii(enemy_name):
      if enemy_name == "Thug":
          print(r"""
                   __
             _/|_ [ o] - Thug
            /  |  """
          )
      elif enemy_name == "Bandit":
          print(r"""
              ____
          __/    [ o] - Bandit
         /        """
          )
      elif enemy_name == "Guard":
          print(r"""
               ___
             [   o] - Guard
            / |  """
          )
      elif enemy_name == "Wolf":
          print(r"""
             __
        _  /  \
       / \/    | - Wolf
       \_      /  
         |____|  """
          )
      elif enemy_name == "Bear":
          print(r"""
                /\/\  
              ( o  o) - Bear
              _\  /_
             /     \ """
          )
      elif enemy_name == "Giant Spider":
          print(r"""
                  /\/\
            _____/ o  o \ - Giant Spider
           /            \ 
          |              | """
          )
      elif enemy_name == "Knight":
          print(r"""
                   /   \  
              [\\  o  o /] - Knight
              <]  \___/ [> """
          )
      elif enemy_name == "Sorcerer":
          print(r"""
              / \___/ \  
            [ o       o] - Sorcerer
            [  \___/  ] """
          )
      elif enemy_name == "Dragon":
          print(r"""
                   /\\
            /      [ o  o] - Dragon
           <________\  /  
                     v """
          )
      elif enemy_name == "Skeleton":
          print(r"""
               __
         __   [ o] - Skeleton
        /  \___\ """
          )
      elif enemy_name == "Zombie":
          print(r"""
                 _
         _____  |*| - Zombie
        /     \_|_ """
          )
      elif enemy_name == "Ghoul":
          print(r"""
                ___
              [o o] - Ghoul
             / ___ \ """
          )
      else:
          print("No ASCII art available for this enemy.")

  class NPC:
      def __init__(self, name, dialogues):
          self.name = name
          self.dialogues = dialogues

      def talk(self):
          print(f"{self.name}: {random.choice(self.dialogues)}")


  def main():
      print(indentspace)
      print("~~ Welcome to the Kingdom of Eloria ~~\nA land of magic and mystery\n(c) 2024 Programmed by LeaferStudios\n")
      print("You are a brave adventurer seeking fame and fortune.")

      player_name = input("What is your name, adventurer? ")
      player = Player(player_name)

      print(indentspace)
      print(f"Greetings, {player.name}! Your journey begins in your house.")
      print("You have four quests to undertake: city, forest, castle, and dungeons.")




      # Locations initialization
      house = Location("House", "You are in your humble house.")
      city = Location("Aldoria", "You are in the heart of the city of Aldoria, where merchants hawk their wares and adventurers seek their fortune.")
      city.add_enemy(Enemy("Thug", 30, 8, 20))
      city.add_enemy(Enemy("Bandit", 40, 10, 30))
      city.add_enemy(Enemy("Guard", 50, 12, 40))

      forest = Location("Darkwood Forest", "You find yourself deep within the Darkwood Forest, where ancient trees loom overhead, and eerie sounds echo through the mist.")
      forest.add_enemy(Enemy("Wolf", 30, 8, 20))
      forest.add_enemy(Enemy("Bear", 50, 12, 40))
      forest.add_enemy(Enemy("Giant Spider", 40, 10, 30))

      castle = Location("Ravenstone Castle", "Before you stands Ravenstone Castle, a towering fortress shrouded in legend and mystery.")
      castle.add_enemy(Enemy("Knight", 60, 15, 50))
      castle.add_enemy(Enemy("Sorcerer", 70, 18, 60))
      castle.add_enemy(Enemy("Dragon", 100, 20, 100))

      dungeons = Location("Catacombs", "You descend into the dark, labyrinthine Catacombs beneath Ravenstone Castle, where ancient horrors lie in wait.")
      dungeons.add_enemy(Enemy("Skeleton", 40, 10, 30))
      dungeons.add_enemy(Enemy("Zombie", 50, 12, 35))
      dungeons.add_enemy(Enemy("Ghoul", 60, 15, 40))

      # Quests dictionary
      quests = {
          "city": city,
          "forest": forest,
          "castle": castle,
          "dungeons": dungeons
      }

      while player.is_alive():
          print(indentspace)
          print("Available Actions:")
          print("1. Explore")

          print("2. Choose a Quest")

          action = input("What will you do? (1/2): ")

          if action == "1":
              explore(player)
          elif action == "2":
              print(indentspace)
              print("Available Quests:")
              for quest, location in quests.items():
                  print(f"{quest.capitalize()} - {location.description}")

              chosen_quest = input("Which quest do you want to undertake? ").lower()
              if chosen_quest in quests:
                  current_location = quests[chosen_quest]

                  print(indentspace)
                  print(f"You embark on the quest to {current_location.name}...")

                  while not current_location.is_cleared() and player.is_alive():
                      current_enemy = current_location.get_random_enemy()
                      print(indentspace)
                      print(f"A {current_enemy.name} blocks your path!")
                      print_enemy_ascii(current_enemy.name)

                      while current_enemy.is_alive() and player.is_alive():
                          action = input("What will you do? (attack/1/2): ").lower()

                          if action == "attack":
                              print(indentspace)
                              print("Available Attacks:")
                              for attack_type in player.attack_types:
                                  print(f"- {attack_type}: Max Damage - {player.attack_types[attack_type]['max_damage']}, Success Rate - {player.attack_types[attack_type]['success_rate'] * 100}%")

                              chosen_attack = input("Choose your attack: ").capitalize()
                              player.attack_enemy(current_enemy, chosen_attack)
                              if current_enemy.is_alive():
                                  current_enemy.attack_player(player)
                              else:
                                  player.xp += current_enemy.xp
                                  player.money += random.randint(10, 20)
                                  player.level_up()
                                  current_location.remove_enemy(current_enemy)
                                  if current_location.is_cleared():
                                      upgrade_choice = input("Do you want to upgrade your skills? (yes/no): ").lower()
                                      if upgrade_choice == "yes":
                                          player.upgrade_strength()
                                          player.upgrade_luck()
                                          player.upgrade_hp()
                          elif action == "1":
                              player.display_stats()
                          elif action == "2":
                              print("Available upgrades:")
                              print("3 - Upgrade Strength (costs 50 coins)")
                              print("4 - Upgrade Luck (costs 50 coins)")
                              print("5 - Upgrade HP (costs 50 coins)")
                          elif action == "3":
                              player.upgrade_strength()
                          elif action == "4":
                              player.upgrade_luck()
                          elif action == "5":
                              player.upgrade_hp()
                          else:
                              print(indentspace)
                              print("Invalid action! Try again.")

                      if not player.is_alive():
                          print(indentspace)
                          print("You have been defeated! Game Over.")
                          break

                      print(indentspace)
                      print(f"You defeated the {current_enemy.name}!")
                      print(f"XP Gained: {current_enemy.xp}")
                      print(f"Current XP: {player.xp}")
                      print(f"Current Level: {player.level}")
                      print(f"Current HP: {player.hp}")
                      print(f"Current Money: {player.money}")

                  if player.is_alive():
                      print(indentspace)
                      print(f"You have cleared the {current_location.name}.")
                      print(f"XP Earned: {player.xp}")
                      print(f"Money Earned: {player.money}")
              else:
                  print(indentspace)
                  print("Invalid quest! Choose again.")
          else:
              print(indentspace)
              print("Invalid action! Try again.")

      print(indentspace)
      print("Thanks for playing!")

  if __name__ == "__main__":
      main()
