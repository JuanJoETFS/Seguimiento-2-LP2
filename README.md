# 🧮 Listas (Arrays) con Cola en Python

Este repositorio presenta una **implementación práctica y didáctica** del concepto de **listas (arrays)** utilizando una **estructura de cola (Queue)** en Python.  
El propósito es comprender cómo funcionan las operaciones básicas de una cola —**enqueue**, **dequeue**, **peek** y **isEmpty**— aplicadas sobre listas.

---

## 📘 Contenido del repositorio

- `cola_listas.py` → Código fuente con un ejemplo completo de uso de listas como colas en Python.  
- `notebook.ipynb` → Cuaderno interactivo con explicaciones paso a paso, ideal para comprender y ejecutar el código directamente desde **Jupyter Notebook**.

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
