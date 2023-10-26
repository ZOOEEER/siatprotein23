import time
import hashlib

import pandas as pd




def read_csv(filename:str) -> pd.DataFrame:
    return pd.read_csv(filename, index_col=0).fillna("")

def random_str(n:int=10) -> str:
    return md5(str(time.time()))[:10]

def md5(key: str) -> str:
    """md5.

    Args:
        key (str): string to be hasehd
    Returns:
        Hashed encoding of str
    """
    return hashlib.md5(key.encode()).hexdigest()
