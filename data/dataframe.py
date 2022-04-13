def remove_adjacent(data):
  assert all(i in data.columns for i in ["KP_beg","KP_end"]), "KP_beg and KP_end columns must be in data"
  if len(data) <= 1: return data
  
  data = (data
    .sort_values("KP_beg")
    .reset_index(drop=True))

  index = 1
  length = len(data)

  old_rows = length

  while index < length:
    first = data.loc[index-1].drop(["KP_beg","KP_end"])
    second = data.loc[index].drop(["KP_beg","KP_end"])

    KP_beg = data.at[index,"KP_beg"]
    KP_end = data.at[index-1,"KP_end"]

    if first.equals(second) and KP_beg == KP_end:
      data.at[index-1,"KP_end"] = data.at[index,"KP_end"]
      data = data.drop(index).reset_index(drop=True)
      index -= 1
    length = len(data)
    index += 1
  print(f"Rows reduced from {old_rows} to {len(data)}")
  return data

def replace_bool(data):
  for column in data.columns:
    temp = data[column].drop_duplicates().dropna()
    if len(temp) <= 2 and all(i == 1 or i == 0 for i in temp):
      data[column] = data[column].replace(1,True).replace(0,False)

def alpha_to_num(col_alpha):
  """Returns the number corresponding to an alphabetic index"""
  numbers = [ord(i) - 97 for i in col_alpha.lower()]
  return sum([i + index*26 for index,i in enumerate(numbers)])