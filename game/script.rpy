screen mapscreen:
    add "maps/completo.png"
    #imagebutton idle "maps/colegio.png" hover "maps/colegio_resaltado.png" focus_mask True
    imagebutton:
        idle "maps/normal/piscina.png"
        hover "maps/resaltado/piscina_resaltado.png"
        focus_mask True
        action Jump("flashback_1")
    imagebutton:
        auto "maps/colegio_%s.png"
        focus_mask True
        action NullAction()
    imagebutton:
        idle "maps/normal/gimnasio.png"
        hover "maps/resaltado/gimnasio_resaltado.png"
        focus_mask True
        action NullAction()
    imagebutton:
        idle "maps/normal/jardin.png"
        hover "maps/resaltado/jardin_resaltado.png"
        focus_mask True
        action NullAction()
    imagebutton:
        idle "maps/normal/comedor.png"
        hover "maps/resaltado/comedor_resaltado.png"
        focus_mask True
        action NullAction()


# El juego comienza aquí.

label start:
    #$ nombre = renpy.input("¿Cual es tu nombre papi?")
    #$ nombre = nombre.strip()

    call screen mapscreen
    #jump flashback_1
    
    return
