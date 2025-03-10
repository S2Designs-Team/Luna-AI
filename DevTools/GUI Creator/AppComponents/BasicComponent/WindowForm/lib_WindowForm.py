from PyQt5.QtCore    import Qt, QPoint, QRect
from PyQt5.QtGui     import QPen, QColor, QPainter
from PyQt5.QtWidgets import QWidget

from AppComponents.BasicComponent.WindowForm.lib_TitleBar  import TitleBar
from AppComponents.BasicComponent.Enums.lib_Enums          import EnumLayout
from AppComponents.BasicComponent.WindowForm.lib_UIElement import UIElement

class WindowForm(UIElement): 
    #- [CLASS CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------
    def __init__(self, par_parent=None):
        super().__init__(par_parent)
        self.objectName      = "WindowForm"
        self.layout_type     = EnumLayout.VERTICAL
        self.setPosition(0, 0)
        self.setSize(550, 400)
        # ----------------------------------       
        self.setWindowFlags(Qt.SubWindow)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.__is_resizing     = False
        self.__resize_position = None   
        self.css_style = f"""
            background-color: #FFFFFF;
            border:           2px solid black;
            border-radius:    10px;
        """
        self.titlebar_ctrl = self.__createTitleBarCtrl()
        self.titlebar_ctrl.setVisible(True)
        self.titlebar_ctrl.show()
        self.titlebar_ctrl.update()
        self.addChild(self.titlebar_ctrl)  

        self.workarea_ctrl = self.__createWorkAreaCtrl()
        self.workarea_ctrl.setVisible(True)
        self.workarea_ctrl.show()
        self.workarea_ctrl.update()
        self.addChild(self.workarea_ctrl)
       
        self.workarea_ctrl.layout.addStretch()
        self.layout.addStretch()

        self.layout.update()
        self.update()

        #self.__setEventsCallbacks()  
        # Log di debug
        print(f"Design WindowForm's TitleBar stylesheet:\n{self.titlebar_ctrl.styleSheet()}")  
        print(f"Design WindowForm's WorkArea stylesheet:\n{self.workarea_ctrl.styleSheet()}")           
        print(f"WindowForm geometry: {self.geometry()}, size: {self.size()}")
        print(f"TitleBar geometry: {self.titlebar_ctrl.geometry()}, size: {self.titlebar_ctrl.size()}")
        print(f"TitleBar size: {self.titlebar_ctrl.size()}, minimum size: {self.titlebar_ctrl.minimumSize()}")        
        print(f"WorkArea geometry: {self.workarea_ctrl.geometry()}, size: {self.workarea_ctrl.size()}")
        print(f"WorkArea size: {self.workarea_ctrl.size()}, minimum size: {self.workarea_ctrl.minimumSize()}")        

        for child in self.findChildren(UIElement):
            print(f"Child: {child.objectName}, Visible: {child.isVisible()}, Parent: {child.parent.objectName}")

        self.titlebar_ctrl.repaint()
        self.workarea_ctrl.repaint()
        self.repaint()     

    #- [CLASS EVENTS]
    #--------------------------------------------------------------------------------------------
    def onWindowClick(self, sender, event):
        print("trallallero trallallà")
        #Handles the click on the WindowForm surface.
        """
        component = self.toolbox.getSelectedComponent()
        if component:
            self.createComponent(component, event.pos().x(), event.pos().y())
            self.toolbox.clearSelectedComponent()
            self.properties_panel.updateProperties(component)
        """
        pass
        
    #- [CLASS PRIVATE METHODS]
    #--------------------------------------------------------------------------------------------
    def __createTitleBarCtrl(self):
        my_new_ctrl            = TitleBar(self)
        my_new_ctrl.objectName = "TitleBar"    
        my_new_ctrl.title      = "TitleBar"
        my_new_ctrl.css_style  = f"""
            background-color: yellow;
            border: 1px solid red;
        """
        #my_new_ctrl.css_style  = f"""
        #    background-color:           #2E2E2E; 
        #    border:                     1px solid black;      
        #    border-top-left-radius:     0px; 
        #    border-top-right-radius:    0px;
        #    border-bottom-left-radius:  0px; 
        #    border-bottom-right-radius: 0px;
        #"""
        print("Design WindowForm's TitleBar created.")
        my_new_ctrl.update()
        return my_new_ctrl

    def __createWorkAreaCtrl(self):
        my_new_ctrl             = WorkArea(self)
        my_new_ctrl.objectName  = "WorkArea"
        my_new_ctrl.setPosition(40, 0)
        my_new_ctrl.setSize(550, 360)
        my_new_ctrl.css_style  = f"""
            background-color: blue;
            border: 1px solid red;
        """
        #my_new_ctrl.css_style   = f"""
        #    background-color:           white;
        #    border:                     1px solid black;
        #    border-top-left-radius:     0px; 
        #    border-top-right-radius:    0px;
        #    border-bottom-left-radius:  10px; 
        #    border-bottom-right-radius: 10px;
        #"""   
        # self.work_area.mousePressEvent = self.onComponentWindowClick           
        print("Design WindowForm's WorkArea created.")
        my_new_ctrl.update()
        return my_new_ctrl
        
    def __setEventsCallbacks(self):
        self.eventsHandler.setOnMouseClick_delegate(self.onWindowClick)


class WorkArea(UIElement):
    def __init__(self, par_parent=None):
        super().__init__(par_parent)
        self.layout_type     = EnumLayout.VERTICAL
        self.setPosition(0, 0)
        self.setSize(200, 100)
        self._designer_focused_component = None

    def setFocusedComponent(self, component):
        self._designer_focused_component = component
        self.update()  # Forza il ridisegno per richiamare paintEvent

    def paintEvent(self, event):
        """Disegna il bordo e i quadratini di ridimensionamento per il componente selezionato"""

        super().paintEvent(event)

        if self._designer_focused_component:
            painter = QPainter(self)
            if not painter.isActive():
                return
            pen = QPen(QColor(0, 0, 255), 2, Qt.SolidLine)
            painter.setPen(pen)
            rect = self._designer_focused_component.geometry()
            painter.drawRect(rect)

            # Disegna i quadratini di ridimensionamento
            handle_size = 6
            handles = [
                QPoint(rect.left(), rect.top()),
                QPoint(rect.right(), rect.top()),
                QPoint(rect.left(), rect.bottom()),
                QPoint(rect.right(), rect.bottom())
            ]
            for handle in handles:
                painter.fillRect(QRect(handle.x() - handle_size // 2, handle.y() - handle_size // 2, handle_size, handle_size), QColor(255, 0, 0))