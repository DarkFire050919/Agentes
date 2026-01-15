# Aspiradora 1 – Documentación Técnica

## Visión general
El archivo **Aspiradora 1.py** implementa una simulación simple de un robot aspirador en un ambiente con dos cuartos. El robot percibe la suciedad en su posición actual y decide limpiar, mover a la izquierda o mover a la derecha.

## Componentes principales

### 1. Clase `Ambiente`
- **Atributos**
  - `cuartos`: lista que representa el estado de limpieza de cada cuarto (1 = sucio, 0 = limpio).

- **Métodos**
  - `step(posicion)`: Devuelve el estado del cuarto en la posición dada.
  - `aplicar(posicion, suciedad)`: Cambia el estado de limpieza del cuarto.

### 2. Clase `AgenteAspiradora`
- **Atributos**
  - `posicion`: Índice actual del robot (0 o 1).
  - `izq`, `der`: Valores de desplazamiento a la izquierda y derecha.

- **Métodos**
  - `sensar(ambiente)`: Obtiene el estado de la posición actual del ambiente.
  - `actuar(ambiente, estado)`: Limpia si está sucio y se mueve a la otra celda.

## Ejemplo de ejecución
```python
ambiente_obj = Ambiente()
aspiradora_obj = AgenteAspiradora()

for _ in range(5):
    estado = aspiradora_obj.sensar(ambiente_obj)
    aspiradora_obj.actuar(ambiente_obj, estado)
```
Esto simula 5 ciclos de detección y acción en los dos cuartos.

## Notas de diseño
- El robot siempre alterna entre los cuartos, moviéndose a la derecha cuando está en posición 0 y a la izquierda cuando está en posición 1.
- La lógica de limpieza es sencilla: si el cuarto está sucio (`estado == 1`), se limpia.

---

*Generado automáticamente por **CodeDocumentationAgent**.*