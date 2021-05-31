# -*- coding: utf-8 -*-
"""
python module logging 对应的配置文件，使用py格式而不是json，是为了方便传递
"""

logging_config = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "simple": {
            "format": "%(levelname)s %(message)s"
        },
        "standard": {
            "format": "[%(asctime)s] %(levelname)s [%(funcName)s:%(lineno)d] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose"
        },
        "file_handler": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "formatter": "verbose",
            # TODO 未来把log的落盘配置写在config里，只留一个需修改文件
            "filename": "logs/log.txt",
            "encoding": "utf8"
        }
    },
    "loggers": {
        "": {
            "handlers": ["console", "file_handler"],
            # TODO 未来把log的level配置写在config里，只留一个需修改文件
            "level": "DEBUG"
        }
    }
}