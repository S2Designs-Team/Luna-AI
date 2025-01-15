from PyQt5.QtWidgets import (QListView, QCalendarWidget,                             
      QToolBox, QLabel, QVBoxLayout, QHBoxLayout, QWidget, 
      QListWidget, QGridLayout, QToolButton, QRadioButton, 
      QCheckBox, QComboBox, QFrame, QDateEdit, QTimeEdit, 
      QTextEdit)
from PyQt5.QtCore    import Qt, QMimeData
from PyQt5.QtGui     import QDrag
from AppComponents.BasicComponent.lib_BasicGuiComponent     import BasicGuiComponent
from AppComponents.BasicComponent.IconButton.lib_IconButton import IconButton
from AppComponents.BasicComponent.Layout.lib_QFlowLayout    import FlowLayout
from AppComponents.BasicComponent.Enums.lib_Enums           import EnumLayout

class ToolBox(QToolBox):
    __selected_component:str   = None
    __layout_type:EnumLayout  = EnumLayout.VERTICAL
    __container               = None

    # Mappa dei componenti
    __component_map = {
        "Toggle button":  QLabel,
        "Radio button":   QRadioButton, 
        "Check box":      QCheckBox, 
        "Icon button":    IconButton,
        "Split button":   QLabel,
        "GroupBox":       QLabel,
        "Frame":          QFrame,
        "Splitter":       QLabel,
        "Dropdown menu":  QLabel,
        "Combo box":      QComboBox,
        "Spinner":        QLabel,
        "List Box":       QListView,
        "Calendar":       QCalendarWidget,
        "Date Picker":    QDateEdit,
        "Time picker":    QTimeEdit,
        "Color picker":   QLabel,
        "File picker":    QLabel,
        "Input Box":      QLabel,
        "Text Box":       QTextEdit,
        "Text Area":      QTextEdit,
        "Label":          QLabel,
        "Rich Text Box":  QTextEdit,
        "Password field": QLabel, 
        "Search bar":     QLabel,
        "Image":          QLabel,
        "Picture":        QLabel,
        "Draw Panel":     QLabel
    }

    @property
    def selectedComponent(self):
        return self.__selected_component

    def __init__(self, parent=None):
        super().__init__()
        self.drag_data = {"x": 0, "y": 0, "start_x": 0, "start_y": 0, "widget": None} 
        
        # Layout per il pannello Toolbox
        self.__setLayoutType(self.__layout_type)
        self.__addToolBarTitle()

        # Lista dei componenti disponibili
        self.toolbox_list = QListWidget()
        self.__addCategory("All",        {"Toggle button", "Radio button", "Check box",    "Icon button", "Split button", 
                                          "GroupBox",      "Frame",        "Splitter",     "Calendar",
                                          "Dropdown menu", "Combo box",    "Spinner",      "List Box",    "Date Picker", "Time picker",    "Color picker", "File picker",
                                          "Input Box",     "Text Box",     "Text Area",    "Label",       "Rich Text Box", "Password field", "Search bar",
                                          "Image",         "Picture",      "Draw Panel", })
        self.__addCategory("Buttons",    {"Toggle button", "Radio button", "Check box", "Icon button", "Split button",})
        self.__addCategory("Containers", {"GroupBox",      "Frame",        "Splitter"})
        self.__addCategory("Selectors",  {"Dropdown menu", "Combo box",    "Spinner",   "List Box",    "Calendar",      "Date Picker",  "Time picker",  "Color picker", "File picker"})
        self.__addCategory("Text",       {"Input Box",     "Text Box",     "Text Area", "Label",       "Rich Text Box", "Password field", "Search bar"})
        self.__addCategory("Image",      {"Image",         "Picture",      "Draw Panel"})
        self.layout.addWidget(self.toolbox_list)

    def __setLayoutType(self, par_layout_type:EnumLayout):
        
        match par_layout_type:
            case EnumLayout.VERTICAL:
                self.layout = QVBoxLayout(self)
            case EnumLayout.HORIZONTAL:
                self.layout = QHBoxLayout(self)
            case EnumLayout.FLOW:
                self.layout = FlowLayout(self)
            case _:
                raise ValueError("Invalid layout type.")
        
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.layout)

        self.__layout_type = par_layout_type

    def __addToolBarTitle(self, par_Toolbar_title:str = "Default Title"):
        # Etichetta della Toolbox
        my_ToolBox_title = QLabel(par_Toolbar_title)
        self.layout.addWidget(my_ToolBox_title)

    def __addCategory(self, category, items):
        """Aggiunge una categoria con i suoi elementi."""
        my_Panel_container = QWidget()
        my_Layout_category_contents = FlowLayout()
        my_IconList_components = QGridLayout()
        my_IconList_components.setSpacing(10)

        # Aggiunge ogni elemento come un bottone con un'icona
        for item in items:
            my_current_PicButton = IconButton(par_res_picture_path=f"DevTools\\GUI Creator\\Resources\\{item}.png", par_button_text=item)
            print(f"DevTools\\GUI Creator\\Resources\\{item}.png")
            my_current_PicButton.setFixedSize(100, 100)
            my_current_PicButton.setToolTip(item)
            my_current_PicButton.mousePressEvent = lambda event, item=item: self.selectComponent(item)
            my_Layout_category_contents.addWidget(my_current_PicButton)
        my_Panel_container.setLayout(my_Layout_category_contents)
        self.addItem(my_Panel_container, category)

    def __addItem(self, category, items):
        container = QWidget()
        layout    = QVBoxLayout()
        for item in items:
            layout.addWidget(IconButton("DevTools\\GUI Creator\\Resources\\calendar.png", item))  # Qui puoi mettere bottoni interattivi o altre interfacce
        container.setLayout(layout)
        self.__addItem(container, category)

    def selectComponent(self, component_name):
        """Memorizza il tipo di componente selezionato"""
        self.__selected_component = component_name
        print(f"Selected component: {component_name}")
    
    def getSelectedComponent(self, x=0, y=0, width=100, height=30):
        """Restituisce un'istanza del componente selezionato"""
        if not self.selectedComponent:
            return None        
        component_class = self.__component_map.get(self.__selected_component)
        if component_class:
            return component_class()
        return None
    
    def clearSelectedComponent(self):
        """Svuota il nome del tipo di oggetto selezionato"""
        self.__selected_component = None    

    def on_component_click(self, event):
        """ Gestisce il click sul componente per iniziare il trascinamento """
        widget = event.widget
        self.drag_data['widget'] = widget
        self.drag_data['start_x'] = event.x
        self.drag_data['start_y'] = event.y

    def on_drag_motion(self, event):
        """ Sposta il componente durante il trascinamento """
        if self.drag_data['widget'] is None:
            return
        
        dx = event.x - self.drag_data['start_x']
        dy = event.y - self.drag_data['start_y']
        
        # Muovi il widget con place
        widget = self.drag_data['widget']
        widget.place(x=widget.winfo_x() + dx, y=widget.winfo_y() + dy)

        # Aggiorna la posizione iniziale per il prossimo movimento
        self.drag_data['start_x'] = event.x
        self.drag_data['start_y'] = event.y

    def on_drag_release(self, event):
        """ Termina il trascinamento quando il mouse viene rilasciato """
        self.drag_data['widget'] = None
    
    def on_iconbutton_startDrag(self, event):
        """Inizia il drag-and-drop del componente"""
        drag = QDrag(event.widget())
        mime_data = QMimeData()
        mime_data.setText(event.widget().toolTip())
        drag.setMimeData(mime_data)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.MoveAction)

    # Funzioni per creare ogni tipo di componente
    """
    def add_label(self, x, y, width, height):
        label = tk.Label(self.parent_frame, text="Etichetta", width=width, height=height, bg="lightgrey")
        label.place(x=x, y=y)
        label.bind("<Button-1>", self.on_drag_start)
        label.bind("<B1-Motion>", self.on_drag_motion)                   
        return label

    def add_button(self, x, y, width, height):
        button = tk.Button(self.parent_frame, text="Pulsante", command=lambda: print("Pulsante premuto"))
        button.place(x=x, y=y, width=width, height=height)
        button.bind("<Button-1>", self.on_drag_start)
        button.bind("<B1-Motion>", self.on_drag_motion)           
        return button

    def add_entry(self, x, y, width, height):
        entry = tk.Entry(self.parent_frame, width=width)
        entry.place(x=x, y=y, width=width, height=height)
        entry.bind("<Button-1>", self.on_drag_start)
        entry.bind("<B1-Motion>", self.on_drag_motion)   
        return entry

    def add_checkbox(self, x, y, width, height):
        checkbox = tk.Checkbutton(self.parent_frame, text="Checkbox")
        checkbox.place(x=x, y=y, width=width, height=height)
        checkbox.bind("<Button-1>", self.on_drag_start)
        checkbox.bind("<B1-Motion>", self.on_drag_motion)        
        return checkbox

    def add_radiobutton(self, x, y, width, height):
        radiobutton = tk.Radiobutton(self.parent_frame, text="RadioButton", value=1)
        radiobutton.place(x=x, y=y, width=width, height=height)
        radiobutton.bind("<Button-1>", self.on_drag_start)
        radiobutton.bind("<B1-Motion>", self.on_drag_motion)  
        return radiobutton

    def add_canvas(self, x, y, width, height):
        canvas = tk.Canvas(self.parent_frame, width=width, height=height, bg="lightblue")
        canvas.place(x=x, y=y)
        canvas.bind("<Button-1>", self.on_drag_start)
        canvas.bind("<B1-Motion>", self.on_drag_motion)           
        return canvas

    def add_listbox(self, x, y, width, height):
        listbox = tk.Listbox(self.parent_frame, width=width, height=height)
        listbox.place(x=x, y=y)
        listbox.bind("<Button-1>", self.on_drag_start)
        listbox.bind("<B1-Motion>", self.on_drag_motion)           
        return listbox

    def add_scrollbar(self, x, y, width, height):
        scrollbar = tk.Scrollbar(self.parent_frame)
        scrollbar.place(x=x + width, y=y, height=height)
        listbox = tk.Listbox(self.parent_frame, yscrollcommand=scrollbar.set)
        listbox.place(x=x, y=y, width=width, height=height)
        scrollbar.config(command=listbox.yview)
        listbox.bind("<Button-1>", self.on_drag_start)
        listbox.bind("<B1-Motion>", self.on_drag_motion)          
        return listbox

    def add_spinbox(self, x, y, width, height):
        spinbox = tk.Spinbox(self.parent_frame, from_=0, to=10, width=width)
        spinbox.place(x=x, y=y, width=width, height=height)
        spinbox.bind("<Button-1>", self.on_drag_start)
        spinbox.bind("<B1-Motion>", self.on_drag_motion)                 
        return spinbox

    def add_scale(self, x, y, width, height):
        scale = tk.Scale(self.parent_frame, from_=0, to=100, orient="horizontal", width=width)
        scale.place(x=x, y=y)
        scale.bind("<Button-1>", self.on_drag_start)
        scale.bind("<B1-Motion>", self.on_drag_motion)             
        return scale

    def add_optionmenu(self, x, y, width, height):
        options = ["Opzione 1", "Opzione 2", "Opzione 3"]
        optionmenu = tk.OptionMenu(self.parent_frame, tk.StringVar(value=options[0]), *options)
        optionmenu.place(x=x, y=y, width=width, height=height)
        optionmenu.bind("<Button-1>", self.on_drag_start)
        optionmenu.bind("<B1-Motion>", self.on_drag_motion)           
        return optionmenu

    def add_message(self, x, y, width, height):
        message = tk.Message(self.parent_frame, text="Messaggio di esempio", width=width)
        message.place(x=x, y=y)
        message.bind("<Button-1>", self.on_drag_start)
        message.bind("<B1-Motion>", self.on_drag_motion)           
        return message

    def add_text(self, x, y, width, height):
        text = tk.Text(self.parent_frame, height=5, width=40)
        text.place(x=x, y=y)
        text.bind("<Button-1>", self.on_drag_start)
        text.bind("<B1-Motion>", self.on_drag_motion)               
        return text

    def add_frame(self, x, y, width, height):
        frame = tk.Frame(self.parent_frame, bg="lightgrey", width=width, height=height)
        frame.place(x=x, y=y)
        frame.bind("<Button-1>", self.on_drag_start)
        frame.bind("<B1-Motion>", self.on_drag_motion)       
        return frame

        # Lista dei tipi di componenti disponibili
        self.tools = [
            ("Etichetta", self.add_label),
            ("Pulsante", self.add_button),
            ("Casella di testo", self.add_entry),
            ("Checkbox", self.add_checkbox),
            ("RadioButton", self.add_radiobutton),
            ("Canvas", self.add_canvas),
            ("Lista", self.add_listbox),
            ("Scorrimento", self.add_scrollbar),
            ("Spinbox", self.add_spinbox),
            ("Slider", self.add_scale),
            ("Opzioni", self.add_optionmenu),
            ("Messaggio", self.add_message),
            ("Text Area", self.add_text),
            ("Frame", self.add_frame),
        ]    
    """
