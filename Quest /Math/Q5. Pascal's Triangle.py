

def generate(numRows: int):
    L = [[1]]
    if numRows == 0 or numRows == 1:
        return L
    
    len_L = len(L)
    for i in range(numRows-1):

        len_L +=1
        L_suivant= [0 for i in range(len_L)]
        L_suivant[0] = 1
        L_suivant[len_L-1] = 1

        for j in range(1, len_L-1):
            L_suivant[j] = L[-1][j-1] + L[-1][j]

        L.append(L_suivant)

    return L

print(generate(5))