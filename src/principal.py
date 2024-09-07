from cuenta_bancaria import CuentaBancaria

if __name__ == '__main__':
    cuenta = CuentaBancaria("Wendy Fonseca", "5072317169", 200000)

    assert cuenta.get_titular() == "Wendy Fonseca"

    cuenta.set_titular("Karen Tacuma")
    assert cuenta.get_titular() == "Karen Tacuma"

    assert cuenta.get_numero_cuenta() == "5072317169"

    assert cuenta.get_saldo() == 200000

    cuenta.ingresar(50000)
    assert cuenta.get_saldo() == 250000

    cuenta.ingresar(20000)
    assert cuenta.get_saldo() == 270000

    cuenta.retirar(80000)
    assert cuenta.get_saldo() == 190000

    cuenta.retirar(150000)
    assert cuenta.get_saldo() == 40000

    cuenta.set_tipo_interes(0)
    assert cuenta.calcular_interes() == 0

    cuenta.set_tipo_interes(5)
    assert cuenta.calcular_interes() == 2000  # 5% de 40000

    cuenta.set_tipo_interes(2)
    assert cuenta.calcular_interes() == 800  # 2% de 400000

    cuenta.set_tipo_interes(12)
    assert cuenta.calcular_interes() == 4800  # 12% de 40000

    print("Todas las pruebas fueron correctas")