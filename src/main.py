# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtCore import QLocale, QTranslator
from PyQt5.QtWidgets import QApplication
from bibEditor import BibEditor

if __name__ == "__main__":
    app = QApplication(sys.argv)
    enNativeLang = len(sys.argv) == 1
    LANG_PATH = "../assets/lang/"
    if enNativeLang:
        local = QLocale()
    else:
        langCountry = sys.argv[1]

    translators = []
    for prefixQm in ("biblioapp.", "qt_", "qtbase_"):
        translator = QTranslator()
        translators.append(translator)

        if enNativeLang:
            translator.load(local, LANG_PATH+prefixQm)
        else:
            translator.load(LANG_PATH+prefixQm + langCountry)
        app.installTranslator(translator)

    bib = BibEditor()
    bib.show()
    sys.exit(app.exec_())

#    if len(sys.argv) == 1:
#        local = QLocale()
#        translator.load(local, "biblioapp", ".")
#    else:
#        translator.load("biblioapp." + sys.argv[1])
#
#        translator.load("biblioapp.fr_FR")
