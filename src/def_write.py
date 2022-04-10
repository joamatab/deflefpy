"""_summary_
A Python implementation for the DEF file writter.
Supports .def, .json, and .yaml file output.
"""
#TODO
from loguru import logger
from util import Unsupported
import os
import pickle

def __init__():
    feat = Unsupported("DEF Write")
    logger.info("{}".format(str(feat)))
    logger.info("Project File: {}".format(os.path.abspath(__file__)))