import logging
logging.basicConfig(filename='log.txt',filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

for i in range(0,10):
    if (i%2==0):
        logging.warning("Divisible by 2")
    elif (i%3==0):
        logging.critical("Divisible by 3")
    else:
        logging.error("Other than 2 and 3")
