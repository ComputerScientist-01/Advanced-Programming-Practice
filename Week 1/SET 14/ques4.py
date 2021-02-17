def sumofDigits(n):
    sum = 0
    for digit in str(n):   
        sum += int(digit)        
    print(sum)

n =input()
sumofDigits(n)


