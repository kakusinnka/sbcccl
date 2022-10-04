import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("DEBUG message")
logger.info("INFO message")
logger.warning("WARNING message")
logger.error("ERROR message")
logger.critical("CRITICAL message")
logger.exception("EXCEPTION message")