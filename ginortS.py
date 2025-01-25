string = input()
lowercase = ''
upppercase = ''
nodd = ''
neven = ''

for s in string:
    if s.isdigit() and not int(s)%2:
        neven += s
    elif s.isdigit() and int(s)%2:
        nodd += s
    elif ord(s) in range(65, 91):
        upppercase += s
    elif ord(s) in range(97, 123):
        lowercase += s
result = ''.join(sorted(lowercase)) + ''.join(sorted(upppercase)) + ''.join(sorted(nodd)) + ''.join(sorted(neven))
print(result)


    