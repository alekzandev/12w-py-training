import click
import random

@click.command()
@click.option('--num1', default=0, prompt='Número que crees correcto.', type=float)

def adivinador(num1):
    #@click.prompt("Ingresa el número que crees correcto.", type=float)

    num_real = random.randint(1,10)
    almacena = []
    intentos = 1
   
    
    while True:
                
            if num1 < num_real:
                print(f"============================================ \n"
                f"Tu numero es {num1} y es menor al numero correcto \n"
                f"==============================================")
                almacena.append(num1)
                intentos = intentos+1
            elif num1 > num_real:
                    print(f"============================================ \n"
                        f"Tu numero es {num1} y es mayor al numero correcto \n"
                        f"==============================================")
                    almacena.append(num1)
                    intentos = intentos+1
            else:
                    almacena.append(num1)
                    print(f"============================================ \n"
                    f"============================================ \n"
                    f"Tu numero es {num1} CORRECTO!!!, ERES UN FELIZ GANADOR \n"
                    f"-------------------------------------------\n" 
                    f"Los numeros que ingresaste son: {almacena}")
                        
                    intentos = intentos+1
                    
                    intentos_new = click.prompt("quieres seguir jugando ingresa True o False", type=bool)
                    if intentos_new == False:
                        break
                            
            num1 = click.prompt("Ingresa el número que crees correcto.", type=float)
    
        
        
if __name__ == '__main__':
    adivinador()
    