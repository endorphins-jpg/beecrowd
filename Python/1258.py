all_camisas = []

while True:
    casos_teste = int(input())

    if casos_teste > 0:
        camisas = []

        camisas_b_p = []
        camisas_b_m = []
        camisas_b_g = []
        camisas_v_p = []
        camisas_v_m = []
        camisas_v_g = []

        for i in range(casos_teste):
            nome_cidadao = str(input())
            cor, tamanho = input().split()

            if cor[0] == 'b':
                if tamanho.lower() == 'p':
                    camisas_b_p.append('{} {} {}'.format(cor, tamanho, nome_cidadao))
                elif tamanho.lower() == 'm':
                    camisas_b_m.append('{} {} {}'.format(cor, tamanho, nome_cidadao))
                elif tamanho.lower() == 'g':
                    camisas_b_g.append('{} {} {}'.format(cor, tamanho, nome_cidadao))
            elif cor[0] == 'v':
                if tamanho.lower() == 'p':
                    camisas_v_p.append('{} {} {}'.format(cor, tamanho, nome_cidadao))
                elif tamanho.lower() == 'm':
                    camisas_v_m.append('{} {} {}'.format(cor, tamanho, nome_cidadao))
                elif tamanho.lower() == 'g':
                    camisas_v_g.append('{} {} {}'.format(cor, tamanho, nome_cidadao))
        
        camisas = sorted(camisas_b_p) + sorted(camisas_b_m) + sorted(camisas_b_g) + sorted(camisas_v_p) + sorted(camisas_v_m) + sorted(camisas_v_g)
        all_camisas += camisas + ['']
        
    else:
        all_camisas.pop(-1)
        for i in all_camisas:
            print(i)
        exit()