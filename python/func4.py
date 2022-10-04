from google.cloud import logging
logging_client = logging.Client()
log_name = "hello-logging-func4"
logger = logging_client.logger(log_name)

logger.log_text("DEFAULT message", severity="DEFAULT")
logger.log_text("DEBUG message", severity="DEBUG")
logger.log_text("INFO message", severity="INFO")
logger.log_text("NOTICE message", severity="NOTICE")
logger.log_text("WARNING message", severity="WARNING")
logger.log_text("ERROR message", severity="ERROR")
logger.log_text("CRITICAL message", severity="CRITICAL")
logger.log_text("ALERT message", severity="ALERT")
logger.log_text("EMERGENCY message", severity="EMERGENCY")
