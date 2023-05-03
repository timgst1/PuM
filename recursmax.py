def rec_max(liste):
    if len(liste) == 1:
        return liste[0]
    r_max = rec_max(liste[1:])
    if liste[0] < r_max:
        return r_max
    else:
        return liste[0]

b = [1,2,3,4,9,5,6,7,9]

print(rec_max(b))