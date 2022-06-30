import logging

class Logger:
    def logger_func(file_name='logs.log',leg_level=logging.DEBUG):
        logger = logging.getLogger('demo')
        logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler('scrapping.log')
        
        formater = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s", datefmt="%d-%m-%Y %I:%M:%S %p")
        console_handler.setFormatter(formater)
        file_handler.setFormatter(formater)
        
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        
        return logger