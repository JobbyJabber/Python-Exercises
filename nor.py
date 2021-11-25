a = 6
b = 9 
#a i b musza miec wartosci logiczne
def nor(a, b):
    if not a and not b:
        return True
    return False

print(nor(a>b, a==b))