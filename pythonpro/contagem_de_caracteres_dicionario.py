def contar_caracteres(s):
    """Função que conta os caracteres de uma string

    Ex.:

    >>> contar_caracteres('carlos')
    a: 1
    c: 1
    l: 1
    o: 1
    r: 1
    s: 1
    >>> contar_caracteres('banana')
    a: 3
    b: 1
    n: 2

    :param s: string a ser contada

    """

    # # Solução apresentada no curso
    # caracteres_ordenados = sorted(s)
    #
    # caracter_anterior = caracteres_ordenados[0]
    # contagem = 1
    #
    # for caracter in caracteres_ordenados[1:]:
    #     if caracter == caracter_anterior:
    #         contagem += 1
    #     else:
    #         print(f'{caracter_anterior}: {contagem}')
    #         caracter_anterior = caracter
    #         contagem = 1
    #
    # print(f'{caracter_anterior}: {contagem}')

    # Minha solução
    caracteres = sorted(set(s))

    for _ in caracteres:
        print(f'{_}: {s.count(_)}')


if __name__ == '__main__':
    contar_caracteres('carlos')
    print()
    contar_caracteres('banana')
    print()
    contar_caracteres('aaaccbbffffff')
