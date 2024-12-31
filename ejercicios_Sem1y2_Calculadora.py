import click

@click.command()
@click.option('--cantveces', default=2, prompt='Cantidad de veces que deseas utilizar la calculadora.', type=int)
@click.option('--num1', default=3, prompt='Primer número.', type=float)
@click.option('--operador', default='+', prompt='Operador.', type=str)
@click.option('--num2', default=2, prompt='Segundo número.', type=float)
def calculadora(cantveces, num1, operador, num2):
    for _ in range(cantveces):
        num1 = click.prompt('Primer número', type=float)
        operador = click.prompt('Operador', type=str)
        num2 = click.prompt('Segundo número', type=float)
        
        try:
            if operador == "+":
                resultado = num1 + num2
            elif operador == "-":
                resultado = num1 - num2
            elif operador == "*":
                resultado = num1 * num2
            elif operador == "/":
                if num2 == 0:
                    raise ZeroDivisionError("No puedes realizar una división por 0")
                resultado = num1 / num2
            elif operador == "**":
                resultado = num1 ** num2
            elif operador == "%":
                resultado = num1 % num2
            else:
                print("Operador no válido")
                continue

            print(f"********************************** \n"
                  f"********************************** \n"
                  f"Estas usando la calculadora Karly! \n"
                  f"********************************** \n"
                  f"********************************** \n"
                  f"===== tu primer numero es  {num1} \n"
                  f"-------------------------------------- \n"
                  f"===== la operacion que realizaras es   {operador} \n"
                  f"-------------------------------------- \n"
                  f"===== tu segundo numero es  {num2} \n"
                  f"-------------------------------------- \n"
                  f"-------------------------------------- \n"
                  f"===== tu resultado es  * {resultado} * ")

        except ZeroDivisionError as e:
            print(f"---¡¡¡ERROR!!!--- {e}")

if __name__ == '__main__':
    calculadora()