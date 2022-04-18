# -*- coding: utf-8 -*-

from cifra_cesar import __version__ 
from cifra_cesar.cifra import cifrar
from cifra_cesar.cifra import range_abc

def test_version():
    assert __version__ == '0.1.0'

def test_range_abc():
    assert range_abc == range(97, 123)

def test_cifra_de_cesar():
    f_normal = 'a ligeira raposa marrom saltou sobre o cachorro cansado.'
    f_encriptada = 'd oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr.'

    assert cifrar(f_normal, 3, "ENCRYPT") == f_encriptada
    assert cifrar(f_encriptada, 3, "DECRYPT") == f_normal

def test_lower_case():
    f_normal = 'The quick brown fox jumps over the lazy dog.'
    assert cifrar(f_normal, 3).islower() == True

def test_input_none():
    f_normal = ''
    assert cifrar(f_normal) == 'n/a'

