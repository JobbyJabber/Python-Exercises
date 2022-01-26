#zadanie 1 rozwiazanie nr1

words = ['oko', 'grzybobranie', 'żółw', 'jaźń', 'zażółcone krzewy', 'hipodrom', 'szczęki', 'kurs poprawkowy']
polish = 'ą ć ę ł ń ó ś ź ż'.split()
lista = []
for i in words:
    tmp = []
    for x in i:
        if x in polish:
            tmp.append(x)
    lista.append(tmp)
print([len(l) for l in lista])

#zadanie 1 rozwiazanie nr2
# words = ['oko', 'grzybobranie', 'żółw', 'jaźń', 'zażółcone krzewy', 'hipodrom', 'szczęki', 'kurs poprawkowy']
# polish = 'ąćęłńóśźż'

# output = [sum(j in polish for j in i) for i in words]
# print(output)


