#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento
valor=(float(input('Qual o valor da compra: ')))
pagamento=(int(input('Informe a forma de pagamento\n'
                     '[ 1 ] à vista no pix ou dinheiro\n'
                     '[ 2 ] à vista no crédito ou débito\n'
                     '[ 3 ] 2x no cartão de crédito\n'
                     '[ 4 ] 3x ou mais no cartão de crédito\n'
                     'Sua opção: ')))
if pagamento==1:
    preço = valor - ((valor * 10) / 100)
    print(f'Sua opção foi pagar à vista no píx ou dinheiro, então ganha 10% de desconto, sua compra ficará no valor de'
    f' {preço}')
elif pagamento==2:
    preço =valor-((valor*10)/100)
    print(f'Sua opção foi pagar à vista no credito ou no debito, então ganha 5% de desconto, sua compra ficará no valor'
    f' de {preço}')
elif pagamento==3:
    print(f'Sua opção foi pagar 2x no cartão, sua compra ficará no valor de 2x de{valor/2}')
if pagamento==4:
    parcelas= int(input('Em quantas vezes deseja parcelar? '
                      'Sua escolha: '))
    preço= ((valor*20)/100)+valor
    print(f'Você decidiu pagar em {parcelas}x no cartão de crédito, sua compra de {valor} ficará {preço}, com {parcelas}'
          f' parcelas de {preço/parcelas}')
else:
    print(f'\033[31mOpção invalida tente novamente.')