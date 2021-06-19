menu = ['1. Crear contrasena', '2. Ingresar coordenadas actuales', '3. Ubicar zona wifi mas cercana', '4. Guardar', '5. Actualizar registros de zonas wifi desde archivo', '6. Elegir opcion de menu favorita', '7. Cerrar sesion']

choise = input('Elija una opcion: ')

if choise == '6':
    print(input('Ingresa al sistema un numero del 1 al 5 como opcion favorita: '))
    menu_actualizado = len(menu-1)

print(menu)