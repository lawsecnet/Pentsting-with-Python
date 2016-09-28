#
#
# Volhash
#
# Tool for grabbing password hashes from vmem images usisg Volatility framework
#
# As presented in 'Black Hat Python' by Justin Seitz
#
# 


import sys
import struct
import volatility.conf as conf
import volatility.registry as registry

memory_file = "WindowsXPSP2.vmem"
sys.path.append("/volatility-2.4")

registry.PluginImporter()
config = conf.ConfObject()

import volatility.commands as commands
import volatility.addrspace as addrspace


config.parse_options()
config.PROFILE = "WinXPSP2x86"
config.LOCATION = "file://%s" % memory_file

registry.register_global_options(config, commands.Command)
registry.register_global_options(config, addrspace.BaseAddressSpace)

from volatility.plugins.registry.registryapi import registryapi
from volatility.plugins.registry.lsadump import HashDump

registry = RegistryApi(config)
registry.populate_offsets()

sam_offset = None
sys_offset = None

for offset in registry.all_offsets:

    if registry.all_offsets[offset].endwith("\\SAM"):
        sam_offset = offset
        print "[*] System 0x%08x" % offset

    if registry.all_offsets[offset].endwith("\\system"):
        sys_offset = offset
        print "[*] System: 0x%08x" % offset

    if sam_offset is not None and sys_offset is not None:
        config.sys_offset = sys_offset
        config.sam_offset = sam_offset

        hashdump = HashDump(config)

        for hash in hashdump.calculate():
            print hash

        break

if sam_offset in None or sys_offset in None:
    print "[*] Failed to find the system or SAM offset"
