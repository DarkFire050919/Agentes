class Ambiente:
    def __init__(self):   
        self.cuartos = [1, 1]  # crea los cuartos 1 = sucio, 0 = limpio

    def step(self, posicion: int) -> int:
        #verifica si esta limpio o sucio
        return self.cuartos[posicion]

    def aplicar(self, posicion: int, suciedad: int):
        #cambia el estado del cuarto
        self.cuartos[posicion] = suciedad


class AgenteAspiradora:
    def __init__(self):   #inicializa el agente
        self.posicion = 0
        self.izq = -1
        self.der = 1

    def sensar(self, ambiente: Ambiente) -> int:
        estado = ambiente.step(self.posicion)                            #verifica el ambiente y regresa el estado si esta limpio o sucio
        print(f"Sensado posición {self.posicion}: {estado}")
        return estado

    def actuar(self, ambiente: Ambiente, estado: int):
        # Limpiar
        if estado == 1:              # si esta sucio lo limpia
            print("Limpiar")
            ambiente.aplicar(self.posicion, 0)          #va a aplicar 0 que es limpio

        # Moverse
        print("Moviéndose", end=" ")
        if self.posicion == 0:
            print("a la derecha")            #se mueve dependiendo si esta limpio o sucio
            self.posicion += self.der
        else:
            print("a la izquierda")
            self.posicion += self.izq


# Crear objetos
ambiente_obj = Ambiente()
aspiradora_obj = AgenteAspiradora()

# Simulación
for _ in range(5):
    estado = aspiradora_obj.sensar(ambiente_obj)
    aspiradora_obj.actuar(ambiente_obj, estado)
