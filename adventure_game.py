import time
import random


def play_game():
    bad_guy = random.choice(["pirate", "wicked fairie", "troll", "gorgon"])
    weapon = random.choice(["Brainbiter Sword", "Sword Blutgang",
                            "Sword of Fragarach", "Sword of Ogoroth"])
    inventory = []

    def print_pause(text_to_print):
        print(text_to_print)
        time.sleep(3)

    def valid_input(prompt, option1, option2):
        while True:
            response = input(prompt).lower()
            if option1 == response:

                return response
            elif option2 == response:
                return response
            else:
                print_pause(f"(Please enter {option1} or {option2}.)")

    def intro():
        print_pause("You find yourself standing in an open field, filled with "
                    "grass and yellow wildflowers.")
        print_pause(f"Rumor has it that a {bad_guy} is somewhere around here, "
                    "and has been terrifying the nearby village.")
        print_pause("The villagers say he has 10 hit points, but they say you "
                    "do too.")
        print_pause("You wonder what a hit point is and how you somehow got "
                    "10 of them, but decide to not worry about it.\n")
        print_pause("In front of you is a house.")
        print_pause("To your right is a dark cave.")
        print_pause("In your hand you hold your trusty (but not very "
                    "effective) dagger.\n")

    def battle_decision(dmg_mod1, dmg_mod2):
        hero_hp = 10
        bad_guy_hp = 10
        fight_or_flight = valid_input("Would you like to (1) fight or (2) run "
                                      "away?", "1", "2")
        if fight_or_flight == "1":
            while hero_hp >= 1 and bad_guy_hp >= 1:
                hero_damage = dmg_mod1 * random.randint(1, 5)
                bad_guy_damage = dmg_mod2 * random.randint(1, 5)
                hero_hp = hero_hp - bad_guy_damage
                bad_guy_hp = bad_guy_hp - hero_damage
                print_pause(f"The {bad_guy} does {bad_guy_damage} damage to "
                            f"your hit points.  You now have {hero_hp} hit "
                            "points.")
                print_pause(f"You do {hero_damage} damage to the {bad_guy}'s "
                            f"hit points.  He now has {bad_guy_hp} hit "
                            "points.\n")
                if hero_hp <= 0 and bad_guy_hp >= 1:
                    print_pause("You did your best...")
                    print_pause(f"But you were no match for the {bad_guy}.")
                    print_pause("You have been defeated!")
                    play_again()
                elif hero_hp >= 1 and bad_guy_hp <= 0:
                    print_pause("You proved to be an overwhelming foe!")
                    print_pause(f"You have rid the town of the {bad_guy}. You "
                                "are victorious!")
                    play_again()
                elif hero_hp <= 0 and bad_guy_hp <= 0:
                    print_pause("It was the clash of two Titans!")
                    print_pause("You were so equally matched that you are now "
                                "both dead.")
                    print_pause("Take solace in the fact that the villagers "
                                "are now safe.")
                    play_again()
                else:
                    print_pause("Keep fighting!\n")
        else:
            print_pause("You run back into the field.  Luckily, the "
                        f"{bad_guy} takes pity on you and does not follow.\n")
            field()

    def house():
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens and out "
                    f"steps the {bad_guy}.")
        print_pause(f"Eep! This is the {bad_guy}'s house!")
        print_pause(f"The {bad_guy} attacks you.")
        if weapon in inventory:
            print_pause(f"As the {bad_guy} moves to attack, you unsheath your "
                        "new sword.")
            print_pause(f"The {weapon} shines brightly in your hand as you "
                        "brace yourself for the attack.")
            print_pause(f"The {bad_guy} takes one look at your shiny new toy "
                        "and although scared, he attacks anyway!")
            battle_decision(2, 1)
        else:
            print_pause("You feel a bit under-prepared for this, what with "
                        "only having a tiny dagger.")
            battle_decision(1, 2)

    def cave():
        print_pause("You peer cautiously into the cave.")
        if weapon in inventory:
            print_pause("You've been here before, and gotten all the good "
                        "stuff.  It's just an empty cave now.")
            print_pause("You walk back out to the field.")
            field()
        else:
            print_pause("It turns out to be only a very small cave.")
            print_pause("Your eye catches a glint of metal behind a rock.")
            print_pause(f"You have found the magical {weapon}!")
            print_pause("You discard the silly old dagger and take the sword "
                        "with you.")
            print_pause("You walk back out to the field.\n")
            inventory.append(weapon)
            field()

    def field():
        print_pause("Enter 1 to knock on the door of the house.")
        print_pause("Enter 2 to to peer into the cave.")
        print("What would you like to do?")
        decision = valid_input("(Please enter 1 or 2.)\n", "1", "2")
        if decision == "1":
            house()
        else:
            cave()

    def play_again():
        replay = valid_input("Would you like to play again? (y/n)", "y",
                             "n")
        if replay == "y":
            print_pause("Excellent! Restarting the game...\n")
            play_game()
        else:
            print_pause("Thanks for playing! See you next time.")

    intro()
    field()


if __name__ == "__main__":
    play_game()
