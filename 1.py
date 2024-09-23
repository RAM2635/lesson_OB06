import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(10, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self):
        self.player = Hero("Игрок")
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра начинается!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            if self.computer.is_alive():
                self.computer.attack(self.player)
            print(f"Здоровье игрока: {self.player.health}")
            print(f"Здоровье компьютера: {self.computer.health}")
            print("-" * 20)

        if self.player.is_alive():
            print("Игрок победил!")
        else:
            print("Компьютер победил!")


if __name__ == "__main__":
    game = Game()
    game.start()
