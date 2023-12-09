import random
def cal_scr(score):
    if score < 0 or score > 100:
        return "Invalid score. Try again"
    else:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Failed"


def main():
    my_score = int(input("Enter your score: "))
    result = cal_scr(my_score)
    print(result)

    rand_scr = random.randint(0, 100)
    result = cal_scr(rand_scr)
    print("Random score:", rand_scr)
    print("Result for random score:", result)

main()
