import os

def write_prj_file(fname:str,EPSG:int=26910):
  import urllib
  
  fname = os.path.splitext(fname)[0] + ".prj"
  url = f"http://spatialreference.org/ref/epsg/{str(EPSG)}/prettywkt/"
  
  with urllib.request.urlopen(url) as request:
    wkt = (request.read().decode("UTF-8")
      .replace(" ","").replace("\n", "")
      .encode("UTF-8"))

  with open(fname,"wb") as prj:
    prj.write(wkt)