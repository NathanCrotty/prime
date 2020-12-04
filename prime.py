from math import sqrt, ceil
from time import time, sleep
from keyboard import is_pressed
from getpass import getpass
import sys

index = 0
check = 2# this variable stores the number we will be checking to see whether or not it's prime.
# "check" variable is refenced on line 59.

primes = []# this will become a list of prime numbers (referenced on line 58)

def list_strip(lists):
    listout = lists
    if str(type(lists)) != "<class 'list'>":
        sys.stderr.write("\n Input to 'list_strip' function must be a list. instead a " + str(type(lists)) + " input was received. \n")
        return lists
    i = 0
    while True:
        if str(range(0, 9)) in str(lists[i]):
            listout[i] = int(lists[i].strip())
        else:
            sys.stderr.write("\n 'list_strip()' function's input is a list which contains some non numeric values, which may cause problems.\n")
        i += 1
        if i >= len(lists):
            return listout


print('Press "C" to continue where you left off.')
print('Press "N" to start from beginning.')
mode = input(': ')
mode = mode.lower()

if "c" in mode:
    save = open("output.txt", "r+")
    indexsave = open("index.txt", "r+")
    primes = list_strip(save.readlines())
    check = int(primes[-1]) + 2
    index = int(indexsave.read())
    
    save = open("output.txt", "a")

else:
    save = open("output.txt", "w+")
    indexsave = open("index.txt", "w+")

def dec(num):#{
    if round(num) == num:
        return False
    else:
        return True
# this function checks to see if a number is a decimal.
#}

def isprime(num):#{
    # The function "isprime()" can either return "True" or "False", "True" means that the number is prime
    # and "False" means the number is composite


    global primes   
    if dec(num) == True:
        sys.stderr.write("\n input to 'isprime()' is a decimal \n")
        return False
        # the above if statement says that if a the number put into isprime function is a decimal, return "Error".

    elif num == 1:
        return False
    # My algorithm says that "1" is prime, which is false. so I made an exception. 
    # For information on why 1 is composite go to the URL below.
    # https://blogs.scientificamerican.com/roots-of-unity/why-isnt-1-a-prime-number/

    elif num == 2 or num == 3:
        return True
    # I previously had some issues with my algorithm, saying that "2" is not a prime number
    # so I had to write in an exception for it; as above. 

    elif str(num)[-1] == "5" and num > 5:
        return False
        
    a = 0
    b = 2
    while 1 == 1:

        if dec(num / b) == False:# This if statement checks to see if the input number divided by the variable "a" is a decimal 
        #function "dec()" is defined on line 32
        #(variable "b" is defined on line 64) 
            return False

        elif b > ceil(sqrt(num)):
            # "ceil" function (imported on line 1) rounds up. for example "ceil(1.4)" would output "2".
            # "sqrt" function (imported on line 1) finds the square root of a number. for example, sqrt(9) would output "3",
            # ... and sqrt(2) would output "1.41421356..."

             
            return True
            # all things considered, if variable "a" (a is the input of our "isprime" function)
            # ...is greater than or equal to the squareroot of num when num is rounded up to a whole number.

        else:
            if a >= 3 and len(primes) >= 5:
                a += 1
                b = primes[a]
            else:
                b += 1
                continue
#}
#_____________________________end of function_________________________________________________________________________


correct_pass = "46024602"

oldtime = time()
while 1 == 1:#{
    newtime = time()
    if isprime(check):
        primes.insert(-1, check)
        print(f'{primes[len(primes)-2]: ,}')
    #}

    if  check > 3 or dec(check/2):#{
        check += 2
    #}
    else:#{
        check += 1
    #}

    # I've realized that all prime numbers are odd. with the exception of 2.
    # so if I started with 3 and added 2 recursively I would have all odd numbers, and I would get the below sequence.
    # 3, 5, 7, 9, 11, 13...
    # But I mention that 2 is an even prime number, so if I added 2 + 2 recursively I would get al even number.
    # So my above code checks to see if number is divisible by 2, if it is, add 1, which gives us an odd number
    # ...otherwise add 2 to get an odd number
    


    if is_pressed("Q") and is_pressed("R"):#{
    # ^ Function "is_pressed" was imported on line 4. is_pressed can tell whether a key is pressed by user.
        # if user presses "q" key, process terminates and "primes" list (line 9) is saved to output.txt
        passtime = time()
        slep = 1
        passw = getpass(prompt = "password: ", stream = None)
        passtime = (time() - passtime) + slep
        if passw !=  correct_pass:#{
            print("incorrect password " + str(passtime))
            sleep(slep)
            continue
            #}
        else:#{
            primes.insert(0, primes[-1])
            primes.pop(-1)
            # this sorts list of prime numbers form leat to greatest.
            while 1 == 1:#{
                
                if index <= len(primes)-1:#{
                    save.write(str(primes[index]))
                    index += 1
                #}
                else:#{
                    index += 0
                    indexsave.write(str(index))
                    break
                #}
                print("\n" + f'{round(len(primes) / ((time() - oldtime) - passtime), 2): ,}' + " primes found per second")
                print(f'{len(primes): ,}' + " primes found in total")
                print("largest prime found is " + f'{len(str(primes[-1])): ,}' + " digits long. ")
                save.close()
                indexsave.close()
            
#}

