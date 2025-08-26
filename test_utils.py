from utils import Primastro

def test_es_primo():
    Primastro(2) is True
    Primastro(6) is False
    Primastro(7) is True
    Primastro(100) is False