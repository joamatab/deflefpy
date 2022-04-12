"""_summary_
A Python implementation for the LEF file reader.
Supports .lef, .json, and .yaml file output.
"""
#TODO
from loguru import logger
from deflefpy.util import Unsupported
import os
import pickle

def test():
    feat = Unsupported("LEF Read")
    logger.info("{}".format(str(feat)))
    logger.info("Project File: {}".format(os.path.abspath(__file__)))