import random

def roll_dice(num_dice=1):
    """Simulate rolling a given number of dice."""
    rolls = []
    for _ in range(num_dice):
        roll = random.randint(1, 6) 
        rolls.append(roll)
    return rolls

def main():
    print("Welcome to the Dice Roller!")

    num_dice = int(input("Enter the number of dice to roll: ") or 1)
    
    rolls = roll_dice(num_dice)
    
    print(f"\nYou rolled {num_dice} dice:")
    for i, roll in enumerate(rolls, start=1):
        print(f"Dice {i}: {roll}")
    
    while input("\nRoll again? (y/n): ").lower() == 'y':
        rolls = roll_dice(num_dice)
        print(f"\nYou rolled {num_dice} dice:")
        for i, roll in enumerate(rolls, start=1):
            print(f"Dice {i}: {roll}")
    
    print("\nThank you for playing!")

if __name__ == "__main__":
    main()
