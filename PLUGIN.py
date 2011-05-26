# source: http://technogeek.org/python-module.html

import imp
import sys
import os

def use_plugin(name, globals=None, locals=None, fromlist=None):
    # Fast path: see if the module has already been imported.
    try:
        return sys.modules[name]

    except KeyError:
        pass

    # If any of the following calls raises an exception,
    # there's a problem we can't handle -- let the caller handle it.
	
	fp, pathname, description = imp.find_module(name, [os.path.dirname(sys.argv[0]) + "\plugins"])
	
    try:
        return imp.load_module(name, fp, pathname, description)
    finally:
        # Since we may exit via an exception, close fp explicitly.
        if fp:
            fp.close()