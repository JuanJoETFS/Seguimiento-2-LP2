# 🧮 Listas (Arrays) con Cola en Python

Este repositorio presenta una **implementación práctica y didáctica** del concepto de **listas (arrays)** utilizando una **estructura de cola (Queue)** en Python.  
El propósito es comprender cómo funcionan las operaciones básicas de una cola —**enqueue**, **dequeue**, **peek** y **isEmpty**— aplicadas sobre listas.

---

## 📘 Contenido del repositorio

- `README.md` → Incluye este repositorio que estas leyendo ahora mismo.😁 
- `notebook.ipynb` → Cuaderno interactivo con explicaciones paso a paso, ideal para comprender y ejecutar el código directamente desde **Jupyter Notebook**.
- `Pagina web educativa` → Una pagina web estatica, donde hay temas desde introducciones hasta cuestionarios sobre listas como colas.
- `Ejemplo en pyhon (.py)` → Un ejemplo de estas listas usando pyhton
---

## 🧠 Conceptos clave

- **Listas (Arrays):** estructuras dinámicas que permiten almacenar y manipular colecciones de datos.  
- **Cola (Queue):** estructura **FIFO (First In, First Out)**, donde el primer elemento en entrar es el primero en salir.  
- **Operaciones principales:**
  - `enqueue()` → Agrega un elemento al final de la cola.  
  - `dequeue()` → Elimina el primer elemento de la cola.  
  - `peek()` → Muestra el primer elemento sin eliminarlo.  
  - `isEmpty()` → Verifica si la cola está vacía.  

---

## 🧩 Ejemplo breve

```python
from cola_listas import Cola

cola = Cola()
cola.enqueue("A")
cola.enqueue("B")
cola.enqueue("C")

print(cola.dequeue())  # 👉 Salida: A
print(cola.peek())     # 👉 Salida: B
```


💡 Requisitos
Asegúrate de tener instalado Python 3.8+ y Jupyter Notebook:
pip install jupyter
Para abrir el notebook:
jupyter notebook notebook.ipynb

🎯 Objetivo educativo

Este proyecto está orientado a estudiantes y entusiastas de la programación que deseen comprender estructuras de datos básicas desde una perspectiva práctica, con ejemplos claros y código limpio.

📄 Licencia

Este proyecto se distribuye bajo la licencia MIT, lo que significa que puedes usarlo, modificarlo y compartirlo libremente, siempre dando el crédito correspondiente.

Autor: [Juan Jose Restrepo]
📅 Año: 2025
🐍 Lenguajes principales:html, jupyter, python.
