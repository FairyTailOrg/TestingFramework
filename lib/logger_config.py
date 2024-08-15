"""Logger to be used in the project."""
import logging


def setup_logger(name='framework log', log_file='framework_log.log', level=logging.DEBUG):  # noqa: E501
    """Configure the logger to be used.

    Args:
        name (str, optional): Name of the logger. Defaults to 'framework log'.
        log_file (str): Logger file path. Defaults to 'framework_log.log'.
        level (_type_, optional): Log level to use. Defaults to logging.DEBUG.

    Returns:
        _type_: _description_
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - [PID %(process)d]- %(name)s - %(levelname)s - %(message)s')  # noqa: E501
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
