def validate_number(numero, num_max, num_min):
    if numero>num_max or numero<num_min :
        retorno= False
    else:
        retorno= True
    return retorno

def validate_legnt(longitud:int,texto:str):
    if len(texto)==longitud:
        retorno= True
    else:
        retorno= False
    return retorno
def validate(valido_float,numero):
    retorno=""
    if  valido_float >=0 : 
        
        comprueno= numero.replace(".","")
        valido_str= comprueno.isdigit()
        if valido_str:
            retorno = True
    else:
        retorno= False
    return retorno
# pido_numero="45.6"

# valido_float= pido_numero.count(".")  
# print (valido_float)
# sd=(validate(valido_float,pido_numero))
# print(sd)
    
