# set of Domino tiles
def dominoes_set(n):
    # left side of tiles
    print('Dominoes sets:')
    for left in range(n):
        # right side of tiles
        for right in range(left,n):
            print('['+str(left)+'|'+ str(right)+ ']', end=' ')
        print()
    print()

#Double-12 Dominoes
dominoes_set(13)
#Double-6 Dominoes
dominoes_set(7)
