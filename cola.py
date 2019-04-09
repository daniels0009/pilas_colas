clase  Cola :
    "" " Representa una cola con operaciones de encolar, desencolar y
        verificar si está vacía. ""

    def  __init__ ( self ):
        "" " Crea una cola vacía. " ""
        # La cola vacía se representa con una lista vacía
        auto .items = []

    def  encolar ( self , x ):
        "" " Agrega el elemento xa la cola. " ""
        # Encolar es agregar al final de la cola.
        auto .items.append (x)

    def  desencolar ( self ):
        "" Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola está vacía levanta una excepción. ""
        tratar :
            atendido =  auto .items [ 0 ]
            auto .items.pop ( 0 )
            volver atendido
        excepto  IndexError :
            impresión
            " La cola esta vacia "

    def  es_vacia ( self ):
        "" " Devuelve True si la lista está vacía, False si no. " ""
        volver  auto .items == []

    def  tamano ( uno mismo ):
        volver  len ( auto .items)
