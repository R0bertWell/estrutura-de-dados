def funcao_que_lanca_excecao():
    raise Exception('Erro da função')


def funcao_que_nao_lanca_erro():
    return 0


if __name__ == "__main__":
    try:
        funcao_que_lanca_excecao()
    except Exception as e:
        print(e.args)
    else:
        print('Não deu erro')
    finally:
        print('Sempre executa')

    try:
        funcao_que_nao_lanca_erro()
    except Exception as e:
        print(e.args)
    else:
        print('Não deu erro')
    finally:
        print('Sempre executa')
