from CheckBisiesto import esBisiesto

def test_esBisiesto_Y():
    decision = esBisiesto(2024)
    assert decision == "Es Bisiesto"
    
def test_esBisiesto_F():
    decision = esBisiesto(2025)
    assert decision == "Es NO Bisiesto"