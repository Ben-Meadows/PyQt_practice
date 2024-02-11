from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow, QMenuBar, QStatusBar, QFileDialog
from PyQt6.QtGui import QAction,QIcon,QFont
import sys

class Window(QMainWindow):
    
    def  __init__(self):
        super().__init__()
        self.setWindowTitle("Ben's PyQt window")
        self.setWindowIcon(QIcon("gt.png"))
        self.setGeometry(500,200,500,400)
        self.create_menu_bar()
        
        self.create_widgets()


    def create_widgets(self):
        btn = QPushButton("Click me",self)
        btn.setGeometry(100,100,100,100)
        btn.setStyleSheet('background-color: blue')
        btn.setIcon(QIcon('football.png'))
        btn.clicked.connect(self.clicked_btn)
        
        self.label = QLabel ("My Label",self)
        self.label.setGeometry(100,220,200,100)
        self.label.setStyleSheet('color:green')
        self.label.setFont(QFont("Times New Roman",15))
        
        
    def clicked_btn(self):
        self.label.setText("text has changed")
        self.label.setStyleSheet('background color:red')
        
        
    

    def create_menu_bar(self):
        menu_bar = self.menuBar()  # Create the menu bar

        # Create menus
        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")
        settings_menu = menu_bar.addMenu("Settings")
        

        # Create actions for the File menu
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        open_action = QAction("&Open CSV", self)
        open_action.triggered.connect(self.open_csv_file)
        file_menu.addAction(open_action)
        
    def open_csv_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)")
        if file_name:
            print(file_name)  # Here you will process the CSV file


        
        
        
                
        
        
        
        
app = QApplication([])
window = Window()
window.show()

sys.exit(app.exec())