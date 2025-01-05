import logging
import multiprocessing
from   logging.handlers import QueueHandler, QueueListener

class ProcessLogger:
    _message_queue         = multiprocessing.Queue()
    _log_consumer_callback = None
    _listener              = None
    _logger:logging.Logger = None

    def __init__(self, par_process_name=None, par_logger_callback=None):
        self.process_name    = par_process_name
        self.logger_callback = par_logger_callback
        self._logger         = self.get_logger(par_process_name)

    @classmethod
    def initialize(cls, callback=None):
        """
        Inizializza il listener per gestire i messaggi nella coda.
        """
        """
        if cls._listener is None:
            # Configura il listener con un handler base
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

            cls._listener = QueueListener(
                cls._message_queue,
                cls._handle_message,
                respect_handler_level=True
            )
            cls._listener.start()

        cls._log_consumer_callback = callback
        """
        logger = logging.getLogger()
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)




    @classmethod
    def _handle_message(cls, record):
        """
        Gestisce i messaggi nella coda: log o messaggi operativi.
        """
        if isinstance(record, logging.LogRecord):
            logging.getLogger(record.name).handle(record)
            if cls._log_consumer_callback:
                cls._log_consumer_callback(record)
        elif isinstance(record, dict):
            cls._process_message(record)

    @classmethod
    def _process_message(cls, message):
        """
        Elabora i messaggi operativi ricevuti.
        """
        print(f"[Message Queue] Received message: {message}")

    @classmethod
    def get_logger(cls, par_logger_name:str=None):
        """
        Crea e restituisce un logger configurato per inviare messaggi nella coda.
        """
        if not par_logger_name == None:
            _logger = logging.getLogger(par_logger_name)
        else: 
            _logger = logging.getLogger()
        if not _logger.handlers:  # Assicurati che il logger non abbia già handler
            _logger.setLevel(logging.DEBUG)
            _logger.addHandler(QueueHandler(cls._message_queue))
        return _logger


    @classmethod
    def send_message(cls, message):
        """
        Invia un messaggio operativo nella coda.
        """
        cls._message_queue.put(message)

    @classmethod
    def set_log_consumer_callback(cls, callback):
        """
        Imposta il callback per gestire i log a livello dell'interfaccia grafica.
        """
        cls._log_consumer_callback = callback


    def log(self, level, message):
        """
        Logga un messaggio con il livello specificato.
        """
        formatted_message = f"[{self.process_name}] {message}"
        if level.lower() == "info":
            self._logger.info(formatted_message)
        elif level.lower() == "warning":
            self._logger.warning(formatted_message)
        elif level.lower() == "error":
            self._logger.error(formatted_message)
        elif level.lower() == "debug":
            self._logger.debug(formatted_message)
        # Callback personalizzato
        if self.logger_callback:
            self.logger_callback(formatted_message)


    def info(self, msg, *args, **kwargs):
        """
        Logs an INFO level message.
        """
        self.log("info", msg)

    def debug(self, msg, *args, **kwargs):
        """
        Logs a DEBUG level message.
        """
        self.log("debug", msg)

    def warning(self, msg, *args, **kwargs):
        """
        Logs a WARNING level message.
        """
        self.log("warning", msg)

    def error(self, msg, *args, **kwargs):
        """
        Logs an ERROR level message.
        """
        self.log("error", msg)
