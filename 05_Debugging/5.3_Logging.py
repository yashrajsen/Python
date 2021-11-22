# to enable logging module
import logging
# call basic Config function with below parameters
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# to log all the log info in a file, use the below parameters
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#to diable all the logging, we use the disable function below
# logging.disable(logging.CRITICAL) # disables all critical and lower
#levels of logging types from high to low
# 1 - CRITICAL
# 2 - ERROR
# 3 - WARNING
# 4 - INFO
# 5 - DEBUG

##Buggy Factorial Program

logging.debug('Start of Program')
def factorial(n):
    logging.debug('Start of factorial (%s)' % (n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i,total))
    
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))