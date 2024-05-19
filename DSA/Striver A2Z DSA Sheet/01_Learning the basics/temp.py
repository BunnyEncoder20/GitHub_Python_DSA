def reverseInteger(num : int) -> int:
    reverseNum = 0
    
    if num < 0:
        num = abs(num)
        isNegative = True
        
    while num > 0:
        lastDigit = num%10
        num = num//10
        reverseNum = reverseNum*10+lastDigit
        
    if -2**31 < reverseNum < 2**31-1:
        return reverseNum if isNegative == False else -reverseNum
    else :
        return 0

if __name__=='__main__':
    x = int(input("x:"))
    print(reverseInteger(x))