import csv
import os

def cargar_inventario():
    inventario = {}
    # Esto construye el path correcto sin importar desde dónde se ejecute
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_csv = os.path.join(base_dir, 'inventario.csv')
    try:
        with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                inventario[fila['id']] = {
                    "nombre": fila['nombre'],
                    "precio": int(fila['precio'])
                }
    except FileNotFoundError:
        print("Error: No se encontró el archivo de inventario.")
    return inventario
# Cargamos el inventario al iniciar
inventario = cargar_inventario()

def validar_numero(mensaje):
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
    LIMITE_PRESUPUESTO = 50000
    if costo_total > LIMITE_PRESUPUESTO:
        return "Pendiente_Aprobacion_Chelo"
    return "Enviado"

def main():
    print("--- ImperioBot: Sistema de Pedidos ---")
    estado = "INICIO"

    while True:
        if estado == "INICIO":
            comando = input("Escriba 'pedido' para comenzar o 'salir' para cerrar: ").lower()
            if comando == "pedido":
                estado = "PROCESO"
            elif comando == "salir":
                break
        
        elif estado == "PROCESO":
            print(f"Inventario disponible: {inventario}")
            id_prod = input("Ingrese el ID del producto: ")
            
            if id_prod in inventario:
                cantidad = validar_numero("Ingrese cantidad: ")
                costo = inventario[id_prod]["precio"] * cantidad
                print(f"Total: ${costo}")
                resultado = verificar_presupuesto(costo)
                print(f"Estado del pedido: {resultado}")
                estado = "INICIO"
            else:
                print("Producto no encontrado.")

if __name__ == "__main__":
    main()
