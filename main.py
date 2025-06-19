import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QVBoxLayout, QMessageBox

class PyToExeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyToEXE Helper")
        self.setGeometry(200, 200, 400, 200)

        self.label = QLabel("Vyber Python (.py) súbor na konverziu:", self)
        self.button_select = QPushButton("Vybrať .py súbor", self)
        self.button_convert = QPushButton("Konvertovať na .exe", self)

        self.button_select.clicked.connect(self.select_file)
        self.button_convert.clicked.connect(self.convert_to_exe)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_select)
        layout.addWidget(self.button_convert)
        self.setLayout(layout)

        self.py_file = ""

    def select_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Vybrať Python súbor", "", "Python súbory (*.py)")
        if file_path:
            self.py_file = file_path
            self.label.setText(f"Vybraný súbor: {os.path.basename(file_path)}")

    def convert_to_exe(self):
        if not self.py_file:
            QMessageBox.warning(self, "Chyba", "Najprv vyber .py súbor.")
            return

        # Príkaz na konverziu .py -> .exe pomocou pyinstaller
        exe_name = os.path.splitext(os.path.basename(self.py_file))[0]
        command = f'pyinstaller --onefile --noconsole "{self.py_file}"'

        QMessageBox.information(self, "Prebieha konverzia", "Okno príkazového riadka sa otvorí. Počkajte na dokončenie.")
        os.system(command)

        QMessageBox.information(self, "Hotovo", f"EXE súbor bude v priečinku dist\\{exe_name}.exe")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PyToExeApp()
    window.show()
    sys.exit(app.exec())
    
