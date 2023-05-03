def conway_check(num):
    answer = []
    temp = 0
    while num > 0:
        answer.append(num%10)
        num //= 10

    if to_list_and_compare(answer.reverse()):
        for i in range(1,11):
            for y in answer[:i]:
                temp += answer[y]*10**(y+1)

            if temp // i == 0:
                temp = 0
            else:
                return False
        return True
    

def to_list_and_compare(answer):
    liste = [0,1,2,3,4,5,6,7,8,9]
    
    return answer.sort() == liste


print(conway_check(3816547290))