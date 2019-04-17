import importlib
PLUGIN_NAME = "plugins.dbPlugin"

plugin_module = importlib.import_module(PLUGIN_NAME, ".")
plugin = plugin_module.Plugin("Hello", key=123)
print(plugin.execute(1, 2))

