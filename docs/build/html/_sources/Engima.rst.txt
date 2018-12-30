Engima module
=============
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
.. exec::
    import json
    from ciphers.Engima import M3
    json_obj = json.dumps(M3.rotor_choices, sort_keys=True, indent=4)
    json_obj= json_obj[:-1]+""
    print('.. code-block:: JavaScript\n\n    %s\n\n' % json_obj)   

*********    
Reflector Dict
*********
.. exec::
    import json
    from ciphers.Engima import M3    
    reflector = json.dumps(M3.reflector, sort_keys=True, indent=4)
    reflector= reflector[:-1]+""
    print('.. code-block:: JavaScript\n\n    %s\n\n' % reflector)
