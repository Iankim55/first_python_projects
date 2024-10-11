def game():
    print("Welcome to the game")
    user =input("enter your name: ")
    score = 0
    if len(user)>12:
        print("your name is too long")
        score += 1
    else:
        print(f"{user} welcome to the game")
    Start= input("what is it that makes month? ")

    if Start != "A week":
        print("Your answer is incorrect")
        score+=1
    print ("you got "+str(score)+ "questions incorrectly")
    print ("you got "+str(score/1*100)+ "% questions correctly")


print (game())