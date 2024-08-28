from enum import Enum

class Carro:
    @staticmethod
    def acelerar(velmax):
        potencias = {pot.name: pot.value for pot in Potencia}
        if velmax in potencias: print(f"Velocidade máxima de {potencias.get(velmax)}")
        else: return print("Opss! Esse modelo não existe!")

class Potencia(Enum):
    V8 = 260
    V10 = 280
    V12 = 300

potencia_motor = input("Qual é potencia do seu carro: V8, V10 ou V12?")
Carro.acelerar(potencia_motor)

