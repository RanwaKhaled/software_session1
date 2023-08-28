dim = int(input('enter the dimension for you pyramids (between 1 and 8): '))
while (dim<1 or dim>8):
    dim = int(input('please enter a number between 1 and 8: '))
for i in range(dim,0,-1):
    #spaces
    for j in range(i-1,0,-1):
        print(' ',end="")
    #hashes
    for k in range(0,dim-(i-1),1):
        print('#',end="")
    print('  ',end='')
    for k in range(0,dim-(i-1),1):
        print('#',end="")
    print('')