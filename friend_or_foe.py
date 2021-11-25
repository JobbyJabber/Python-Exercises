def friend(x):
    filtered_iterator = filter(isFriend, x)
    filtered = list(filtered_iterator)
    return filtered

    
def isFriend(name):
    if len(name) == 4:
        return True
    return False
        

guys = ["Ryan", "Kieran", "Jason", "Yous"]
result = friend(guys)
print(result)