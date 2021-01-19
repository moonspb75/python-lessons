print("введите километры в первый день")
a = float(input())
print(" введите желаемое количество километров")
b = float(input())
resultat = a
day = 1
while resultat < b :
    resultat = resultat * 1.1
    day = day + 1
print(int(day))