
import os
import datetime as dt

def file_date(fname,date_format="%Y %m %d",prefix="",suffix="") -> dt.datetime:
  name,_ = os.path.splitext(os.path.basename(fname))
  try:
    if prefix and suffix: date_str = name[name.index(prefix) + len(prefix):name.index(suffix)]
    elif prefix: date_str = name[name.index(prefix) + len(prefix):]
    elif suffix: date_str = name[:name.index(suffix)]
    else: date_str = name
  except ValueError as e:
    print(f"ERROR: {prefix} or {suffix} is not contained within {name}")
    return False
  
  try:
    date = dt.datetime.strptime(date_str,date_format)
  except ValueError as e:
    print(f"ERROR: {date_str} does not match the format of {date_format}")
    return False

  return date