from shapely import wkt

def wkt_loads(string):
  if type(string) != str: return string
  try: return wkt.loads(string)
  except: return string