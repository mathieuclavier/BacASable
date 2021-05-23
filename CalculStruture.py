import sys
from PyQt5.QtWidgets import QApplication, QWidget

monApp=QApplication(sys.argv)
w=QWidget()
w.resize(500,300)
w.move(500, 500)
w.setWindowTitle("Titre de fenêtre")
w.show()

sys.exit(monApp.exec_())
