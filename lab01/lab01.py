import pandas
import pandas as pd

class SampleBase:
  samples: list[list[str]] = []
  attributes: list[str] = []
  is_atr_char: list[bool] = []
  df: pandas.DataFrame

  def __init__(self, value_path: str, attr_path: str):
    df_attr = pd.read_csv(attr_path, sep='\t', header=None)
    self.df = pd.read_csv(value_path, sep='\t', header=None, names=df_attr[0])

    self.attributes = df_attr[0].tolist()

    for _, row in self.df.iterrows():
      self.samples.append(row.tolist())

    for _, row in df_attr.iterrows():
      self.is_atr_char.append(row[1] == "s")

  def get_all_samples(self) -> list[list[str]]:
    return self.samples

  def get_sample(self, col: int, row: int) -> str:
    if row > len(self.samples) or col > len(self.samples[0]):
      return "Index out of range"

    return self.samples[row][col]

  def get_all_attributes(self):
    return self.is_atr_char

  def is_attribute_char(self, index: int):
    if index > len(self.is_atr_char):
      return "Index out of range"

    return self.is_atr_char[index]

  def get_df(self):
    return self.df


base = SampleBase("iris.txt", "iris-type.txt")
print(base.get_sample(1,0))
print(base.get_all_samples())
print(base.get_df())
