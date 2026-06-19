# main.py - Sistema de Gestión de Pedidos "El Imperio"

# Datos simulados en memoria (Diccionario)
inventario = {
    "1": {"nombre": "Pirotines N°10", "precio": 800},
    "2": {"nombre": "Film de PVC", "precio": 1200}
}

def validar_numero(mensaje):
    """Función para el manejo de excepciones (Camino Infeliz)"""
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("ERROR: Ingrese un valor mayor a cero.")
                continue
            return valor
        except ValueError:
            print("ERROR: Ingrese una cantidad numérica válida.")

def verificar_presupuesto(costo_total):
    """Gateway de control administrativo"""
    LIMITE_PRESUPUESTO = 50000
    if costo_total > LIMITE_PRESUPUESTO:
        return "Pendiente_Aprobacion_Chelo"
    return "Enviado"

def main():
    print("--- ImperioBot: Sistema de Pedidos ---")
    estado = "INICIO"
    
    while True:
        if estado == "INICIO":
            comando = input("Escribí 'pedido' para comenzar o '/exit' para salir: ").lower()
            if comando == "pedido":
                estado = "SELECCION"
            elif comando == "/exit":
                break
                
        elif estado == "SELECCION":
            print("Categoría: Desechables")
            print("1. Pirotines N°10 ($800) | 2. Film de PVC ($1200)")
            opcion = input("Seleccioná el insumo (1 o 2): ")
            
            if opcion in inventario:
                insumo = inventario[opcion]
                cantidad = validar_numero("Ingresá la cantidad: ")
                
                costo = cantidad * insumo["precio"]
                resultado = verificar_presupuesto(costo)
                
                print(f"Pedido realizado. Estado: {resultado}. Costo: ${costo}")
                estado = "INICIO"
            else:
                print("Opción inválida.")
                estado = "INICIO"

if __name__ == "__main__":
    main()
