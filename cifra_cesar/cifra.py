# -*- coding: utf-8 -*-


range_abc = range(ord("a"), ord("z") + 1)


def check_not_input(func):
    
    def func_wrapper(char_array, key=3, mode="ENCRYPT"):
        
        if not char_array:
            return "n/a"
        
        return func(char_array, key, mode)
    
    return func_wrapper 


def func_nova_letra(char, key, mode="ENCRYPT"):
    
    if mode == "ENCRYPT":
    
        return chr((ord(char) + key) % max(range_abc))
    
    elif mode == "DECRYPT":
    
        return chr((ord(char) - key) % max(range_abc))


@check_not_input 
def cifrar(char_array, key, mode):
    
    frase_encriptada = ''
    
    for char in char_array:
        
        if ord(char) in range_abc:
            frase_encriptada += func_nova_letra(char, key, mode) 
        else:
            frase_encriptada += char    

    return frase_encriptada.lower()
