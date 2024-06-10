from .validate import*
def get_int(mensaje: str, mensaje_error: str, num_max: int, num_min: int, cantidad_intentos: int,operacion):
    contador = 0 
    retorno = ""
    bandera = True
    validacion=""
    if operacion == True:
        pido_numero = int(input(mensaje))
        validacion = validate_number(pido_numero,num_max,num_min)
        if validacion == False:
            retorno = str(pido_numero).zfill(8)   
        else:
            retorno= pido_numero      
    elif operacion== False:
        pido_numero = (input(mensaje))
        valido_str= pido_numero.isdigit()
        while bandera:
           
            if valido_str==True:
                pido_numero=int(pido_numero)
                validacion = validate_number(pido_numero, num_max, num_min)
                if validacion==False:
                    contador += 1

                    pido_numero=int(input(mensaje_error))
                    validacion = validate_number(pido_numero, num_max, num_min)
                else:
                    print("Número validado")
                    retorno =int( pido_numero)
                    bandera = False

            else:
                pido_numero = (input(mensaje_error))
                valido_str= pido_numero.isdigit()
                contador+=1
            if contador == cantidad_intentos:
                retorno = None
                print("Error")
                bandera = False
    return retorno

def get_string(mensaje:str, error_mensaje:str ,reintentos:int)-> str| None:
    retorno =""
    #pido_string=input(mensaje)
    #valido_caracteres=pido_string.isalpha()
    contador=0
  #  valido_string=validate_legnt(longitud,pido_string)
    pido_string=input(mensaje)
    valido_caracteres=pido_string.isalpha()
    while True:
    
      
       if     valido_caracteres== False or len(pido_string) > 20   :
        pido_string=input(error_mensaje)
        valido_caracteres=pido_string.isalpha()

        contador+=1

       else:
          retorno = pido_string
          print("guardado")
          break
       if contador== reintentos:
           retorno = None
           break
    return retorno
#prueba

# def get_float(mensaje: str, mensaje_error: str, num_max: int, num_min: int, cantidad_intentos: int):
#     contador = 0 
#     retorno = ""
#     bandera = True
#     pido_numero = float(input(mensaje))
#     while bandera:
      
#         validacion = validate_number(pido_numero, num_max, num_min)

#         if  validacion==False or type(pido_numero)==str:
#             contador += 1
#             pido_numero=float(input(mensaje_error))
#         else:
#             print("Número validado:")
#             retorno = pido_numero
#             bandera = False

#         if contador == cantidad_intentos:
#             retorno = None
#             print("Error")
#             bandera = False

#     return retorno
def get_float(mensaje: str, mensaje_error: str, num_max: int, num_min: int, cantidad_intentos: int):
    contador = 0 
    retorno = ""
    bandera = True
    pido_numero = (input(mensaje))
    valido_float= pido_numero.count(".")
    validacion=validate(valido_float,pido_numero)   

    while bandera:
        if validacion:
            pido_numero=float(pido_numero)
            validacion = validate_number(pido_numero, num_max, num_min)
            if validacion==False:
                contador += 1

                pido_numero=float(input(mensaje_error))
                validacion = validate_number(pido_numero, num_max, num_min)


            else:
                print("Número validado")
                retorno =float( pido_numero)
                bandera = False

        else:
            pido_numero = (input(mensaje_error))
            contador+=1
            valido_float= pido_numero.count(".")
            validacion=validate(valido_float,pido_numero)
            
        
        if contador == cantidad_intentos:
            retorno = None
            print("Error")
            bandera = False

    return retorno
# dni= get_int("ingrese, su dni","error ingrese nuevamnete",99999999,40000000,5,True)
# print(dni)