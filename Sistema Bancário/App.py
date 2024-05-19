menu_acesso = """
[1]Sacar
[2]Depositar
[3]Extrato
[4]Novo usuário
[5]Nova conta corrente
[0]Sair
"""

LIMITE_SAQUES=3
AGENCIA="0001"

saldo = 0
extrato=""
numero_saques= 0
limite = 500
lista_usuarios = []
conta = []

def sacar(*,saldo,extrato,limite,numero_saques,limite_saques):

      valor_sacado = float(input("Valor a ser sacado: "))
      saque_diario = 0
      saque_diario += valor_sacado

      if valor_sacado > saldo :
            print ("Valor de saldo insuficiente!")
      elif saque_diario > limite:
            print("Erro! Limite de R$ 500 de saque diário já alcançado")
            saque_diario -= valor_sacado
            print(f"Valor já sacado: {saque_diario:.2f}")
      elif numero_saques >= limite_saques:
            print("Erro! Limite de saques diários já alcançados")
      elif valor_sacado > 0 :
            saldo -= valor_sacado
            extrato += f"Saque: R$ {valor_sacado:.2f}\n"
            numero_saques += 1
            print(numero_saques)    
      else :
            print("Erro! Valor inserido é inválido")

      return saldo,extrato,numero_saques

def visualizar_extrato(saldo,/,*,extrato):
      if not extrato:
            print("Não houveram movimentações na conta!")
      else :
            print(f"\n{extrato}")

      print(f"Saldo Bancário: R$ {saldo:.2f}") 

def depositar(saldo,extrato,/):
      valor_deposito = float(input("Valor a ser depositado: "))
      if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
      else :
            print("Erro! Valor inserido é inválido")
      
      return saldo, extrato
            
def criar_usuario(lista_usuarios):

      cpf = input("Informe o seu CPF:")
      novo_usuario = filtrar_usuario(cpf, lista_usuarios)

      if novo_usuario == False:
            print("Já existe um usuário com esse CPF!")
            return
      else:
            nome = input("Informe o seu nome:")
            data_nascimento = input("Informe a sua data de nascimento:")
            rua = input("Informe a sua rua:")
            bairro = input("Informe o seu bairro:")
            numero = input("Informe o numero da sua residência:")
            cidade_estado = input("Informe a sua cidade e estado ex(Osasco/SP):")

      lista_usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"endereco":{"rua":rua,"bairro":bairro,"numero":numero,"cidade_estado":cidade_estado}})

def filtrar_usuario(cpf,lista_usuarios):      
     for i in range(0, len(lista_usuarios)):
        usuario = lista_usuarios[i]

        if (cpf == usuario['cpf']):
              return False
            
def criar_conta_corrente(agencia,numero_conta,lista_usuarios):
      cpf = input("Informe o seu CPF:")
      usuario = filtrar_usuario(cpf, lista_usuarios)

      if usuario == False:
            print("Conta criada com sucesso!")
            return {"agencia":agencia,"numero_conta":numero_conta,"usuario":usuario}
      else:
            print("Usuário não encontrado!Operação encerrada!")

while True:
      operacao = input(f"Escolha a operação desejada: {menu_acesso}")

      if (operacao == "1"):
            saldo,extrato,numero_saques = sacar(
                  saldo=saldo,
                  extrato=extrato,
                  limite=limite,
                  numero_saques=numero_saques,
                  limite_saques=LIMITE_SAQUES
            ) 

      elif (operacao == "2"):
            saldo,extrato = depositar(saldo,extrato)
      
      elif (operacao == "3"):
            visualizar_extrato(saldo,extrato=extrato)

      elif (operacao == "4"):
            criar_usuario(lista_usuarios)

      elif (operacao == "5"):
            numero_conta = len(conta) + 1
            criar_conta_corrente(AGENCIA,numero_conta,lista_usuarios)

      elif (operacao == "0"):
            break
      else :
            print("Operação não encontrada!")
      print()


      
