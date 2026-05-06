from src.utils.logger import get_logger

logger = get_logger(__name__)

logger.info("This is an info message")
logger.warning("This is an warning message")
logger.error("This is an error message")