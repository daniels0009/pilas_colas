clase  Pila :
    "" " Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. ""
 
    def  __init__ ( self ):
        "" " Crea una pila vacía. " ""
        # La pila vacía se representa con una lista vacía
        auto .items = []

    def  apilar ( self , x ):
        "" " Agrega el elemento xa la pila. " ""
        # Apilar es agregar al final de la lista.
        auto .items.append (x)

    def  desapilar ( uno mismo ):
        "" Devuelve el elemento tope y lo elimina de la pila.
            Si la pila está vacía levanta una excepción. ""
        tratar :
            volver  auto .items.pop ()
        excepto  IndexError :
            elevar  ValueError ( " La pila está vacía " )

    def  es_vacia ( self ):
        "" " Devuelve True si la lista está vacía, False si no. " ""
        volver  auto .items == []

 Libros de clase:
    def   __init__ ( self , nombre , autor ):
        auto .n = nombre
         auto.a=autor


    def   getNombre ( self ):
        volver auto .n       
    def   getNombre ( self ):
        volver auto .a
        
