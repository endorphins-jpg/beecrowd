while True:
    user_input = input()

    if user_input == '0':
        exit()
    else:
        Q, D, P = user_input.split()
        Q = int(Q)
        D = int(D)
        P = int(P)

        x = (P*D*Q/(P*Q-Q*Q))
        qt = int(x*Q)
        if qt == 1:
            print("1 pagina")
        else:
            print("{} paginas".format(qt))