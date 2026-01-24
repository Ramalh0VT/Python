import json
import os # NEW: Needed to check if the file exists

# --- CLASSES (Same as before) ---
class Pet:
    def __init__(self, hunger=50, hygiene=50, happiness=50, health=50):
        self.min_value = 0
        self.max_value = 100
        self.hunger = hunger 
        self.hygiene = hygiene
        self.happiness = happiness
        self.health = health

    def _clamp(self, value):
        return max(self.min_value, min(value, self.max_value))

    @property
    def hunger(self): return self._hunger
    @hunger.setter
    def hunger(self, value): self._hunger = self._clamp(value)

    @property
    def hygiene(self): return self._hygiene
    @hygiene.setter
    def hygiene(self, value): self._hygiene = self._clamp(value)

    @property
    def happiness(self): return self._happiness
    @happiness.setter
    def happiness(self, value): self._happiness = self._clamp(value)

    @property
    def health(self): return self._health
    @health.setter
    def health(self, value): self._health = self._clamp(value)

    def feed(self):
        self.hunger += 20
        self.health += 5
        print("Fed the pet!")

    def play(self):
        self.hunger -= 10
        self.happiness += 20
        print("Played with pet!")

    def bath(self):
        self.hygiene += 40
        print("Gave a bath!")

    def get_status(self):
        print(f"Stats: Hunger:{self.hunger} | Hygiene:{self.hygiene} | Happiness:{self.happiness} | Health:{self.health}")

class Cat(Pet):
    def bath(self):
        super().bath()
        self.happiness -= 50
        print("The cat scratched you!")

class Dog(Pet):
    def play(self):
        super().play()
        self.happiness += 40
        self.hygiene -= 20
        print("Dog is happy but muddy!")

# --- SAVE & LOAD FUNCTIONS ---

def save_pet(pet):
    data = {
        "type": pet.__class__.__name__, # Saves "Cat" or "Dog"
        "hunger": pet.hunger,
        "hygiene": pet.hygiene,
        "happiness": pet.happiness,
        "health": pet.health
    }
    with open("savegame.json", "w") as f:
        json.dump(data, f)
    print("--- Game Saved Successfully! ---")

def load_pet():
    """Reads the file and creates the correct Pet object."""
    try:
        with open("savegame.json", "r") as f:
            data = json.load(f)
            
        # 1. Identify which Class to create
        pet_type = data["type"]
        
        # 2. Create the specific object using the saved numbers
        if pet_type == "Cat":
            # We pass the saved values into the __init__
            loaded_pet = Cat(
                hunger=data["hunger"],
                hygiene=data["hygiene"],
                happiness=data["happiness"],
                health=data["health"]
            )
        elif pet_type == "Dog":
            loaded_pet = Dog(
                hunger=data["hunger"],
                hygiene=data["hygiene"],
                happiness=data["happiness"],
                health=data["health"]
            )
        else:
            return None # Unknown type

        print(f"\nWelcome back! Your {pet_type} missed you.")
        return loaded_pet
        
    except (FileNotFoundError, json.JSONDecodeError):
        return None # Return None if anything goes wrong

# --- MAIN EXECUTION ---

def main():
    print("Welcome to Python Pets!")
    current_pet = None

    # 1. CHECK FOR SAVE FILE
    if os.path.exists("savegame.json"):
        choice = input("Found a saved game! Do you want to load it? (yes/no): ").lower()
        if choice == "yes":
            current_pet = load_pet()

    # 2. IF NO PET LOADED, CREATE NEW
    if current_pet is None:
        print("\nStarting a New Game...")
        while True:
            choice = input("Do you want a Cat or a Dog? ").strip().lower()
            if choice == "dog":
                current_pet = Dog()
                break
            elif choice == "cat":
                current_pet = Cat()
                break
            else:
                print("Invalid Option")

    # 3. GAME LOOP
    while True:
        current_pet.get_status()
        action = input("\nAction (feed, play, bath, save, quit): ").lower()

        if action == "feed":
            current_pet.feed()
        elif action == "play":
            current_pet.play()
        elif action == "bath":
            current_pet.bath()
        elif action == "save":
            save_pet(current_pet)
        elif action == "quit":
            print("Goodbye!")
            break
        else:
            print("I don't understand that command.")

if __name__ == "__main__":
    main()