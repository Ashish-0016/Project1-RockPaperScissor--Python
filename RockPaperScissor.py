import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)   ░𝐑░ ░𝐎░ ░𝐂░ ░𝐊░ 🪨
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)   ░𝐏░ ░𝐀░ ░𝐏░ ░𝐄░ ░𝐑░ 📄
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)    ░𝐒░ ░𝐂░ ░𝐈░ ░𝐒░ ░𝐒░ ░𝐎░ ░𝐑░  ✂️
      (____)
---.__(___)
'''

img = [rock, paper, scissor]
chances = 0
while chances < 6:
    user_choice = input("\nType 0 for Rock, 1 for Paper, 2 for Scissor, or 3 to exit.\n")

    if user_choice == '3':
        break

    user_choice = int(user_choice)

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, please try again.")
        continue
    print("𝐘𝐨𝐮 𝐜𝐡𝐨𝐬𝐞 :")
    print(img[user_choice]+"\n")

    computer_choice = random.randint(0, 2)
    print("Computer 𝗰𝗵𝗼𝘀𝗲 :")
    print(img[computer_choice]+"\n")

    if user_choice == computer_choice:
        print("🅳  🆁  🅰  🆆!")
    elif user_choice == 0 and computer_choice == 2:
        print("🆈 🅾  🆄   🆆 🅸 🅽 🆂 !")
    elif computer_choice == 0 and user_choice == 2:
        print("🅲 🅾 🅼 🅿  🆄  🆃  🅴  🆁     🆆 🅸 🅽 🆂 ❗")
    elif computer_choice > user_choice:
        print("🅲 🅾 🅼 🅿  🆄  🆃  🅴  🆁     🆆 🅸 🅽 🆂 ❗")
    else:
        print("🆈 🅾  🆄   🆆 🅸 🅽 🆂 !")

    chances += 1

print("\nThank you for playing! created by ASHISH cap03_001\n")
