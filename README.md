#  Máquina de Turing

Implementación de una **Máquina de Turing (MT)** en Python, con una interfaz gráfica para definir y ejecutar simulaciones paso a paso.

---

##  Descripción

Una Máquina de Turing es el modelo computacional más simple capaz de definir el concepto de **computabilidad**. Está compuesta por:

- Un conjunto finito de **estados**
- Un **alfabeto** de entrada y un alfabeto de cinta (que incluye el símbolo blanco)
- Una **función de transición** δ: Q × Γ → Q × Γ × {Izquierda, Derecha}
- Un **estado inicial**
- Uno o más **estados de aceptación**

Este proyecto simula su funcionamiento: dada una cadena de entrada y un conjunto de reglas de transición, la máquina recorre la cinta, lee y escribe símbolos, y determina si la cadena es **aceptada** o **rechazada**.

---

## Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `maquina_turing.py` | Lógica principal de la Máquina de Turing: estados, transiciones, ejecución sobre la cinta. |
| `interfaz.py` | Interfaz gráfica (Tkinter) para definir la máquina, ingresar la cadena y visualizar la ejecución. |

---

