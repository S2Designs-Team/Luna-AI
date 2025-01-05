import logging

class LoggerManager:
    def __init__(self):
        
        logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
        self.logger = logging.getLogger("LunaLogger")
        self.logger.setLevel(logging.DEBUG)

        # Console Handler
        #gui_console_handler = logging.StreamHandler()
        #gui_console_handler.setLevel(logging.DEBUG)
        #gui_console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        #gui_console_handler.setFormatter(gui_console_formatter)
        #self.logger.addHandler(gui_console_handler)

        # Consumers (ad esempio GUI)
        self.consumers = []

    def add_consumer(self, log_function, loglevel):
        """Registra una funzione per ricevere i log"""
        class CallbackHandler(logging.Handler):
            def __init__(self, callback):
                super().__init__()
                self.callback = callback

            def emit(self, record):
                log_entry = self.format(record)
                self.callback(log_entry)

        handler = CallbackHandler(log_function)
        handler.setLevel(loglevel)
        handler_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(handler_formatter)        
        self.logger.addHandler(handler)

    def getLogger(self, name=None):
        if not name or isinstance(name, str) and name == logging.root.name:
            return logging.root
        return logging.getLogger(name)


    def log(self, level, message):
        """Logga un messaggio"""
        if level == "info":
            self.logger.info(message)
        elif level == "error":
            self.logger.error(message)
        elif level == "debug":
            self.logger.debug(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "critical":
            self.logger.critical(message)

    def info(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'INFO'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.info("Houston, we have a %s", "interesting problem", exc_info=1)
        """
        self.logger.info(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'ERROR'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.error("Houston, we have a %s", "major problem", exc_info=1)
        """
        self.logger.error(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'DEBUG'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.debug("Houston, we have a %s", "thorny problem", exc_info=1)
        """
        self.logger.debug(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'WARNING'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.warning("Houston, we have a %s", "bit of a problem", exc_info=1)
        """
        self.logger.warning(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'CRITICAL'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.critical("Houston, we have a %s", "major disaster", exc_info=1)
        """
        self.logger.critical(msg, *args, **kwargs)