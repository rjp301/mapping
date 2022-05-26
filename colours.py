import math
import numpy as np

def percent_exaggeration(p,n=4):
  assert p <= 1 and p >= 0, "p must be between 0 and 1"
  for _ in range(n):
    p = math.log2(p+1)
  return p

def colour_scale(c1,c2,num_col=2):
  colours = np.linspace(c1,c2,num_col)
  colours = [[int(i) for i in j] for j in colours]
  return colours

def colour_interp(c1:list, c2:list, v1:float, v2:float, v:float):
  if v1 == v2: return c1
  return [int(c1[i] + (v - v1) * (c2[i] - c1[i]) / (v2 - v1)) for i in range(3)]

def colour_rainbow(length):
  frequency = 0.8
  p1,p2,p3 = 0,2,4
  width = 127
  center = 128

  red = [math.sin(frequency*i + p1)*width + center for i in range(length)]
  grn = [math.sin(frequency*i + p2)*width + center for i in range(length)]
  blu = [math.sin(frequency*i + p3)*width + center for i in range(length)]

  return [(r,g,b) for r,g,b in zip(red,grn,blu)]