print('=== SISTEMA CALCULO EXATO ===')
try:
    valor_compra = float(input('Digite o valor da compra do restaurante: R$ '))
    taxa_servico = int(input('Digite o valor da % da taxa de serviço: '))
    couvert = float(input('Insira o valor do couvert, caso não tenha insira "0" : R$ '))

    if valor_compra < 0 or couvert < 0:
        print("Erro: Os valores da compra e do couvert não podem ser negativos.")
    else:
        valor_taxa = (valor_compra * (taxa_servico / 100))
        valor_total = valor_taxa + valor_compra + couvert

        print('Valor da compra: R$ {:.2f}'.format(valor_compra))
        print('Taxa de serviço: {} %'.format(taxa_servico))
        print('Couvert: R$ {:.2f}'.format(couvert))
        print('O Valor que vai ser pago é: R$ {:.2f}'.format(valor_total))
        print('Obrigado, volte sempre')
except ValueError:
    print("Erro: Certifique-se de inserir valores válidos (números) para a compra e o couvert.")