score = input('Enter score: ')
try:
    x = float(score)
except:
    print('Pls give a numeric value!!!')
    quit()
if 0.0 <= x <= 1.0:
    if x >= 0.9:
        print('A')
    elif x >= 0.8:
        print('B')
    elif x >= 0.7:
        print('C')
    elif x >= 0.6:
        print('D')
    elif x < 0.6:
        print('F')
else:
    print('The score that you gave is out of range!!!')
