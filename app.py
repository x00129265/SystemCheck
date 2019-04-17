import importlib
PLUGINS = "dbPlugin", "osPlugin", "dbUserPlugin"

for plugin in PLUGINS:
    print("***** Plugin: {} *****".format(plugin))
    plugin_module = importlib.import_module("plugins."+plugin, ".")
    plugin_exe = plugin_module.Plugin()
    plugin_exe.execute()
    print()

