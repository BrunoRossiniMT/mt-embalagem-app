def calcular():
    print("Calculadora MT Embalagem")
    print("-----------------------")

    quantidade = int(input("Quantidade de sacolas: "))
    preco_unitario = float(input("Preço por unidade: "))

    total = quantidade * preco_unitario

    print(f"\nValor total: R$ {total:.2f}")


