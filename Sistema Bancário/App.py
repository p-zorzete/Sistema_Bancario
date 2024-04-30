menu_acesso = """
[1]Sacar
[2]Depositar
[3]Extrato
[0]Sair
"""

saldo = 0
saque = 0
numero_saques=0
limite_saques=3

while True:
      operacao = input(f"Escolha a operação desejada: {menu_acesso}")

      if (operacao == "1"):
            if (numero_saques == limite_saques):
                  print ("Limite de saques diários alcançados!")  
            else : 
                  valor_sacado = input("Valor a ser sacado: ")
                  valor_sacado = float(valor_sacado)
                  saque += valor_sacado
                  if (valor_sacado > saldo) :
                        print ("Valor de saldo insuficiente!")
                  elif (saque > 500):
                        print("Limite de R$ 500 de saque diário")
                        saque -= valor_sacado
                        print(f"Valor já sacado: {saque:.2f}")
                  else :
                        saldo -= valor_sacado
                        numero_saques += 1

      elif (operacao == "2"):
            valor_deposito = input("Valor a ser depositado: ")
            valor_deposito = float(valor_deposito)
            saldo += valor_deposito
      
      elif (operacao == "3"):
            print(f"Extrato Bancário: R$ {saldo:.2f}")

      elif (operacao == "0"):
            break
      else :
            print("Operação não encontrada!")
      print()


      
