import random
import os
import time
import pygame

pygame.mixer.init()

def russian_roulette():
    chamber = ["Kosong"] * 5 + ["Peluru"]
    random.shuffle(chamber)
    used_choice = set()
    
    ronde = 1
    while len(chamber) > 0:
        while True:
            try:
                choice = int(input(f"Round {ronde}, try to guess it (1-6): "))
                if 1 <= choice <= 6 and choice not in used_choice:
                    used_choice.add(choice)
                    break
                elif choice in used_choice:
                    print("Gentleman, you already chose that, pick another number.")
                else:
                    print("Gentleman, the allowed numbers are 1-6")
            except ValueError:
                print("Gentleman, you only be able to input a number.")
            
        os.system("cls")
        shot = chamber.pop(0)
        
        if shot == "Peluru":
            # 6th round inevitable death haha
            if ronde == 6:
                try:
                    sound = pygame.mixer.Sound("Gunshot.mp3")
                    sound.play()
                except pygame.error as e:
                    print("No such sound:", e)
                print("Your death is inevitable")
                time.sleep(3)
                exit()
            else:
                try:
                    sound = pygame.mixer.Sound("Gunshot.mp3")
                    sound.play()
                except pygame.error as e:
                    print("No such sound:", e)
                print("And now you're death")
                time.sleep(3)
                exit()
        else:
            print("Safe, but I wonder how long it will last?")
        
        ronde += 1

if __name__ == "__main__":
    russian_roulette()
