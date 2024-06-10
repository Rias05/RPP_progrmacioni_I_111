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
    print("8. deternminar compatibilidad")
    print("9. Salir")

def mi_programa():
    lista_pacientes=[]

    de_alta= False
    id = actualizar_id(lista_pacientes)
    lista_pacientes = parser_csv_pacientes("pacientes.csv")
    while True:
        mostrar_menu()
        opcion = input("ingrese una opcion")
        if opcion =="1":
            id+=1
            lista_pacientes=dar_de_alta(id,lista_pacientes)
            de_alta= True
        elif opcion =="2" and de_alta:
            lista_pacientes= modificar(lista_pacientes)
        elif opcion==" 3" and de_alta:
            dni= get_int("ingrese, su dni","error ingrese nuevamente",99999999,40000000,5,False)
            lista_pacientes = eliminar_empleado(lista_pacientes,dni)  
        elif opcion=="4" and de_alta:
            mostrar_todos(lista_pacientes)
        elif opcion=="5" :
            forma= input("ingrese e forma ascendente o decendente:")
            dato_ordenar=input("que dato desea ordenar de la lista?")

            lista_pacientes=ordenar_lista_dato(lista_pacientes,forma,dato_ordenar)
            print(lista_pacientes)# xd
        elif opcion=="6" and de_alta:
            dni= get_int("ingrese, su dni","error ingrese nuevamnete",99999999,40000000,5,False)

            paciente=buscar_paciente_dni(lista_pacientes,dni)
            print(paciente)
        elif opcion=="7"  and de_alta:
            promedio= calcular_salario_promedio(lista_pacientes)
            print(promedio)

            pass
        elif opcion =="8":
            determinar_compatibilidad(lista_pacientes)

            

        elif opcion =="9":

            generar_csv_pacientes("pacientes.csv",lista_pacientes)
            break
mi_programa()