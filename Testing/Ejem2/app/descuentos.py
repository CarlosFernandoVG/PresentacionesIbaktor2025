# app/descuentos.py

def calcular_descuento(cliente):
    if cliente["tipo"] == "premium":
        return cliente["total"] * 0.8
    elif cliente["tipo"] == "regular":
        return cliente["total"] * 0.9
    else:
        return cliente["total"]
