def contar_caracteres(s):
    """Função que conta os caracteres de uma string

    Ex.:

    >>> contar_caracteres('carlos')
    {'a': 1, 'c': 1, 'l': 1, 'o': 1, 'r': 1, 's': 1}
    >>> contar_caracteres('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada
    :return: dictionary

    """
    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return dict(sorted(resultado.items(), key=lambda kv: kv[0]))


if __name__ == "__main__":
    print(contar_caracteres("carlos"))
    print(contar_caracteres("banana"))
    print(contar_caracteres("aaaccbbffffff"))
