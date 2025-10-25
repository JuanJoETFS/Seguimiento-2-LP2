# Ejemplo real: Sistema de gestión de pedidos de restaurante
from collections import deque
import time
import random

class SistemaPedidos:
    def __init__(self):
        self.pendientes = deque()  # Cola de pedidos pendientes
        self.completados = []     # Lista de pedidos completados
        self.numero_pedido = 1
    
    def agregar_pedido(self, cliente, items):
        """Agrega un nuevo pedido a la cola"""
        pedido = {
            'numero': self.numero_pedido,
            'cliente': cliente,
            'items': items,
            'hora': time.strftime("%H:%M:%S"),
            'estado': 'pendiente'
        }
        self.pendientes.append(pedido)
        self.numero_pedido += 1
        print(f"📝 Pedido #{pedido['numero']} agregado para {cliente}")
        return pedido['numero']
    
    def procesar_siguiente_pedido(self):
        """Procesa el siguiente pedido en la cola"""
        if not self.pendientes:
            print("⚠️ No hay pedidos pendientes")
            return None
        
        pedido = self.pendientes.popleft()
        pedido['estado'] = 'completado'
        pedido['hora_completado'] = time.strftime("%H:%M:%S")
        self.completados.append(pedido)
        
        print(f"✅ Pedido #{pedido['numero']} completado para {pedido['cliente']}")
        return pedido
    
    def mostrar_estado(self):
        """Muestra el estado actual del sistema"""
        print(f"\\n📊 ESTADO DEL SISTEMA")
        print(f"🔄 Pedidos pendientes: {len(self.pendientes)}")
        print(f"✅ Pedidos completados: {len(self.completados)}")
        
        if self.pendientes:
            print("\\n📋 Próximos pedidos:")
            for i, pedido in enumerate(self.pendientes):
                print(f"   {i+1}. #{pedido['numero']} - {pedido['cliente']} ({len(pedido['items'])} items)")

# Simulación del sistema
sistema = SistemaPedidos()

# Agregar varios pedidos
sistema.agregar_pedido("Ana", ["Hamburguesa", "Papas fritas", "Refresco"])
sistema.agregar_pedido("Carlos", ["Pizza familiar", "Ensalada"])
sistema.agregar_pedido("María", ["Sushi", "Sopa miso"])
sistema.agregar_pedido("Juan", ["Tacos", "Agua de horchata"])

# Mostrar estado inicial
sistema.mostrar_estado()

# Procesar algunos pedidos
print("\\n🍳 Procesando pedidos...")
sistema.procesar_siguiente_pedido()
sistema.procesar_siguiente_pedido()

# Mostrar estado final
sistema.mostrar_estado()