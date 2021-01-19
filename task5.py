print ("введите выручку")
viruchka = int(input())
print ("введите издержку")
izderzka = int(input())
if viruchka > izderzka:
    print ("прибыль")
    rent = (viruchka-izderzka) / viruchka
    print("рентабельность = "+ str(rent))
    print("введите количество сотрудников")
    sotrudniki = int(input())
    rent = rent/sotrudniki
    print("прибыль на сотрудника = " + str(rent))
else:
    print("убыток")
