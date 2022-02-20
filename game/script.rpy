

# El juego comienza aquí.

label start:
    $ nombre = renpy.input("¿Cual es tu nombre papi?")

    $ nombre = nombre.strip()

    jump flashback_1
    
    return
