
list = [16,16,56,124,254,16,16,56]
list2 = []
longest = 0
for b in list:
    a = (bin(b)[2:])
    list2.append(a)
    if len(a) > longest:
        longest = len(a)
for c in list2:
    spaces = longest-len(c)
    print(spaces*' '+c)
