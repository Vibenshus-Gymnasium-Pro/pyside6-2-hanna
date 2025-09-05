# [[file:README.org::*Konvertering af ui-fil til pythonfil][Konvertering af ui-fil til pythonfil:1]]
import sys 
import string
import re
#Import af filen/modulet roeversprog.py -
# Læg mærke til at .py ikke er taget med.
import roeversprog

# Import af de almindelige elementer i pyside6
from PySide6.QtWidgets import QApplication, QMainWindow
# Import af brugerfladen fra pythonfilen, som er generet vha pyside6-uic
from oversaetterlayout_gui import Ui_MainWindow

# Vores nye klasse, som starter med at nedarve fra almindeligt QMainWindow
class oversaetterlayout(QMainWindow):
    def __init__(self):
        super().__init__()
        # Her oprettes self.ui ud fra den klasse som er i den genererede pythonfil
        self.ui = Ui_MainWindow()
        # Her sættes brugerfladen op.
        self.ui.setupUi(self)
        # Her sættes vinduestitlen til noget andet end i Designer.
        # Læg mærke til at self.ui IKKE anvendes men blot self.
        self.setWindowTitle("Konvertering vha pyside6-uic")
        # Her sættes signal og slot op for oversaetknap og metoden oversaet
        self.ui.translatebutton.clicked.connect(self.oversaet)
        
    def oversaet(self):
        # Denne metode anvender funktionen oversaet_til_roeversprog, som
        # ligger i modulet roeversprog (som er importeret i starten)
    
        current_insertlabel_text = self.ui.insertlabel.text()
        current_røversprog_text = self.ui.roversprog.text() 
        # we check which language we are translating to/from
        
        if current_insertlabel_text == "Insert any language here:" and current_røversprog_text == "Røversprog:":
            output_fra_oversaetteren = roeversprog.oversaet_til_roeversprog(self.ui.inputfelt.toPlainText())

        elif current_insertlabel_text == "Indsæt dit røversprog" and current_røversprog_text == "Almindeligt sprog":
            output_fra_oversaetteren = roeversprog.oversaet_fra_roeversprog_til_andet_sprog(
            self.ui.inputfelt.toPlainText())

        self.ui.outputfelt.setPlainText(output_fra_oversaetteren)
        # we use .setPlainText because the outputfelt is a QTextEdit 
        # that way we can extract the text from the inputfelt
        # and put it into the outputfelt

program = QApplication.instance()
if program == None:
    program = QApplication(sys.argv)
oversaetterlayout = oversaetterlayout()
oversaetterlayout.show()
program.exec()
# Konvertering af ui-fil til pythonfil:1 ends here
