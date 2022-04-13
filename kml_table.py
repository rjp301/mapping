import os

def format_kml_table(data,**kwargs) -> str:
  fname = os.path.join("kml_table_style.html")
  with open(fname,"r") as file: style = file.read()
  
  html = data.to_html(header=False,na_rep="-",**kwargs)
  desc = style + html
  desc = desc.replace(" 00:00:00","")
  return desc