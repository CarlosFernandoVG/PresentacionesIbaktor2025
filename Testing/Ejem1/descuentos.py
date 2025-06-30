def calcular_descuento(cliente):
    if cliente["tipo"] == "premium":
        return cliente["total"] * 0.8  # 20% de descuento
    elif cliente["tipo"] == "regular":
        return cliente["total"] * 0.9  # 10% de descuento
    else:
        return cliente["total"]