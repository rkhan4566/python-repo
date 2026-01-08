#logging with multiple loggers
#you can create multiple loggers for different parts of your application
import logging
##create a logger for module1
logger1=logging.getLogger("module1")
logger1.setLevel(logging.DEBUG)

#create a logger for multiple2
logger2=logging.getLogger("module2")
logger2.setLevel(logging.WARNING)

#configure logging settings
logging.basicConfig(
level=logging.DEBUG,
format='%(asctime)s-%(name)s - %(levelname)s - %(message)s',
datefmt='%Y-%M-%d %H:%M:%S'



)
#log messege with different loggers
logger1.debug("this is a debug messege")
logger2.warning("this is a warning messege for module2")
logger2.error("this is a error messege")


