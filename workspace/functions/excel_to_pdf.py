import pandas as pd
from xhtml2pdf import pisa

def load_excel(path: str) -> pd.DataFrame:
    """excelファイルを読み込む
       全シート読み込む

    Args:
        path (str): excelファイルへのパス

    Returns:
        pd.DataFrame: excelデータ
    """

    return pd.read_excel(path, sheet_name=None, index_col=0)

def output_to_pdf(
        data: pd.DataFrame,
        output_path: str
        ) -> None:
    """DataFrameをPDFファイルへ出力する

    Args:
        data (pd.DataFrame): _description_
    """

    with open(output_path, "w+b") as file:
        pisa.CreatePDF(src=data.to_html(), dest=file)

