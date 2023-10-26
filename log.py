import sys
import logging
from imp import reload

def main(debug:bool = False, log_file:str = "run.log", *args, **kwargs):

    reload(logging)
    if debug:
        logging_level = logging.DEBUG
    else:
        logging_level = logging.INFO
    logging.basicConfig(
        level=logging_level,
        format="%(asctime)s %(levelname)s: %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_file),
        ],
    )
    logging.debug(f"Logging level: {logging_level}")

class Verbose(object):
    """Verbose.

    Class to handle the verbose.

    Changed from: https://github.com/connorcoley/MolPAL/blob/master/molpal/utils.py

    """

    def __init__(self, msg, verbose, *args, **kwargs):
        """__init__.

        Args:
            msg:
        """
        self.msg = msg
        self.verbose = verbose
        self.logger = logging.getLogger()
        # if verbose:
        #     logging.info(f"{self.msg}")

    def __enter__(self):
        """__enter__."""
        pass

    def __exit__(self, type, value, traceback):
        """__exit__.

        Args:
            type:
            value:
            traceback:
        """
        if self.verbose:
            logging.info(f"{self.msg}")

class Stage(object):
    """Stage.

    Class to handle the stage.

    Changed from: https://github.com/connorcoley/MolPAL/blob/master/molpal/utils.py

    """

    def __init__(self, msg, verbose, *args, **kwargs):
        """__init__.

        Args:
            msg:
        """
        self.msg = msg
        self.verbose = verbose
        self.logger = logging.getLogger()
        # if verbose:
        #     logging.info(f"{self.msg}")

    def __enter__(self):
        """__enter__."""
        if self.verbose:
            logging.info(f"++++ Stage: {self.msg} ++++")

    def __exit__(self, type, value, traceback):
        """__exit__.

        Args:
            type:
            value:
            traceback:
        """
        if self.verbose:
            logging.info(f"---- Done: {self.msg} ----")

def md5(key: str) -> str:
    """md5.

    Args:
        key (str): string to be hasehd
    Returns:
        Hashed encoding of str
    """
    return hashlib.md5(key.encode()).hexdigest()
