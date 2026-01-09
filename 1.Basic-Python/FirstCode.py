"""import logging
## logging setting

logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s- %(levelname)s -%(messege)s',
        datefmt='%Y-%M-%d %H:%M:%S',
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
)
logger=logging.getLogger("ArithmaticApp")

def add(a,b):
    result=a+b
    logger.debug(f"adding {a} + {b}={result}")
    return result

def substract(a,b):
    result=a-b
    logger.debug(f"substaction {a} - {b}={result}")
    return result

def multiply(a,b):
    result=a*b
    logger.debug(f"multiply {a} * {b}={result}")
    return result

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"divide {a} / {b}={result}")
        return result
    except ZeroDivisionError:
        logger.error("division by zero error")
        return None
    
add(10,15)
substract(15,10)
multiply(10,20)
divide(20,10)
"""
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(a, b):
    result = a + b
    logger.debug(f"add {a} + {b} = {result}")
    return result

def substract(a, b):
    result = a - b
    logger.debug(f"substract {a} - {b} = {result}")
    return 

def multiply(a, b):
    result = a * b
    logger.debug(f"multiply {a} * {b} = {result}")
    return result

def divide(a, b):
    result = a / b
    logger.debug(f"divide {a} / {b} = {result}")
    return result



if __name__ == "__main__":
    add(10, 5)
    divide(20, 10)
    multiply(10,20)
    substract(20,10)



