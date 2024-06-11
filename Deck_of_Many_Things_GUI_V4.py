import tkinter as tk
from tkinter import messagebox
import random

# Define the cards in the Deck of Many Things
deck_of_many_things = [
    "Balance: Your mind suffers a wrenching alteration, causing your alignment to change. Lawful becomes chaotic, good becomes evil, and vice versa. If you are true neutral or unaligned, this card has no effect on you.",
    "Comet: If you single-handedly defeat the next hostile monster or group of monsters you encounter, you gain experience points enough to gain one level. Otherwise, this card has no effect.",
    "Donjon: You disappear and become entombed in a state of suspended animation in an extradimensional sphere. Everything you were wearing and carrying stays behind in the space you occupied when you disappeared. You remain imprisoned until you are found and removed from the sphere. You can't be located by any divination magic, but a wish spell can reveal the location of your prison. You draw no more cards.",
    "Euryale: The card's medusa-like visage curses you. You take a -2 penalty on saving throws while cursed in this way. Only a god or the magic of The Fates card can end this curse.",
    "The Fates: Reality's fabric unravels and spins anew, allowing you to avoid or erase one event as if it never happened. You can use the card's magic as soon as you draw the card or at any other time before you die.",
    "Flames: A powerful devil becomes your enemy. The devil seeks your ruin and plagues your life, savoring your suffering before attempting to slay you. This enmity lasts until either you or the devil dies.",
    "Fool: You lose 10,000 XP, discard this card, and draw from the deck again, counting both draws as one of your declared draws. If losing that much XP would cause you to lose a level, you instead lose an amount that leaves you with just enough XP to keep your level.",
    "Gem: Twenty-five pieces of jewelry worth 2,000 gp each or fifty gems worth 1,000 gp each appear at your feet.",
    "Idiot: Permanently reduce your Intelligence by 1d4 + 1 (to a minimum score of 1). You can draw one additional card beyond your declared draws.",
    "Jester: You gain 10,000 XP, or you can draw two additional cards beyond your declared draws.",
    "Key: A rare or rarer magic weapon with which you are proficient appears in your hands. The DM chooses the weapon.",
    "Knight: You gain the service of a 4th-level fighter who appears in a space you choose within 30 feet of you. The fighter is of the same race as you and serves you loyally until death, believing the fates have drawn him or her to you. You control this character.",
    "Moon: You are granted the ability to cast the wish spell 1d3 times.",
    "Rogue: A nonplayer character of the DM's choice becomes hostile toward you. The identity of your new enemy isn't known until the NPC or someone else reveals it. Nothing less than a wish spell or divine intervention can end the NPC's hostility toward you.",
    "Ruin: All forms of wealth that you carry or own, other than magic items, are lost to you. Portable property vanishes. Businesses, buildings, and land you own are lost in a way that alters reality the least. Any documentation that proves you should own something lost to this card also disappears.",
    "Skull: You summon an avatar of death-a ghostly humanoid skeleton clad in a tattered black robe and carrying a spectral scythe. It appears in a space of the DM's choice within 10 feet of you and attacks you, warning all others that you must win the battle alone. The avatar fights until you die or it drops to 0 hit points, whereupon it disappears. If anyone tries to help you, the helper summons its own avatar of death. A creature slain by an avatar of death can't be restored to life.",
    "Star: Increase one of your ability scores by 2. The score can exceed 20 but can't exceed 24.",
    "Sun: You gain 50,000 XP, and a wondrous item (which the DM determines randomly) appears in your hands.",
    "Talons: Every magic item you wear or carry disintegrates. Artifacts in your possession aren't destroyed but do vanish.",
    "Throne: You gain proficiency in the Persuasion skill, and you double your proficiency bonus on checks made with that skill. In addition, you gain rightful ownership of a small keep somewhere in the world. However, the keep is currently in the hands of monsters, which you must clear out before you can claim the keep as yours.",
    "Vizier: At any time you choose within one year of drawing this card, you can ask a question in meditation and mentally receive a truthful answer to that question. Besides information, the answer helps you solve a puzzling problem or other dilemma. In other words, the knowledge comes with wisdom on how to apply it.",
    "The Void: This black card spells disaster. Your soul is drawn from your body and contained in an object in a place of the DM's choice. One or more powerful beings guard the place. While your soul is trapped in this way, your body is incapacitated. A wish spell can't restore your soul, but the spell reveals the location of the object that holds it. You draw no more cards."
]

class DeckOfManyThingsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Deck of Many Things")
        
        self.draw_buttons = []
        self.drawn_cards_labels = []
        
        for i in range(1, 4):
            draw_button = tk.Button(master, text=f"Draw {i} Cards", command=lambda num=i: self.draw_cards(num))
            draw_button.grid(row=i-1, column=0, padx=5, pady=5, sticky="e")
            self.draw_buttons.append(draw_button)
            
            drawn_cards_label = tk.Label(master, text="", wraplength=400, justify="left", anchor="w")  # Increased wraplength to 400
            drawn_cards_label.grid(row=i-1, column=1, padx=5, pady=5, sticky="w")
            self.drawn_cards_labels.append(drawn_cards_label)
        
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_cards)
        self.reset_button.grid(row=3, columnspan=2, pady=10)
            
    def draw_cards(self, num):
        # Draw the specified number of cards
        drawn_cards = random.sample(deck_of_many_things, num)
        
        # Display the drawn cards
        for i in range(num):
            self.drawn_cards_labels[i].config(text=drawn_cards[i])
    
    def reset_cards(self):
        # Reset drawn cards labels
        for label in self.drawn_cards_labels:
            label.config(text="")

def main():
    root = tk.Tk()
    app = DeckOfManyThingsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
