from loguru import logger
import os

def main():
    print("deflef_py, Version 0.1.0")
    logger.info("Project File: {}".format(os.path.abspath(__file__)))
    
if __name__ == "__main__":
    main()