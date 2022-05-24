import random

def guess_number(num):
    try:
        ran_num = random.randint(1,5)
        if num and 0<num<6:
            if ran_num==num:
                return "Hurrah! You guessed it right!"
            else:
                return "Close but wrong! Try again"
        else:
            return "Number invalid - Enter a valid number!"
    except (ValueError,TypeError) as err:
        return err

if __name__=="__main__":
    num = int(input("Please enter a valid number between 1 to 5 : "))
    result = guess_number(num)
    print(result)