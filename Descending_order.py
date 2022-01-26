from numpy import sort


def descending_order(num):
    liczba = []
    for i in str(num):
        liczba.append(i)
    sorted_list = sorted(liczba, reverse = True) 
    s = ''
    s = s.join(sorted_list)
    s = int(s)
    return s

    
w = 42145
print(descending_order(w))