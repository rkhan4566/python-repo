#Python Logging
#Logging is a crucial aspect of any application,
#  providing a way to track events, errors, and operational information.
#  Python’s built-in logging module offers a flexible framework for emitting log messages from Python programs.
#  In this lesson, we will cover the basics of logging, including how to configure logging, log levels, and best practices for using logging in Python applications.

import logging 

#configure the basics logging settings
logging.basicConfig(level=logging.DEBUG)

##log messege
logging.debug("this is debug messege")
logging.info("this is info messege")
logging.warning("this is the warning messege")
logging.error("this is an error messege")
logging.critical("this is a critical messege")

#configuring logging
import logging

logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(levelname)s-%(messege)s',
    datefmt='%Y-%M-%d %H:%M:%S'
)
##logging messege with different severity levels
logging.debug("this is debug messege")
logging.info("this is info messege")
logging.warning("this is the warning messege")
logging.error("this is an error messege")
logging.critical("this is a critical messege")


import logging

logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.debug("this is debug message")
logging.info("this is info message")
logging.warning("this is the warning message")
logging.error("this is an error message")
logging.critical("this is a critical message")
