# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Emilia")
define a = Character("Agnes")

screen mapscreen:
    #imagemap:
    #    auto "colegio_%s.png"
    add "colegio.png"

# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    #show screen mapscreen
    scene bg room

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show emilia green smile

    # Presenta las líneas del diálogo.

    e "Ahora bajate los pantalones"

    e "Te voy a dejar mas seco que habitante de dragon ball en la saga de Cell"

    e "UwU"
    # Finaliza el juego:

    return
