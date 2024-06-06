from parcial import*
def mostrar_menu():
  
    print("Seleccione una opción:")
    print("1. dar de alta")
    print("2. modificar")
    print("3. Eliminar")
    print("4. Mostrar todos")
    print("5. ordenar pacinetes")
    print("6. Buscar paciente por dni")
    print("7. calcular promedio")
    print("8. Salir")
def mi_programa():
    lista_pacientes=[]
    de_alta= False
    id=0
    while True:
        mostrar_menu()
        opcion = input("ingrese una opcion")
        if opcion =="1":
            print(lista_pacientes)

            id+=1
            pacientes=dar_de_alta(id)
            lista_pacientes.append(pacientes)
            de_alta= True
            
            pass
        elif opcion =="2" and de_alta:
            lista_pacientes= modificar(lista_pacientes)
            pass
        elif opcion==" 3" and de_alta:
            dni= get_int("ingrese, su dni","error ingrese nuevamnete",99999999,40000000,5)

            
            lista_eliminados = eliminar_empleado(lista_pacientes,dni)
            pass
        elif opcion=="4":
            mostrar_todos(lista_pacientes)
            pass
        elif opcion=="5":
            forma= input("ingrese de forma ascendente o decendente:")
            dato_ordenar=input("que dato desea ordenar de la lista?")

            ordenar_lista_dato(lista_pacientes,forma,dato_ordenar)
        elif opcion=="6":
            dni= get_int("ingrese, su dni","error ingrese nuevamnete",99999999,40000000,5)

            paciente=buscar_paciente_dni(lista_pacientes,dni)
            print(paciente)
        elif opcion=="7":
            promedio= calcular_salario_promedio(lista_pacientes)
            print(promedio)

            pass
        elif opcion =="8":
            break
mi_programa()