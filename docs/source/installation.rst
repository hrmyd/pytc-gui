============
Installation 
============

**Note**: If you would like to use the `pytc API <https://pytc.readthedocs.io/>`_ in
addition to the GUI, we recommend installing the python scientific computing
stack and then installing pytc-gui via the `pip` method.  

Demo heat files for testing the GUI are 
`here <https://github.com/hrmyd/pytc-gui/blob/master/pytc_install/pytc_demos.zip?raw=true>`_.

Windows or Mac installation
===========================
**For users who only want to use the GUI**

+ **Windows**: download the `installation file <https://github.com/hrmyd/pytc-gui/blob/master/pytc_install/pytc-gui_v1.0.1_setup.exe?raw=true>`_ and follow the prompts for the installer. 
+ **Mac**: download the `dmg <https://github.com/hrmyd/pytc-gui/blob/master/pytc_install/pytc-gui_v1.0.1_osx.dmg?raw=true>`_, unpack it, and then drag the pytc icon into the Applications folder.  

It will install its own mini python scientific computing stack, independent of
other python distributions installed on the system.

pip installation (windows, mac, or linux)
=========================================
**For users who want to use the GUI and API or for users who want to use an
existing python installation**

Make sure that python3 and pip3 are already installed (see below).

**Option 1: pip.** In a terminal, type:
::

  pip3 install pytc-gui

**Option 2: git.**  In a terminal, type:
::

  git clone https://github.com/harmslab/pytc-gui.git
  cd pytc-gui
  pip3 install .

Installing python3
==================

You can obtain python3 from the following sources:

* `Anaconda <https://www.continuum.io/downloads>`_. A single large installation
  with binaries for windows, mac, and linux.
* `WinPython <https://winpython.github.io/>`_. A single large installation for
  windows.
* Package managers (linux and mac). For example, the Ubuntu command would be: 
  :code:`sudo apt-get install python3 python3-pip`
* `python.org <https://www.python.org/downloads/>`_. The main python binary for
  windows, mac, and linux. 

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
