import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import re as RegEx
import os
from typing import Any, Dict
from Helpers.ConfigurationManagement.lib_ConfigurationManager import ConfigurationManager
from Helpers.ComponentManagement.lib_ComponentManager         import ComponentManager
from ObjectsLib.ConfigDictionary.lib_ConfigDictionary         import ConfigDictionary
from AppComponents.MainWindow.lib_MainWindow                  import MainWindow

class GUICreator(QMainWindow):
    # Impostazioni predefinite
    __default_settings = {
        "canvas_bg"     : "white",     #
        "window_width"  : 320,         #
        "window_height" : 800,         #
        "panel_bg"      : "lightgray", #
        "grid_size"     : 20           # Dimensione della griglia per snapping
    }
    __config_dir                = "DevTools\\GUI Creator\\Config\\"
    __config_file_path          = os.path.join(__config_dir, "settings.yaml")
    __ConfigurationManager      = ConfigurationManager()
    __ComponentManager          = ComponentManager()
    __settings:ConfigDictionary = None
                                 
    def __init__(self, root):
        super().__init__()
        # Carica le impostazioni
        self.__settings = self.__ConfigurationManager.loadYaml(self.__config_file_path)

        # Applica le impostazioni
        self.__applySettings()

        # Layout principale
        self.create_layout()

        # Binding del click sulla canvas per selezionare un'area dove posizionare il componente
        self.design_canvas.bind("<Button-1>", self.create_component_at_position)

        # Variabile per memorizzare i widget aggiunti
        self.widgets = []
        self.selected_widget = None
        self.drag_data = {"widget": None, "x": 0, "y": 0}

        # Menu principale
        self.create_menu()

    def applySettings(self, par_ComponentManager:ComponentManager) -> None:
        """
        Applica le impostazioni calcolando le formule e aggiornando i componenti.
        component_manager: Oggetto che gestisce i componenti dell'interfaccia.
        """
        def resolveReference(reference: str) -> Any:
            """
            Risolve un riferimento tipo <nome_componente>.<nome_proprietà>.
            """
            keys = reference.lower().split('.')
            current = self.settings
            for key in keys:
                if key in current:
                    current = current[key]
                else:
                    raise KeyError(f"Riferimento non trovato: {reference}")
            return current['value']

        def evaluateFormula(formula: str) -> Any:
            """
            Valuta una formula risolvendo i riferimenti e calcolando l'espressione.
            """
            def replacer(match: RegEx.Match) -> str:
                reference = match.group(1)
                try:
                    return str(resolveReference(reference))
                except KeyError as e:
                    raise ValueError(f"Errore nel riferimento della formula: {e}")

            # Trova tutti i riferimenti nella formula
            pattern = r'\{([a-z0-9_.]+)\}'  # Cattura nomi del tipo {componente.proprietà}
            resolved_formula = RegEx.sub(pattern, replacer, formula)

            # Valuta l'espressione matematica
            try:
                return eval(resolved_formula, {"__builtins__": None}, {})
            except Exception as e:
                raise ValueError(f"Errore nel calcolo della formula '{formula}': {e}")

        def resolveValues(data: Dict[str, Any]) -> None:
            for key, item in data.items():
                if isinstance(item, dict):
                    if 'formula' in item and item['formula']:
                        formula = item['formula']
                        item['value'] = evaluateFormula(formula)
                    elif isinstance(item, dict):
                        resolveValues(item)

        resolveValues(self.settings)
        self.__ComponentManager.updateComponents(self.settings)
        
    """
    def create_layout(self):
        Crea il layout principale dell'app
        # Pannello laterale sinistro per strumenti
        self.toolbox = ToolBox(self.root)

        # Canvas principale per il design
        self.design_canvas = tk.Canvas(self.root, bg=self.__settings["canvas_bg"])
        self.design_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Pannello destro per le proprietà
        self.properties_panel = tk.Frame(self.root, width=200, bg=self.__settings["panel_bg"])
        self.properties_panel.pack(side=tk.RIGHT, fill=tk.Y)
    """
        
    """
    def create_menu(self):
        Crea il menu principale dell'applicazione
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Menu File
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Esporta codice", command=self.export_code)
        file_menu.add_separator()
        file_menu.add_command(label="Esci", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Menu Preferenze
        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label="Preferenze", command=self.open_preferences)
        menubar.add_cascade(label="Preferenze", menu=settings_menu)
    """

    """    
    def create_component_at_position(self, event):
        Gestisce l'evento di click sulla canvas e crea il componente selezionato
        if self.toolbox.selectedComponent is None:
            print("Seleziona un componente dalla toolbox prima di cliccare sulla canvas.")
            return

        # Ottieni la posizione del click (event.x, event.y)
        x, y = event.x, event.y
        
        # Chiedi alla ToolBox di creare un nuovo componente
        new_component = self.toolbox.getNewComponent(x, y, width=100, height=50)
        
        # Il nuovo componente viene automaticamente aggiunto alla canvas
        new_component.place(x=x, y=y)
        new_component.bind("<ButtonPress-1>", self.on_component_click)
        new_component.bind("<B1-Motion>", self.on_drag_motion)
        new_component.bind("<ButtonRelease-1>", self.on_drag_release)
    """
        
    """
    def add_toolbox_items(self):
        
        tk.Label(self.toolbox, text="Strumenti", bg=self.__settings["panel_bg"], font=("Arial", 12, "bold")).pack(pady=10)

        tools = [
            ("Etichetta",        self.add_label),
            ("Pulsante",         self.add_button),
            ("Casella di testo", self.add_entry),
            ("Checkbox",         self.add_checkbox),
            ("RadioButton",      self.add_radiobutton),
        ]

        for name, command in tools:
            btn = tk.Button(self.toolbox, text=name, command=command, width=20)
            btn.pack(pady=5)
    """
            
    def add_label(self):
        """Aggiunge un'etichetta al canvas"""
        label = tk.Label(self.design_canvas, text="Etichetta", bg="yellow")
        self.add_widget(label, "Label")

    def add_button(self):
        """Aggiunge un pulsante al canvas"""
        button = tk.Button(self.design_canvas, text="Pulsante")
        self.add_widget(button, "Button")

    def add_entry(self):
        """Aggiunge una casella di testo al canvas"""
        entry = tk.Entry(self.design_canvas)
        self.add_widget(entry, "Entry")

    def add_checkbox(self):
        """Aggiunge una checkbox al canvas"""
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(self.design_canvas, text="Checkbox", variable=var)
        self.add_widget(checkbox, "Checkbutton")

    def add_radiobutton(self):
        """Aggiunge un radiobutton al canvas"""
        var = tk.StringVar()
        radiobutton = tk.Radiobutton(self.design_canvas, text="RadioButton", variable=var, value="1")
        self.add_widget(radiobutton, "Radiobutton")

    def add_widget(self, widget, widget_type):
        """Aggiunge un widget al canvas con funzionalità di trascinamento"""
        widget_id = self.design_canvas.create_window(100, 100, window=widget, anchor=tk.CENTER)

        self.widgets.append((widget_id, widget, widget_type))

        # Abilita il trascinamento
        self.enable_dragging(widget, widget_id)

    def enable_dragging(self, widget, widget_id):
        """Abilita il trascinamento di un widget nel canvas"""

        def start_drag(event):
            """Avvia il trascinamento memorizzando la posizione iniziale"""
            self.drag_data["widget_id"] = widget_id
            self.drag_data["start_x"] = event.x
            self.drag_data["start_y"] = event.y

        def drag(event):
            """Aggiorna la posizione del widget sul canvas"""
            dx = event.x - self.drag_data["start_x"]
            dy = event.y - self.drag_data["start_y"]
            self.design_canvas.move(self.drag_data["widget_id"], dx, dy)

        def end_drag(event):
            """Termina il trascinamento azzerando i dati temporanei"""
            self.drag_data.clear()

        widget.bind("<Button-1>", start_drag)
        widget.bind("<B1-Motion>", drag)
        widget.bind("<ButtonRelease-1>", end_drag)

    def start_drag(self, event, widget_id):
        """Inizia il drag-and-drop del widget"""
        self.drag_data["widget"] = widget_id
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def do_drag(self, event, widget_id):
        """Gestisce il drag-and-drop del widget"""
        if self.drag_data["widget"] == widget_id:
            canvas = self.design_canvas
            dx = event.x - self.drag_data["x"]
            dy = event.y - self.drag_data["y"]

            # Ottieni posizione attuale del widget
            x, y = canvas.coords(widget_id)

            # Calcola la nuova posizione e applica snapping alla griglia
            grid_size = self.settings["grid_size"]
            new_x = x + dx
            new_y = y + dy
            snapped_x = round(new_x / grid_size) * grid_size
            snapped_y = round(new_y / grid_size) * grid_size

            # Aggiorna la posizione del widget nel canvas
            canvas.coords(widget_id, snapped_x, snapped_y)

    def stop_drag(self, event, widget_id):
        """Termina il drag-and-drop del widget"""
        self.drag_data["widget"] = None

    def select_widget(self, widget):
        """Seleziona un widget e visualizza le sue proprietà"""
        self.selected_widget = widget
        self.show_properties(widget)

    def show_properties(self, widget):
        """Visualizza le proprietà del widget selezionato"""
        for child in self.properties_panel.winfo_children():
            child.destroy()

        tk.Label(self.properties_panel, text="Proprietà", bg=self.settings["panel_bg"], font=("Arial", 12, "bold")).pack(pady=10)

        # Proprietà modificabili
        if isinstance(widget, (tk.Label, tk.Button)):
            # Testo
            tk.Label(self.properties_panel, text="Testo").pack()
            text_var = tk.StringVar(value=widget["text"])
            text_entry = tk.Entry(self.properties_panel, textvariable=text_var)
            text_entry.pack()
            text_var.trace_add("write", lambda *args: widget.config(text=text_var.get()))

            # Colore di sfondo
            tk.Label(self.properties_panel, text="Colore sfondo").pack()
            bg_button = tk.Button(self.properties_panel, text="Scegli colore", command=lambda: self.pick_color(widget, "bg"))
            bg_button.pack()

            # Colore del testo
            tk.Label(self.properties_panel, text="Colore testo").pack()
            fg_button = tk.Button(self.properties_panel, text="Scegli colore", command=lambda: self.pick_color(widget, "fg"))
            fg_button.pack()

    def pick_color(self, widget, property_name):
        """Apre un color picker per selezionare un colore"""
        color_code = colorchooser.askcolor(title="Seleziona colore")[1]
        if color_code:
            widget.config({property_name: color_code})

    def export_code(self):
        """Esporta il layout come codice Python"""
        code_lines = [
            "import tkinter as tk\n\n",
            "def create_gui():\n",
            "    root = tk.Tk()\n",
            "    root.title('Generated GUI')\n",
            "    root.geometry('800x600')\n\n"
        ]

        for widget_id, widget, widget_type in self.widgets:
            widget_name = widget_type.lower() + str(widget_id)
            x, y = self.design_canvas.coords(widget_id)
            if widget_type == "Label":
                code_lines.append(f"    {widget_name} = tk.Label(root, text='{widget.cget('text')}', bg='{widget.cget('bg')}')\n")
            elif widget_type == "Button":
                code_lines.append(f"    {widget_name} = tk.Button(root, text='{widget.cget('text')}')\n")
            elif widget_type == "Entry":
                code_lines.append(f"    {widget_name} = tk.Entry(root)\n")
            elif widget_type == "Checkbutton":
                code_lines.append(f"    {widget_name} = tk.Checkbutton(root, text='{widget.cget('text')}')\n")
            elif widget_type == "Radiobutton":
                code_lines.append(f"    {widget_name} = tk.Radiobutton(root, text='{widget.cget('text')}')\n")
            code_lines.append(f"    {widget_name}.place(x={int(x)}, y={int(y)})\n\n")

        code_lines.append("    root.mainloop()\n\n")
        code_lines.append("if __name__ == '__main__':\n")
        code_lines.append("    create_gui()\n")

        # Salva il codice in un file
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python files", "*.py")])
        if file_path:
            with open(file_path, "w") as file:
                file.writelines(code_lines)
            messagebox.showinfo("Esportazione completata", f"Codice salvato in {file_path}")

    def __applySettings(self):
        """
        Applica le impostazioni calcolando le formule e aggiornando i componenti.
        component_manager: Oggetto che gestisce i componenti dell'interfaccia.
        """  
        self.setWindowTitle("[S2 Designs team] GUI Creator for python - Tkinter WYSIWYG")  

        mainWindow_top    = self.__settings.getProperty("main_window.top")
        mainWindow_left   = self.__settings.getProperty("main_window.left")
        mainWindow_height = self.__settings.getProperty("main_window.height")
        mainWindow_width  = self.__settings.getProperty("main_window.width")

        # Applica le impostazioni alla finestra principale
        self.setGeometry(mainWindow_top, mainWindow_left, mainWindow_width, mainWindow_height)
        """
        def resolve_reference(reference: str) -> Any:
            # Risolve un riferimento tipo <nome_componente>.<nome_proprietà>.
            keys = reference.lower().split('.')
            current = self.settings
            for key in keys:
                if key in current:
                    current = current[key]
                else:
                    raise KeyError(f"Riferimento non trovato: {reference}")
            return current['value']

        def evaluate_formula(formula: str) -> Any:
            try:
                # Semplice valutazione della formula (potenzialmente pericolosa con input non controllati)
                return eval(formula, {"__builtins__": None}, self.settings)
            except Exception as e:
                return f"Error: {e}"

        def resolve_values(data: Dict[str, Any]) -> None:
            for key, item in data.items():
                if isinstance(item, dict):
                    if 'formula' in item and item['formula']:
                        formula = item['formula']
                        item['value'] = evaluate_formula(formula)
                    elif isinstance(item, dict):
                        resolve_values(item)

        resolve_values(self.__settings)
        self.__ComponentManager.updateComponents(self.__settings)
        """
        

# Avvia l'app
if __name__ == "__main__":
    app    = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())