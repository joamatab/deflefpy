"""_summary_
A Python implementation for the LEF file writter.
Supports .lef, .json, and .yaml file output.
"""
#TODO
from loguru import logger
from util import Unsupported
import os
import pickle

def __init__():
    feat = Unsupported("LEF Write")
    logger.info("{}".format(str(feat)))
    logger.info("Project File: {}".format(os.path.abspath(__file__)))