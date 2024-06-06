from input import*
def sangre():
    pido_puesto= input( "ingrese su sangre:").upper()

    if pido_puesto =="A+" or pido_puesto==" B+" or pido_puesto=="AB+" or pido_puesto== "O+" or pido_puesto=="A-" or pido_puesto=="B-" or pido_puesto=="AB+":
        retorno = pido_puesto
    else:
        pido_puesto =input("error ingrese nuevamnte el puesto")
        retorno = pido_puesto
    return retorno
def dar_de_alta(id:int):
    id= id
    nombre = get_string("ingrese su nombre:","error ingrese nuevamente el nombre",5)
    apellidos =get_string("ingrese su apellido:","error ingrese nuevamente el apellido",5)
    edad= get_int("ingrese su edad","error, ingrese nuevamnete",120,1,5)
    altura= get_int("ingrese su altura","error, ingrese nuevamnete",300,10,5)
    dni= get_int("ingrese, su dni","error ingrese nuevamnete",99999999,40000000,5)
    grupo_sanguineo=sangre()
    dicc_paciente ={
                    "nombre":nombre,
                    "apellido":apellidos,
                    "edad":edad,
                    "altura":altura,
                    "dni":dni,
                    "grupo sannguineo":grupo_sanguineo,
                    "id":id}
    return dicc_paciente
def modificar(lista_pacientes):



    pido_id= get_int("ingrese su id:","error, ingrese nuevamente el id ",20,1,5)
    #   busco=busqueda(lista_pacientes,)
    for empleado in lista_pacientes:
            if empleado["Id"]== str(pido_id):
                print("empleado encontrado")
                dato_a_cambiar=input("¿que datos desea modificar? solo puede modifacr estos datos\n.nombre\n.Apellido\n.dni\n.altura\n.peso\n").capitalize()
                if dato_a_cambiar =="nombre":

                        nueva_dato_modificado= get_string("ingrese su nombre","hubo un error ingrese nuevamente el nombre. no debe superar los 20 caracteres",5).capitalize()
                        empleado[dato_a_cambiar] = nueva_dato_modificado

                elif dato_a_cambiar=="apellido":

                            nueva_dato_modificado=  get_string("ingrese su nombre:","hubo un error ingrese nuevamente el nombre. no debe superar los 20 caracteres",5).capitalize()
                            empleado[dato_a_cambiar] = nueva_dato_modificado
                elif dato_a_cambiar == "dni":
                        nueva_dato_modificado=  get_int("ingrese el valor nuevo de dni :","error ingrese nuveamente el dni:",500000000,10000000,5)
                        empleado[dato_a_cambiar] = nueva_dato_modificado
                elif dato_a_cambiar =="altura":
                        nueva_dato_modificado==65
                        empleado[dato_a_cambiar] = nueva_dato_modificado
                elif dato_a_cambiar == "peso":
                        nueva_dato_modificado= get_int("ingrese el peso que desea  modificar:","error, ingrese nuevamanete el peso:",234315,0,5)
                        empleado[dato_a_cambiar]=nueva_dato_modificado
                elif dato_a_cambiar=="grupo sanguineo":
                    nueva_dato_modificado= sangre()
                    empleado[dato_a_cambiar]=nueva_dato_modificado

                else:
                    print("error")
    return lista_pacientes
def eliminar_empleado(lista_empleados:list[dict],pido_dni:int):
    eliminado=""
    for i in lista_empleados:
        if i["dni"]== pido_dni:
            eliminado= i
            print(f"datos del empleado a eliminar:{eliminado}")
            lista_empleados.remove(eliminado)
    return lista_empleados
def mostrar_todos(lista_empleados):
    # Encabezado de la tabla
    encabezado = ["nombre", "apellido", "edad", "altura","peso","dni","grupo sanguineo"]
    print("-------------------------------------------------------")
    print("| {:<10} | {:<10} | {:<15} | {:<5} |{:<7}| {:<10}|{:<15} ".format(*encabezado))
    print("-------------------------------------------------------")

    # Imprimir datos de cada empleado
    for empleado in lista_empleados:
        print("| {:<10} | {:<10} | {:<5} | {:<7}cm | {:4kg} | {:<10} | {:<15} |".format(empleado["Nombre"], empleado["Apellido"], empleado["edad"], empleado["altura"],empleado["peso"], empleado["dni"],empleado["grupo sanguineo"]))

    # Separador final
    print("-------------------------------------------------------")
def ordenar_lista(lista:list[dict], valor:str, ascendente:bool):
   n = len(lista)
   for i in range(n):
    for j in range(0, n-i-1):
            if ascendente :
               if lista[j][valor] > lista[j+1][valor]:
                  lista[j], lista[j+1] = lista[j+1], lista[j]
            else:
               if lista[j][valor] < lista[j+1][valor]:
                  lista[j], lista[j+1] = lista[j+1], lista[j]
   return lista

def ordenar_lista_dato(lista_empleados:list[dict], forma:str, dato_ordenar:str):
   if forma == "ascendente":
      lista_ordenada = ordenar_lista(lista_empleados, dato_ordenar, True)
   elif forma == "descendente":
      lista_ordenada = ordenar_lista(lista_empleados, dato_ordenar, False)
      
   return lista_ordenada

def buscar_paciente_dni(lista:list,dni:int):
    for dato in lista:
            if dato["Dni"]== dni:
                empleado =print (dato["nombre"],dato["apellido"])
    return empleado
# def calcular_promedio(lista:list,dato_a_promediar:str):
def calcular_salario_promedio(lista_empleados:list[dict]):
   print("datos que se podra modificar\nedad\naltura\npeso")
   dato_a_promediar=input("ingrese el dato que desea modificar:").lower()
   acumulador_salarios = 0
   contador = 0
   for i in lista_empleados:
            acumulador_salarios+= i[{dato_a_promediar}]
            contador+=1
   promedio = acumulador_salarios/ contador
   return promedio
