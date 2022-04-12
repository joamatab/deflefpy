"""
deflefpy is a DEF-LEF file parser for Python, written in Python.
"""

__version__ = '0.1.0'
__author__  = 'Diogo André Silvares Dias'
__email__   = 'das.dias@campus.fct.unl.pt'

from loguru import logger
import os
import warnings

from src.deflefpy.util import (
    Unsupported,
    LefDecimal,
    LefPoint,
    LefPort,
)
from src.deflefpy.lef_data import (
    LefLibrary, 
    LefUnits, 
    LefVia, 
    LefViaRule, 
    LefLayerCut, 
    LefLayerRouting,
    LefPin,
)
from src.deflefpy.lef_read import *
from src.deflefpy.lef_write import *

print("deflef_py, Version 0.1.0")
logger.info("Project File: {}".format(os.path.abspath(__file__)))

warnings.warn(
    "[DELFEF] DEF (Design Exchange Format) parsing is not yet supported.",
    category = Unsupported,
    stacklevel = 1
)
