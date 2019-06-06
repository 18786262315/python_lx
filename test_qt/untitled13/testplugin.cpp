#include "test.h"
#include "testplugin.h"

#include <QtPlugin>

testPlugin::testPlugin(QObject *parent)
    : QObject(parent)
{
    m_initialized = false;
}

void testPlugin::initialize(QDesignerFormEditorInterface * /* core */)
{
    if (m_initialized)
        return;

    // Add extension registrations, etc. here

    m_initialized = true;
}

bool testPlugin::isInitialized() const
{
    return m_initialized;
}

QWidget *testPlugin::createWidget(QWidget *parent)
{
    return new test(parent);
}

QString testPlugin::name() const
{
    return QLatin1String("test");
}

QString testPlugin::group() const
{
    return QLatin1String("");
}

QIcon testPlugin::icon() const
{
    return QIcon();
}

QString testPlugin::toolTip() const
{
    return QLatin1String("");
}

QString testPlugin::whatsThis() const
{
    return QLatin1String("");
}

bool testPlugin::isContainer() const
{
    return false;
}

QString testPlugin::domXml() const
{
    return QLatin1String("<widget class=\"test\" name=\"test\">\n</widget>\n");
}

QString testPlugin::includeFile() const
{
    return QLatin1String("test.h");
}
#if QT_VERSION < 0x050000
Q_EXPORT_PLUGIN2(testplugin, testPlugin)
#endif // QT_VERSION < 0x050000
