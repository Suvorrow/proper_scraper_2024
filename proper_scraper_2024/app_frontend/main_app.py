import sys

from PySide6.QtWidgets import QApplication



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Scraper")

    scrApp = MainWindow(app)

    scrApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Application')