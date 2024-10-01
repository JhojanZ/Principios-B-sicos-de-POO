from ui.ui import mostrar_menu, crear_cuenta, depositar_dinero, retirar_dinero, mostrar_cuenta, mostrar_todas_las_cuentas

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        print("")

        if opcion == 1:
            crear_cuenta()
        elif opcion == 2:
            depositar_dinero()
        elif opcion == 3:
            retirar_dinero()
        elif opcion == 4:
            mostrar_cuenta()
        elif opcion == 5:
            mostrar_todas_las_cuentas()
        elif opcion == 6:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
