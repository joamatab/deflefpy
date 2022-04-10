"""_summary_
A Python implementation for the DEF file reader.
Supports .def, .json, and .yaml file output.
"""
#TODO
from loguru import logger
from util import Unsupported
import os

def __init__():
    feat = Unsupported("DEF Read")
    logger.info("{}".format(str(feat)))
    logger.info("Project File: {}".format(os.path.abspath(__file__)))