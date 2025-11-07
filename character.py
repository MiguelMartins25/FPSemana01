# Avaliação Semana 01 #

char1 = input()
A1 = input()
D1 = input()
char2 = input()
A2 = input()
D2 = input()
char3 = input()
A3 = input()
D3 = input()

stats1 = (int(A1),int(D1))
stats2 = (int(A2),int(D2))
stats3 = (int(A3),int(D3))

characters = [[char1,stats1],[char2,stats2],[char3,stats3]]

print(characters)
if A1 > A2 and A1 > A3:
    print("Ataque",char1,A1)
elif A2 > A1 and A2 > A3:
    print("Ataque",char2,A2)
elif A3 > A2 and A3 > A1:
    print("Ataque",char3,A3)
else:
    print("O maior stat de Ataque é repetido entre diferentes characters")
if D1 > D2 and D1 > D3:
    print("Defesa",char1,D1)
elif D2 > D1 and D2 > D3:
    print("Defesa",char2,D2)
elif D3 > D2 and D3 > D1:
    print("Defesa",char3,D3)
else:
    print("O maior stat de Defesa é repetido entre diferentes characters")