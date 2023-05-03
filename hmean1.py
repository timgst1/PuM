def hmean(liste):
    sum = 0
    for i in liste:
        sum += 1/i
    
    return len(liste)/sum


a = [1,2,3,4]

print(hmean(a))