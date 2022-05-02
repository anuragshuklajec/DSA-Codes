def towerOfHanoi(n, a, b, c):
    if n == 1:
        print('move 1st disk from '+ a + ' to ' + c)
        return
    towerOfHanoi(n-1,a,c,b)
    print('move '+str(n)+' disk from '+ a + ' to ' + c)
    towerOfHanoi(n-1,b,a,c)

n = int(input())
towerOfHanoi(n,'S','H','D')
