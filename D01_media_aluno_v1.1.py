from time import sleep
while True:
    print(' = = = = SISTEMA DE MÉDIA DAS NOTAS = = = = = =')
    aluno = str(input('Digite o nome do aluno(a): ')).strip()#uso o .strip() para remover os espaços no inicio e no fim da string a ser inserida.
    # inserindo as notas.
    n1 = float(input('Insira a 1ª nota do aluno(a): '))
    n2 = float(input('Insira a 2ª nota do aluno(a): '))
    n3 = float(input('Insira a 3ª nota do aluno(a): '))
    media = (n1 + n2 + n3) / 3
    print('processando ...') # inserindo um print + um sleep pra dar a ideia que o PC está preparando a resposta.
    sleep(1)

    #Retornando para o usuario as medias.
    if media >= 7:
        print('Aprovado com média {:.2f} !!!, o {} concluiu a diciplina com um bom aproveitamento'.format(media, aluno))
    elif 5 <= media < 7:
        print('A média do {} foi {:.2f}. E o mesmo está de recuperação, precisa refazer uma prova para a nova analise de seus conhecimentos'.format(aluno, media))
    else:
        print('A média do {} foi {:.2f}. E o mesmo terá que reprovar a diciplina para que possa adquirir o conhecimento desejado'.format(aluno, media))
    sleep(0.5)

    #Aqui começo o verificador para continuar ou não no programa.
    nova_ope = input('Deseja calcular a média de um novo aluno? S para Sim, N para Não: ').strip().lower()

    if nova_ope == 'n':
        break
    elif nova_ope != 's':
        print('Opção inválida. Por favor, digite "S" para Sim ou "N" para Não.')
print('Espero que tenha gostado -> Volte Sempre ! <-')
