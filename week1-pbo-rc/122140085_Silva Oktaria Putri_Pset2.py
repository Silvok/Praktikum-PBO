import random

class Robot:

  def __init__(self, name, hp, attack):
    self.name = name
    self.hp = hp
    self.attack = attack

  def take_damage(self, damage):
    self.hp -= damage

  def is_alive(self):
    return self.hp > 0

  def __str__(self):
    return f"{self.name} {self.hp}|{self.attack}|"


class Game:

  def __init__(self, robot1, robot2):
    self.robot1 = robot1
    self.robot2 = robot2
    self.round = 1

  def start(self):
    while self.robot1.is_alive() and self.robot2.is_alive():
      print(f"Round-{self.round}{'=' * 50}")
      print(f"{self.robot1}\n{self.robot2}\n")
      self.battle()
      self.round += 1

    winner = self.robot2.name if self.robot1.is_alive() else self.robot1.name
    print(f"{winner} wins!")

  def battle(self):
    actions = ["Attack", "Defense", "Giveup"]
    for robot in [self.robot1, self.robot2]:
      print("\n".join(f"{i + 1}. {action}"
                      for i, action in enumerate(actions)))
      action = int(input(f"{robot.name}, Select the action: "))

      if action == 1:
        target = self.robot2 if robot == self.robot1 else self.robot1
        damage = robot.attack
        if random.random() <= 0.5:
          target.take_damage(damage)
          print(f"---------{target.name} Miss the attack----------" if target
                == self.robot2 else f"{target.name} takes {damage} damage!")
        else:
          print(f"{target.name} defends!")
      elif action == 3:
        print(f"{robot.name} gives up!")
        return


robot1 = Robot("Atreus", 500, 10)
robot2 = Robot("Daedalus", 750, 8)

game = Game(robot1, robot2)
game.start()
