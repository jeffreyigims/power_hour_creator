import logging
import sys

from PyQt5 import QtWidgets, QtCore

from power_hour_creator.ui.main_window import build_main_window
from .boot import bootstrap_app


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logger = logging.getLogger()
    logger.critical("Uncaught exception:", exc_info=(exc_type, exc_value, exc_traceback))
    sys.exit(1)

sys.excepthook = handle_exception


def launch_app():
    app = QtWidgets.QApplication(sys.argv)
    bootstrap_app()
    logger = logging.getLogger(__name__)
    logger.info("Bootstrapping app environment")
    logger.info("Launching GUI")
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    logger.info("Showing main window")
    app.main_window = build_main_window(app)
    app.main_window.show()
    return app


def main():
    app = launch_app()

    sys.exit(app.exec_())

