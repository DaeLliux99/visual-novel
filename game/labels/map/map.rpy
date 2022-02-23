screen mapscreen:
    add "maps/completo.png"
    #imagebutton idle "maps/colegio.png" hover "maps/colegio_resaltado.png" focus_mask True
    imagebutton:
        auto "maps/colegio_%s.png"
        action NullAction()



