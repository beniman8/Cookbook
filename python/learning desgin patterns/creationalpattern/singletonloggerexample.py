import logging
import threading
from abc import ABC,ABCMeta,abstractmethod
import os 
import datetime

# #set up the logger
# logger = logging.getLogger('my_logger')
# logger.setLevel(logging.DEBUG)


# #create a file handler and set is level to Debug
# file_handler = logging.FileHandler('my_log_file.log')
# file_handler.setLevel(logging.DEBUG)

# # create a console handler and set its level to INFO
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)

# # Create a formatter and add it to the handlers
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# console_handler.setFormatter(formatter)


# #add the handlers to the logger
# logger.addHandler(file_handler)
# logger.addHandler(console_handler)


###################################################
# Now you can use the logger to output messages
# logger.debug('This is a debug message ')
# logger.info('This is a info message ')
# logger.warning('This is a warning message ')
# logger.error('This is a error message ')
# logger.critical('This is a critical message ')


################# SINGLETON LOGGER iteration 1 ###################################


# #define single ton class
# class SingletonLogger:
#     # initialize the class-level instance variable to None
#     _instance = None
#     # initialize a lock to ensure thread-safe singleton instantiation
#     _lock = threading.Lock()

#     # class method to get the singletonlogger instance
#     @classmethod
#     def get_instance(cls):
#         # Acquire the lock to ensure thread safety
#         with cls._lock:
#             # if an instance of singletonlogger does not exist,create one
#             if cls._instance is None:
#                 cls._instance = cls()
#                 # Initialize the logger for the singletonlogger instance
#                 cls._instance._initialize_logger()
#             # return the existing or newly created singletonlogger instance
#             return cls._instance

#     # helper method to initialize the logger
#     def _initialize_logger(self):
#         #Create a logger object with the specified name
#         self.logger =logging.getLogger('my_logger')
#         # set the logging level to debug
#         self.logger.setLevel(logging.DEBUG)

#         #create a file handler and set is level to Debug
#         file_handler = logging.FileHandler('my_log_file.log')
#         file_handler.setLevel(logging.DEBUG)

#         # create a console handler and set its level to INFO
#         console_handler = logging.StreamHandler()
#         console_handler.setLevel(logging.INFO)

#         # Create a formatter and add it to the handlers
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         file_handler.setFormatter(formatter)
#         console_handler.setFormatter(formatter)


#         #add the handlers to the logger
#         self.logger.addHandler(file_handler)
#         self.logger.addHandler(console_handler)

# ###################################################
# #Now you can use the logger to output messages
# logger=SingletonLogger().get_instance().logger
# logger.debug('This is a debug message ')
# logger.info('This is a info message ')
# logger.warning('This is a warning message ')
# logger.error('This is a error message ')
# logger.critical('This is a critical message ')


################# SINGLETON LOGGER iteration 2 ###################################

# #define a metaclass singleton that inherits from type
# class SingletonMeta(type):
#     #initialise dictionary to store instances of the singleton class
#     _instances ={}
#     #initialize a lock to ensure thread safe singleton instantiation
#     _lock = threading.Lock()

#     #override the call methods to control how the class ins instantiated
#     def __call__(cls, *args, **kwds):
#         # acquire the lock to ensure thead safety
#         with cls._lock:
#             #if the class is not in the instances dictionary create a mew instance
#             if cls not in cls._instances:
#                 cls._instances[cls] = super(SingletonMeta,cls).__call__(*args, **kwds)
#             #return the newly created instance of the class
#             return cls._instances[cls]

# #define a logger singleton class with singleton as its metaclass
# class Logger(metaclass=SingletonMeta):
#     _logger = None

#     def __init__(self):
#         self._initialize_logger()

#     #method to initialize the logger
#     def _initialize_logger(self):
#         print('<Logger init> initializing logger...')
#         #Create a logger object with the specified name
#         self._logger =logging.getLogger('my_logger')
#         # set the logging level to debug
#         self._logger.setLevel(logging.DEBUG)

#         #create a file handler and set is level to Debug
#         file_handler = logging.FileHandler('my_log_file.log')
#         file_handler.setLevel(logging.DEBUG)

#         # create a console handler and set its level to INFO
#         console_handler = logging.StreamHandler()
#         console_handler.setLevel(logging.INFO)

#         # Create a formatter and add it to the handlers
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         file_handler.setFormatter(formatter)
#         console_handler.setFormatter(formatter)


#         #add the handlers to the logger
#         self._logger.addHandler(file_handler)
#         self._logger.addHandler(console_handler)

#     # getter method
#     def getLogger(self):
#         return self._logger

# # ###################################################
# # #Now you can use the logger to output messages
# logger=Logger().getLogger()
# logger.debug('This is a debug message ')
# logger.info('This is a info message ')
# logger.warning('This is a warning message ')
# logger.error('This is a error message ')
# logger.critical('This is a critical message ')


################# SINGLETON LOGGER Final version ###################################


class SingletonMeta(metaclass=ABCMeta):
    _instances = {}
    # initialize a lock to ensure thread-safe singleton instantiation
    _lock = threading.Lock()

    def __call__(cls, *args, **kwds):
        # Acquire the lock to ensure thread safety
        with cls._lock:
            print("<SingletonMeta> int the _call_...")
            if cls not in cls._instances:
                cls._instances[cls]
                cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwds)
            # return the newly created instance of the class
            return cls._instances[cls]


class BaseLogger(SingletonMeta):
    @abstractmethod
    def debug(cls, message: str):
        pass

    @abstractmethod
    def info(cls, message: str):
        pass

    @abstractmethod
    def warning(cls, message: str):
        pass

    @abstractmethod
    def error(cls, message: str):
        pass

    @abstractmethod
    def critical(cls, message: str):
        pass


class MyLogger(BaseLogger):

    def __init__(self):
        print("<Logger init> initializing logger...")
        # Create a logger object with the specified name
        self._logger = logging.getLogger("my_logger")
        # set the logging level to debug
        self._logger.setLevel(logging.DEBUG)

        # create a file handler and set is level to Debug
        file_handler = logging.FileHandler("my_log_file.log")
        file_handler.setLevel(logging.DEBUG)

        # create a console handler and set its level to INFO
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create a formatter and add it to the handlers
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # add the handlers to the logger
        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def debug(self, message):
        self._logger.debug(message)

    def info(self, message):
        self._logger.info(message)

    def warning(self, message):
        self._logger.warning(message)

    def error(self, message):
        self._logger.error(message)

    def critical(self, message):
        self._logger.critical(message)


# #Now you can use the logger to output messages
logger = MyLogger()
logger.debug("This is a debug message ")
logger.info("This is a info message ")
logger.warning("This is a warning message ")
logger.error("This is a error message ")
logger.critical("This is a critical message ")
