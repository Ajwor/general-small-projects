#Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
#the Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones

#define the function to generate the numbers:
def fibonacci(num):
    sequence = [0]
    if num > 0:
        sequence.append(1)
    for i in range(num-1):
        sequence.append(sequence[-1]+sequence[-2])
    return sequence
        
while True:
    try:
        n = int(input('To what number n would you like the Fibonacci sequence up to Fn? (Where F0=0 and F1=1) '))
    except:
        print('That is not a valid entry. Please type in a positive integer.')
    else:
        if n < 0:
           print('That is not a valid entry. Please type in a positive integer.') 
        else:
            break

print(f'The Fibonacci sequence up to n = {n} is:')
print(fibonacci(n))
