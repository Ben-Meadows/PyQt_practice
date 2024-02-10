from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QAction,QIcon,QFont
import sys

class Window(QWidget):
    
    def  __init__(self):
        super().__init__()
        self.setWindowTitle("Ben's PyQt window")
        self.setWindowIcon(QIcon("gt.png"))
        self.setGeometry(500,200,500,400)
        
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
        
        
        
                
        
        
        
        
app = QApplication([])
window = Window()
window.show()

sys.exit(app.exec())