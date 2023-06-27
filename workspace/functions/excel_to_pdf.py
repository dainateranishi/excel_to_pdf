import pandas as pd

def load_excel(path: str) -> pd.DataFrame:
    """excelファイルを読み込む
       全シート読み込む

    Args:
        path (str): excelファイルへのパス

    Returns:
        pd.DataFrame: excelデータ
    """

    return pd.read_excel(path, sheet_name=None, index_col=0)
