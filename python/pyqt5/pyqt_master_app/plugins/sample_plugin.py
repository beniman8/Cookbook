from python.pyqt5.pyqt_master_app.plugins.plugin_interface import Plugin

class SamplePlugin(Plugin):
    def run(self):
        print("Plugin running!")
