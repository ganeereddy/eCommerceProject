import logging

class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(filename='.\\Logs\\automation.log', level=logging.DEBUG, force=True)
        logging.basicConfig(filename='.\\Logs\\automation.log',
                            level=logging.INFO, force=True,
                            format='%(asctime)s %(levelname)s %(threadName)-10s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


