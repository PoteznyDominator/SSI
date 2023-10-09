import pandas as pd

class SampleBase:
  samples: list[list[str]] = []
  attributes: list[str] = []
  is_atr_char: list[bool] = []

  def __init__(self, value_path: str, attr_path: str):
    df_attr = pd.read_csv(attr_path, sep='\t', header=None)
    df = pd.read_csv(value_path, sep='\t', header=None, names=df_attr[0])

    self.attributes = df_attr[0].tolist()

    for _, row in df.iterrows():
      self.samples.append(row.tolist())

    for _, row in df_attr.iterrows():
      self.is_atr_char.append(row[1] == "s")

  def get_all_samples(self) -> list[list[str]]:
    return self.samples

  def get_sample(self, col: int, row: int) -> str:
    return self.samples[row][col]

  def get_all_attributes(self):
    return self.is_atr_char

  def is_attribute_char(self, index: int) -> bool:
    return self.is_atr_char[index]


base = SampleBase("iris.txt", "iris-type.txt")
print(base.get_sample(1,0))