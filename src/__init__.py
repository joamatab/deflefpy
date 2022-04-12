"""
deflefpy is a DEF-LEF file parser for Python, written in Python.
"""

__version__ = '0.1.0'
__author__  = 'Diogo André Silvares Dias'
__email__   = 'das.dias@campus.fct.unl.pt'

import warnings
from src.util import (
    Unsupported,
    LefDecimal,
    LefPoint,
    LefPort,
)
from src.lef_data import (
    LefLibrary, 
    LefUnits, 
    LefVia, 
    LefViaRule, 
    LefLayerCut, 
    LefLayerRouting,
    LefPin,
)
from src.lef_read import *
from src.lef_write import *

warnings.warn(
    "[DELFEF] DEF (Design Exchange Format) parsing is not yet supported.",
    category = Unsupported,
    stacklevel = 1
)