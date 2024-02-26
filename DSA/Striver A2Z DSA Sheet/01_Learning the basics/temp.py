def reverse(x: int) -> int:
        revNum = 0 
        isPositive = True
        if x < 0 : isPositive = False
        x = abs(x)
        originalNum = x
        print(originalNum)
        while x>0 :
            lastDigit = x%10
            if not (x==originalNum and lastDigit==0):
                revNum = revNum*10 + lastDigit
            x = int(x/10)
            print(revNum)
        if  -2**31<revNum<2**31-1 :
            return revNum if isPositive else -revNum 
        else : 
            return 0
    
if __name__ == '__main__':
    print(reverse(1534236469))