from plugins.pluggable import Pluggable
from plugins.lib.osManager import out


class Plugin(Pluggable):
    def _execute(self):
        print(out("wmic MEMORYCHIP get BankLabel, DeviceLocator, MemoryType, TypeDetail, Capacity, Speed"))
