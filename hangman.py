import random
print("Welcome to Hangman word guessing game!!")
name=input("Enter your name: ")
print("Hope you won't let your man hang !")
print("You have 10 chances ...")

def hangman():
    word_list=["cake","chain","family","reader","beginning","leveling","nobe"]
    word=random.choice(word_list)
    # print(word)
    
    
    chance=10
    guess_made=""
    valid_word=set("abcdefghijklmnopqrstuvwxyz")
    while len(word) > 0:
        main_word=""
                
        for letter in word:
            if letter in guess_made:
                main_word += letter
            else:
                main_word += '_ '
                
        if main_word == word:
            print(main_word)
            print("You won !")
            break
        
        print("guess the word",    main_word)
        guess = input("enter the guess letter: ")
        
        if guess in valid_word:
            guess_made += guess
            
        else:
            print("Invalid character")
            
        if guess not in word:
            chance -= 1
            
            if chance == 9:
                print("  9 chances left !")
                print("   ____________")
            if chance == 8:
                print("  8 chances left !")
                print("   ____________")
                print("         0     ")
            if chance == 7:
                print("  7 chances left !")
                print("   ____________")
                print("         0      ")
                print("         |      ")
            if chance == 6:
                print("6 chances left !")
                print("   ____________")
                print("         0      ")
                print("         |      ")
                print("        /       ")
            if chance == 5:
                print("  5 chances left !")
                print("   ____________")
                print("         0      ")
                print("         |      ")
                print("        / \     ")
            if chance == 4:
                print("  4 chances left !")
                print("   ____________")
                print("        \0      ")
                print("         |      ")
                print("        / \     ")
            if chance == 3:
                print("  3 chances left !!,      oi dumb ... you are about to lose ...")
                print("   ____________")
                print("        \0/     ")
                print("         |      ")
                print("        / \     ")
            if chance == 2:
                print("  2 chances left !!,      your man is about to die..., loser!!")
                print("   ____________")
                print("         0      ")
                print("        /|\     ")
                print("        / \     ")
            if chance == 1:
                print("  1 chance left !! ,      your man is in last breathe....dumb ass")
                print("   ____________")
                print("             |  ")
                print("         0      ")
                print("        /|\     ")
                print("        / \     ")
            if chance == 0:
                print("     you killed your man !!            .... - ~ -.... muderer")
                print("     you lose!!            ... * _ *...")
                print("   ____________")
                print("              | ")
                print("         Q____| ")
                print("        /|\     ")
                print("        / \     ")
                break
hangman()
            
def replay():
    while True:
        play_again = input("Do you want to play again enter y if yes or anything if no: ")
        if play_again == "y":
            hangman()
        else:
            break
replay()