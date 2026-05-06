# s = 'abc'

# def myfun(s:str)->str:
# 	l = list(s.lower())
# 	for i in range(len(l)):
# 		if i%2==0:
# 			l[i] = l[i].upper()
# 	return ''.join(l)

# print(myfun(s))


# input = abc
# output = aBc

def odd_upper_case(s:str)->str:
    l = list(s.lower())
    for i in range(len(l)):
        if i%2 != 0 :
            l[i] = l[i].upper()
    return ''.join(l)

s = 'abc'
print(odd_upper_case(s))