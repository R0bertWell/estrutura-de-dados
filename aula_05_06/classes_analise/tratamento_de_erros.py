def funcao_que_lanca_excecao():
    raise Exception('Erro da função')
    # return 'Oi'


if __name__ == '__main__':
    try:
        funcao_que_lanca_excecao()
    except Exception as e:
        print(e.args)
    else:
        print('Não deu erro')
    finally:
        print('Executou anyway')

