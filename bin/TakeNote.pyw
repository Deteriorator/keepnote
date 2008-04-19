#!/usr/bin/env python

import sys, os


# pygtk imports
import pygtk
pygtk.require('2.0')
import gtk

basedir = os.path.dirname(os.path.realpath(sys.argv[0]))
basedir = os.path.split(basedir)[0]



try:
    import takenote
except ImportError:
    sys.path.append(basedir)
    import takenote
    
import takenote.gui



#=============================================================================

def main():
    gtk.main()


if __name__ == "__main__":
    app = takenote.gui.TakeNote(basedir)
    
    if len(sys.argv) > 1:
        app.open_notebook(sys.argv[1].rstrip("/"))
        
    elif app.pref.default_notebook != "":
        # open default
        app.open_notebook(app.pref.default_notebook)
    
    main()

