# 1 - Suppose you're building a logging library for a web application that needs to keep track of all
#     requests and responses. You want to use the Singleton pattern to ensure that there's only one instance of
#     the logger class throughout the application.
class Logger:
    instance = None
    
    def __new__(cls):
        # this will ensure that there's no other instance of the class Logger
        if cls.instance is None:
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance


if __name__ == '__main__':
    # let's check what we did
    logger1 = Logger()
    logger2 = Logger()
    
    print("The Singleton Worked? " + str(logger1 is logger2))
