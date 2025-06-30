def esBisiesto(year: int):   
    print("Vamo a probar")
    if year % 400 == 0:
        print("Hola")
        return("Es Bisiesto")
    elif (year % 4 == 0) & (year % 100 != 0):
        var = (year % 4 == 0) & (year % 100 != 0)
        return("Es Bisiesto")
    else:
        return("Es NO Bisiesto")