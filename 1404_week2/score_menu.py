
def get_score():
    score = int(input("Enter your score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        return score
        #print_res(score)
        #star(score)
def cal(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Failed"

def print_res(score):
    result= cal(score)
    print ("You are",result)
def star(score):
    print("*" * score)

def main():

    MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars 
(Q)uit"""
    print(MENU)
    choice= input("Choose one>> ").upper()

    while choice!="Q":
        if choice == "G":
            score=get_score()

        elif choice == "P":
            # cal(score)
             print_res(score)

        elif choice == "S":
            star(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input("Choose one>> ").upper()
    print("Farewell")

main()