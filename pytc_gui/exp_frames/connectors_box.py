from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import pytc
import inspect

from .base import Experiments
from .. import slider_popup
from .. import sliders

class ConnectorsBox(Experiments):
    """
    hold global parameter/sliders
    """
    def __init__(self, name, connector, parent):
        """
        """
        self._connector = connector
        self._linked_list = []
        self._main_box = parent._main_box
        self._exp = None

        super().__init__(name, parent)

    def exp_widgets(self):
        """
        create slider
        """
        self._remove_name = "Unlink From All"
        
        # see if global variable is a connector or simple var
        param = self._connector.params

        for p, v in param.items():
            s = sliders.GlobalSliders(p, self)
            self._slider_list["Global"][self._name].append(s)

    def slider_popup(self):
        """
        hide and show slider window
        """
        self._slider_window = slider_popup.ConnectorPopUp(self)
        self._slider_window.show()

    def linked(self, loc_slider):
        """
        """
        self._linked_list.append(loc_slider)

    def unlinked(self, loc_slider):
        """
        remove item from linked list if local param unlinked from global param
        """
        self._linked_list.remove(loc_slider)

        # if nothing linked, delete the glob exp object
        if len(self._linked_list) == 0:
            self.remove()

    def remove(self):
        """
        """
        try:
            self._fitter.remove_global(self._name)
            self._slider_list["Global"].pop(self._name, None)
            self._global_tracker.pop(self._name, None)
            
            for s in self._linked_list:
                s.reset()
        except:
            pass

        self.close()
