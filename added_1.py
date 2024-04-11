def move_A_to_C(n,a,b,c):
    if n == 1:
        print(a,'->',c)
    else:
        move_A_to_C(n-1,a,c,b)
        move_A_to_C(1,a,b,c)
        move_A_to_C(n-1,b,a,c)
