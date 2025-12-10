
print(not([]))


def isValid( s: str) -> bool:
    ouverts = ['(', '[','{']
    fermes = [ ')',']','}']
    paire = {'(':')', '[':']','{':'}','': 0}
    historique_ouverts = []
    a = 0
    b = 0
    c = 0
    pointeur = ''
    for lettre in s:
        if lettre in fermes and paire[pointeur]!=lettre:
            return False
        if lettre in ouverts:
            pointeur = lettre
            historique_ouverts.append(lettre)
        if lettre in fermes and len(historique_ouverts)>1:
            historique_ouverts.pop()
            pointeur = historique_ouverts[-1]

        if lettre == '(':
            a+=1
        if lettre == '[':
            b+=1
        if lettre == '{':
            c+=1 

        if lettre == ')':
            a-=1
        if lettre == ']':
            b-=1
        if lettre == '}':
            c-=1

    return (a==b==c==0)


def isValidPRO( s: str) -> bool:
    brackets = {')':'(', '}': '{', ']': '['}
    stack = []

    for c in s:
        if stack and c in brackets and brackets[c] == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    return len(stack) == 0

