
class EventsHandler:
       
    __onMouseClick_delegate       = None  # Delegate (initially it is empty)
    __onMouseDoubleClick_delegate = None  # Delegate (initially it is empty)
    __onMouseHover_delegate       = None  # Delegate (initially it is empty)

    # Event
    def mousePressEvent(self, sender, event):
        """
        Manages the Mouse click event.

        Args:
            sender (QObject): L'oggetto che ha generato l'evento (es. un bottone o altro elemento).        
            event (QEvent): The Mouse Click event.
        """
        if self.__onMouseClick_delegate:
            self.__onMouseClick_delegate(sender, event)
        else:
            print(f"[EventHandlers]=> Mouse clicked at position: {event.pos()} on {sender.__class__.__name__}")
    # Set custom delegate for the event management
    def setOnMouseClick_delegate(self, delegate):
        """
        Imposta il delegato per l'evento di click del mouse.

        Args:
            delegate (callable): Il metodo che sarà chiamato durante l'evento.
        """
        self.__onMouseClick_delegate = delegate

    # Event
    def mouseDoubleClickEvent(self, sender, event):
        """
        Manages the Mouse Double Click event.

        Args:
            sender (QObject): L'oggetto che ha generato l'evento (es. un bottone o altro elemento).        
            event (QEvent): The Mouse Double Click event.
        """        
        if self.__onMouseDoubleClick_delegate:
            self.__onMouseDoubleClick_delegate(sender, event)
        else:
            print(f"[EventHandlers]=> Mouse Double clicked at position: {event.pos()} on {sender.__class__.__name__}")
    # Set custom delegate for the event management
    def setOnMouseDoubleClick_delegate(self, par_delegate):
        self.__onMouseDoubleClick_delegate = par_delegate

    # Event
    def enterEvent(self, sender, event):
        """
        Manages the Mouse Hover event.

        Args:
            sender (QObject): L'oggetto che ha generato l'evento (es. un bottone o altro elemento).        
            event (QEvent): The Mouse Hover event.
        """                
        if self.__onMouseHover_delegate:
            self.__onMouseHover_delegate(sender, event)
        else:
            print(f"[EventHandlers]=> Mouse Hover at position: {event.pos()} on {sender.__class__.__name__}")
    # Set custom delegate for the event management
    def setOnMouseHover_delegate(self, par_delegate):
        self.__onMouseHover_delegate = par_delegate