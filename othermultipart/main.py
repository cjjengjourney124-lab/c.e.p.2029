for muscle in range(0,1):
    import os, hangman, starwarsName, kingD

    
    
    
    while True:
        
        os.system("clear")
        ilikepizza = int(input("Do you want to play, \n1. hangman \n \n2. star wars name generator? \n \nor\n  \n3. kingdom of elo   \njust put numbers ->  "))
        os.system("clear")
        if ilikepizza == 1:
            hangman.hangmanthegame()
        elif ilikepizza == 2:
            starwarsName.starwarsnamegen()
        elif ilikepizza == 3:
            kingD.kingdomofE()
