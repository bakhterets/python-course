import os
import logging
import logging.config
import re
from pathlib import Path


"""
Logger config
Logger function returns logger
"""

def get_logger(log_dir: Path = Path("."), script_name: str = Path(__file__).name, log_level: str = "INFO"):

    # Directory validation
    if not os.path.exists(log_dir):
        print("a logging directory is currently being created..")
        os.makedirs(log_dir)
        print("This is logdir: " + str(log_dir))

    regex = "^.*\.py$"
    pattern = re.compile(regex)
    
    # logger name validation 
    if pattern.search(script_name) is not None:
        logger_name = (script_name).rstrip(".py")
    else:
        logger_name = script_name

    print("Logger name is: " + str(logger_name))
    log_name = str(logger_name) + ".log"
    base_log_path = os.path.join(log_dir, log_name)
    print("base log path is: " + str(base_log_path))

    # log level validation
    list_of_levels = ["DEBUG","INFO","WARNING","ERROR","CRITICAL"]
    log_level = (str(log_level)).upper()
    if log_level not in list_of_levels:
        log_level = "INFO"
    
    dictLogConfig = {
        "version":1,
        "handlers":{
            "RotatingFileHandler":{
                "class":"logging.handlers.RotatingFileHandler",
                "formatter":"ddFormatter",
                "filename": base_log_path,
                "mode":"a",
                "maxBytes": 2097152,
                "backupCount": 3
            }
        },
        "loggers":{
            logger_name:{
                "handlers":["RotatingFileHandler"],
                "level": log_level,
            }
        },
        "formatters":{
            "ddFormatter":{
                "format":"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        }
    }
    
    logging.config.dictConfig(dictLogConfig)
    logger = logging.getLogger(logger_name)
    print("Log file name is: " + str(log_name))
    print("Log level  is: " + str(log_level))
    return logger
