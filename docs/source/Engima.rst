Engima module
=============
*******************
``M3 Enigma`` class
*******************
.. automodule:: ciphers.Engima
.. autoclass:: M3
    :exclude-members: rotor_choices,reflector
    :members:
    :undoc-members:
    :show-inheritance:
*********
Rotor Dic
*********
sadasdasdasd::
    
    rotor_choices = {
        1: {
            'wiring': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
            'step': 'Q'
        },
        2: {
            'wiring': 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
            'step': 'E'
        },
        3: {
            'wiring': 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
            'step': 'V'
        },
        4: {
            'wiring': 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
            'step': 'J'
        },
        5: {
            'wiring': 'VZBRGITYUPSDNHLXAWMJQOFECK',
            'step': 'Z'
        },
    }  
**************    
Reflector Dict
**************
..code-block:: python
    These are the entries::
        {
            'reflector_b': 'YRUHQSLDPXNGOKMIEBFZCWVJAT',  # b reflector
            'reflector_c': 'FVPJIAOYEDRZXWGCTKUQSBNMHL'  # c reflector
        }
