def lenDigits(x): 
    x = abs(x)

    if x < 10:
        return 1

    return 1 + lenDigits(x / 10)



def crosssum(integer):
    par = lenDigits(integer)
    sum = 0
    rangeparameter = len(str(integer))
    for i in range(0,par):
        sum += integer % 10
        integer = integer // 10
    
    return sum

print(crosssum(13423246464234567876543290091908912837120391023912309172308128585123123))
