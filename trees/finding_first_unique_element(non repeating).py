def unique(name):
    count = collections.Counter(name)
    for ch in name:
        if count[ch] == 1:
            return name.index(ch)
        else:
            return -1
            
 #Driver code:
name = "geeks"
unique(name)
