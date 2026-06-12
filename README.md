# 🧠 Máquina de Turing

Implementación de una **Máquina de Turing (MT)** en Python, con una interfaz gráfica para definir y ejecutar simulaciones paso a paso.

---

## 📌 Descripción

Una Máquina de Turing es el modelo computacional más simple capaz de definir el concepto de **computabilidad**. Está compuesta por:

- Un conjunto finito de **estados**
- Un **alfabeto** de entrada y un alfabeto de cinta (que incluye el símbolo blanco)
- Una **función de transición** δ: Q × Γ → Q × Γ × {Izquierda, Derecha}
- Un **estado inicial**
- Uno o más **estados de aceptación**

Este proyecto simula su funcionamiento: dada una cadena de entrada y un conjunto de reglas de transición, la máquina recorre la cinta, lee y escribe símbolos, y determina si la cadena es **aceptada** o **rechazada**.

---

## 📂 Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `maquina_turing.py` | Lógica principal de la Máquina de Turing: estados, transiciones, ejecución sobre la cinta. |
| `interfaz.py` | Interfaz gráfica (Tkinter) para definir la máquina, ingresar la cadena y visualizar la ejecución. |

---

## ⚙️ Requisitos

- Python 3.9 o superior
- Tkinter (incluido por defecto en la mayoría de instalaciones de Python)

---

## 🚀 Instalación

\`\`\`bash
git clone https://github.com/Fernando13423/Maquina-de-Turing.git
cd Maquina-de-Turing
\`\`\`

---

## ▶️ Uso

Ejecutar la interfaz gráfica:

\`\`\`bash
python interfaz.py
\`\`\`

Desde la interfaz se puede:

- Definir o seleccionar una máquina de Turing (estados, alfabeto y transiciones).
- Ingresar la cadena de entrada a evaluar.
- Ejecutar la simulación paso a paso o de forma continua.
- Visualizar el contenido de la cinta y el estado actual.
- Obtener el resultado: cadena **aceptada** o **rechazada**.

---

## 🔍 Cómo funciona

- La cade
