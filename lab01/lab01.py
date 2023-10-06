import pandas as pd

class SampleBase:
  sample_: list[list[str]] = []
  attributes_: list[str] = []
  is_attr_symb_: list[bool] = []

  def __init__(self, value_path: str, attr_path: str):
    df = pd.read_csv(value_path, sep='\t', header=None)
    df_attr = pd.read_csv(attr_path, sep='\t', header=None)

    self.attributes_ = df_attr.columns

    print(df_attr)


SampleBase("iris.txt", "iris-type.txt")