class Superhero:
    def __init__(self, name, secret_identity, powers, weakness, base_of_operations):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers  # List of powers
        self.weakness = weakness
        self.base_of_operations = base_of_operations
        self.health = 100
        self.energy = 100
    
    def use_power(self, power_name):
        if power_name in self.powers and self.energy >= 20:
            self.energy -= 20
            print(f"{self.name} uses {power_name}! Energy remaining: {self.energy}")
            return True
        else:
            print(f"Cannot use {power_name}! Not enough energy or power not available.")
            return False
    
    def take_damage(self, damage_amount, damage_type=None):
        if damage_type == self.weakness:
            damage_amount *= 2
            print(f"Critical hit! {self.name} is weak to {damage_type}!")
        
        self.health -= damage_amount
        print(f"{self.name} takes {damage_amount} damage! Health: {self.health}")
        
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
    
    def rest(self):
        self.health = min(100, self.health + 30)
        self.energy = min(100, self.energy + 50)
        print(f"{self.name} rests. Health: {self.health}, Energy: {self.energy}")
    
    def introduce(self):
        return f"I am {self.name}, also known as {self.secret_identity}. My powers include: {', '.join(self.powers)}"


# Inheritance - TechHero specializes Superhero
class TechHero(Superhero):
    def __init__(self, name, secret_identity, powers, weakness, base_of_operations, gadgets):
        super().__init__(name, secret_identity, powers, weakness, base_of_operations)
        self.gadgets = gadgets  # Dictionary: {gadget_name: uses_remaining}
    
    def use_gadget(self, gadget_name):
        if gadget_name in self.gadgets and self.gadgets[gadget_name] > 0:
            self.gadgets[gadget_name] -= 1
            print(f"{self.name} uses {gadget_name}! Uses remaining: {self.gadgets[gadget_name]}")
            return True
        else:
            print(f"Cannot use {gadget_name}! No uses remaining or gadget not available.")
            return False
    
    def craft_gadget(self, gadget_name, uses=3):
        self.gadgets[gadget_name] = uses
        print(f"{self.name} crafted {gadget_name} with {uses} uses!")
    
    # Overriding parent method
    def introduce(self):
        base_intro = super().introduce()
        return f"{base_intro} I'm a tech hero with gadgets: {', '.join(self.gadgets.keys())}"


# Inheritance - MagicHero specializes Superhero
class MagicHero(Superhero):
    def __init__(self, name, secret_identity, powers, weakness, base_of_operations, mana=100):
        super().__init__(name, secret_identity, powers, weakness, base_of_operations)
        self.mana = mana
    
    # Overriding parent method - magic uses mana instead of energy
    def use_power(self, power_name):
        if power_name in self.powers and self.mana >= 25:
            self.mana -= 25
            print(f"{self.name} casts {power_name}! Mana remaining: {self.mana}")
            return True
        else:
            print(f"Cannot cast {power_name}! Not enough mana or spell not available.")
            return False
    
    def meditate(self):
        self.mana = min(100, self.mana + 40)
        self.health = min(100, self.health + 20)
        print(f"{self.name} meditates. Mana: {self.mana}, Health: {self.health}")
    
    # Overriding parent method
    def introduce(self):
        base_intro = super().introduce()
        return f"{base_intro} I wield ancient magic with {self.mana} mana."


# Demonstration
if __name__ == "__main__":
    print("=== Superhero Universe Demo ===\n")
    
    # Create different types of superheroes
    iron_man = TechHero(
        "Iron Man", 
        "Tony Stark",
        ["Repulsor Blasts", "Flight", "Super Strength"],
        "EMP",
        "Stark Tower",
        {"Arc Reactor": 5, "Jarvis AI": 10, "Missiles": 3}
    )
    
    doctor_strange = MagicHero(
        "Doctor Strange",
        "Stephen Strange",
        ["Mystic Arts", "Portal Creation", "Time Manipulation"],
        "Dark Magic",
        "Sanctum Sanctorum",
        150
    )
    
    captain_america = Superhero(
        "Captain America",
        "Steve Rogers",
        ["Super Strength", "Enhanced Agility", "Shield Mastery"],
        "Psychological Warfare",
        "Avengers Tower"
    )
    
    # Demonstrate polymorphism
    heroes = [iron_man, doctor_strange, captain_america]
    
    for hero in heroes:
        print(f"\n{hero.introduce()}")
        hero.use_power(hero.powers[0])  # Each uses their first power differently
        hero.take_damage(25, "Random Attack")
    
    # Demonstrate unique abilities
    print("\n=== Special Abilities ===")
    iron_man.use_gadget("Missiles")
    iron_man.craft_gadget("New Gauntlet", 2)
    
    doctor_strange.meditate()
    doctor_strange.use_power("Portal Creation")
    
    captain_america.rest()
    captain_america.use_power("Shield Mastery")
    
    # Demonstrate weakness system
    print("\n=== Weakness Exploitation ===")
    iron_man.take_damage(20, "EMP")  # Double damage!
    doctor_strange.take_damage(15, "Dark Magic")  # Double damage!