a = -1

try:
    if a<0:
        assert False, '數字要大於0'
    print(a)
except AssertionError as msg:
    print(msg)
except :
    print('error')
print('continue')
