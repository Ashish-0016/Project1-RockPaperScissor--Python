from random import randint

t = ["Rock", "Paper", "Scissors"]

emojis = {
    "Rock": '''
    _______
---'   ____)
      (_____)
      (_____)   ░𝐑░ ░𝐎░ ░𝐂░ ░𝐊░ 🪨
      (____)
---.__(___)
'''
,
"Paper": '''
    _______
---'   ____)____
          ______)
          _______)   ░𝐏░ ░𝐀░ ░𝐏░ ░𝐄░ ░𝐑░ 📄
         _______)
---.__________)
'''
,
"Scissors": '''
    _______
---'   ____)____
          ______)
       __________)    ░𝐒░ ░𝐂░ ░𝐈░ ░𝐒░ ░𝐒░ ░𝐎░ ░𝐑░  ✂️
      (____)
---.__(___)
'''
}

total_rounds = 5
Total_Rounds = 0
Wins = 0
Losses = 0
Draw = 0

print("Type 0 for Rock, 1 for Paper, 2 for Scissors, or 3 to exit.")

while Total_Rounds < total_rounds:
    user_choice = input(f"\nRound {Total_Rounds + 1}: Your choice: ")

    if user_choice == '3':
        break

    user_choice = int(user_choice)

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, please try again.")
        continue

    Total_Rounds += 1

    player_move = t[user_choice]

    print(f"\nYour choice: {emojis[player_move]}")
    
    computer_move = t[randint(0, 2)]
    print(f"Computer's choice: {emojis[computer_move]}\n")

    if player_move == computer_move:
        Draw += 1
        print("🅳  🆁  🅰  🆆!")
    elif player_move == "Rock" and computer_move == "Scissors":
        Wins += 1
        print("🆈 🅾  🆄   🆆 🅸 🅽 👨")
    elif computer_move == "Rock" and player_move == "Scissors":
        Losses += 1
        print("🅲 🅾 🅼 🅿  🆄  🆃  🅴  🆁    🆆 🅸 🅽 💻❗")
    elif t.index(computer_move) > t.index(player_move):
        Losses += 1
        print("🅲 🅾 🅼 🅿  🆄  🆃  🅴  🆁    🆆 🅸 🅽 💻❗")
    else:
        Wins += 1
        print("🆈 🅾  🆄   🆆 🅸 🅽 👨")

print("\nMatch Result👇\n")
print(f"Total Rounds: {Total_Rounds}")
print(f"Wins: {Wins}")
print(f"Losses: {Losses}")
print(f"Draws: {Draw}")

print("\nThank you for playing! Created by ASHISH cap03_001\n")
