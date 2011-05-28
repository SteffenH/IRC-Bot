# source: http://technogeek.org/python-module.html

import imp
import sys
import os

def use_plugin(name, plugin_path, globals=None, locals=None, fromlist=None):
    # Fast path: see if the module has already been imported.
    try:
        return sys.modules[name]

    except KeyError:
        pass

    # If any of the following calls raises an exception,
    # there's a problem we can't handle -- let the caller handle it.
	
	#head, tail = os.path.split(plugin_path)
	#print head, tail
	#print os.path.join(head, "plugins")
	
	fp, pathname, description = imp.find_module(name, [plugin_path])#[os.path.join(head, "plugins")])
	
    try:
        return imp.load_module(name, fp, pathname, description)
    finally:
        # Since we may exit via an exception, close fp explicitly.
        if fp:
            fp.close()