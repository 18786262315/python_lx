CONFIG      += plugin debug_and_release
TARGET      = $$qtLibraryTarget(testplugin)
TEMPLATE    = lib

HEADERS     = testplugin.h \
    dialog.h \
    mainwindow.h
SOURCES     = testplugin.cpp \
    dialog.cpp \
    mainwindow.cpp
RESOURCES   = icons.qrc
LIBS        += -L. 

greaterThan(QT_MAJOR_VERSION, 4) {
    QT += designer
} else {
    CONFIG += designer
}

target.path = $$[QT_INSTALL_PLUGINS]/designer
INSTALLS    += target

include(test.pri)

FORMS += \
    dialog.ui \
    mainwindow.ui
