#Will make a list of your given valu
d = []

#Will sum up
c = 0
while True:
    print('Give me a number')
    a = input()
    if a == '':
        break
    else:
        b = int(a)
        c = c + b
        d.append(b)
#Will give the output
print('You have putted ' + d)
print('And, sum of them 'c)
