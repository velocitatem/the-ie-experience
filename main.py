import random
import requests
import gi
gi.require_version("Gtk", "3.0") # Make sure we have Gtk 3.0
from gi.repository import Gtk # Import Gtk 3.0
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import sys


from windows import GreetingWindow

def main():
    app = QApplication(sys.argv)
    window = GreetingWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__": # If this file is run directly
    main() # Run the program
