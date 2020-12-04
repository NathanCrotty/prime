from math import sqrt
def dec(num):
    if round(num) == num:
        return False
    else:
        return True


def isprime(num):
    a = 2
    if dec(num) == True:
        return "Error"
    # the above if statement says that if a the number put into "isprime()" function is a decimal, return "Error"

    while 1 == 1:

        if dec(num / a) == False:
            print(str(num) + " / " + str(a) + " = " + str(num / a))
            return False

            break
        elif a >= round(sqrt(num)):
            return True
            break
        else:
            print(str(num) + " / " + str(a) + " = " + str(num / a))
            if a >= 3:
                a += 2
            else:
                a += 1
            continue


while 1 == 1:
    print(str(isprime(float(input()))))
