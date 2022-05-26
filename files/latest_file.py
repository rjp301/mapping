import os
import datetime as dt

def latest_file(path,date_format="%Y %m %d",prefix=" - ",suffix="",silent=False) -> tuple:
  files = os.listdir(path)
  files = [i for i in files if not (i.startswith(".") or i.startswith("~"))]
  file_date = []
  for file in files:
    name,_ = os.path.splitext(file)
    try:
      if prefix and suffix: date_str = name[name.index(prefix) + len(prefix):name.index(suffix)]
      elif prefix: date_str = name[name.index(prefix) + len(prefix):]
      elif suffix: date_str = name[:name.index(suffix)]
      else: date_str = name
    except ValueError as e:
      if not silent: print(f"ERROR: {prefix} or {suffix} is not contained within {name}")
      continue
    
    try:
      date = dt.datetime.strptime(date_str,date_format)
    except ValueError as e:
      if not silent: print(f"ERROR: {date_str} does not match the format of {date_format}")
      continue
    
    file_date.append((file,date))

  latest = max(file_date,key=lambda i: i[1])
  fname = os.path.join(path,latest[0])
  date = latest[1]
  return fname,date
