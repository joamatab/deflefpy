"""
deflefpy is a DEF-LEF file parser for Python, written in Python.
"""

__version__ = '0.1.3'
__author__  = 'Diogo André Silvares Dias'
__email__   = 'das.dias@campus.fct.unl.pt'

from loguru import logger
import os
import warnings

from deflefpy.util import (
    Unsupported,
    LefDecimal,
    LefPoint,
    LefPort,
)
from deflefpy.lef_data import (
    LefLibrary, 
    LefUnits, 
    LefVia, 
    LefViaRule, 
    LefLayerCut, 
    LefLayerRouting,
    LefPin,
)
from deflefpy.lef_read import *
from deflefpy.lef_write import *

print("deflefpy, version {}".format(__version__))
logger.info("Project File: {}".format(os.path.abspath(__file__)))

warnings.warn(
    "[DELFEF] DEF (Design Exchange Format) parsing is not yet supported.",
    category = Unsupported,
    stacklevel = 1
)
