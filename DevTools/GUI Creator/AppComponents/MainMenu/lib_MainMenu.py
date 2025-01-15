import os
from PyQt5.QtWidgets import  QMenuBar, QMenu,  QAction
from PyQt5.QtCore import Qt
from AppComponents.PreferencesWindow.lib_PreferencesWindow import PreferencesWindow
from AppComponents.OpenFileDialog.lib_OpenFileDialog       import OpenFileDialog
from AppComponents.SaveFileDialog.lib_SaveFileDialog       import SaveFileDialog

class MainMenuBar(QMenuBar):
    def __init__(self):
        super().__init__()
        self.__createMenus()

    def __createMenus(self):
        #- Menu "File"
        #----------------------------------------------------------------------
        my_Menu_file            = self.addMenu("File")
        #---- Menu Item "Open"
        my_MenuItem_open        = QAction("Open", self)
        my_MenuItem_open.triggered.connect(self.__showOpenFile)
        my_Menu_file.addAction(my_MenuItem_open)
        #---- Menu Item "Export"
        my_MenuItem_export      = QAction("Export", self)
        my_MenuItem_export.triggered.connect(self.__showSaveFile)        
        my_Menu_file.addAction(my_MenuItem_export)

        #- Menu "Settings"
        #----------------------------------------------------------------------
        my_Menu_settings        = self.addMenu("Settings")
        #---- Menu Item "Preferences"
        my_MenuItem_preferences = QAction("Preferences", self)
        my_MenuItem_preferences.triggered.connect(self.__showPreferencesWindow)
        my_Menu_settings.addAction(my_MenuItem_preferences)
        #---- Menu Item "Plugins" 
        my_MenuItem_plugins     = QAction("Plugins", self)
        my_MenuItem_plugins.triggered.connect(self.__showPreferencesWindow)
        my_Menu_settings.addAction(my_MenuItem_plugins)
        
        #- Menu "?"
        #----------------------------------------------------------------------
        my_Menu_help            = self.addMenu("?")
        #---- Menu Item "Help"
        my_MenuItem_help        = QAction("Help", self)
        my_MenuItem_help.triggered.connect(self.__showHelp)
        my_Menu_help.addAction(my_MenuItem_help)        
        #---- Menu Item "About"
        my_MenuItem_about       = QAction("About", self)
        my_MenuItem_about.triggered.connect(self.__showAbout)
        my_Menu_help.addAction(my_MenuItem_about)
        #---- Menu Item "Update"
        my_MenuItem_update      = QAction("Update", self)
        my_MenuItem_update.triggered.connect(self.__showUpdate)        
        my_Menu_help.addAction(my_MenuItem_update)

    def __showPreferencesWindow(self):
        preferences_window = PreferencesWindow(self)
        preferences_window.show()

    def __showOpenFile(self):
        print("Show Open File Dialog")
        my_dialog = OpenFileDialog(self)
        my_dialog.show()     
        pass

    def __showSaveFile(self):
        print("Show Save File Dialog")
        my_dialog = SaveFileDialog(self)
        my_dialog.show()        
        pass

    def __showHelp(self):
        print("Help Dialog")
        my_dialog = SaveFileDialog(self)
        my_dialog.show()        
        pass

    def __showAbout(self):
        print("About Dialog")
        my_dialog = SaveFileDialog(self)
        my_dialog.show()        
        pass

    def __showUpdate(self):
        print("Update Dialog")
        my_dialog = SaveFileDialog(self)
        my_dialog.show()        
        pass