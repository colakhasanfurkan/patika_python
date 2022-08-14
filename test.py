import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


x = np.arange(-10,11)

plt.figure(figsize=(12,6))
plt.title("Nice Shit")
plt.plot(x,x**2)
plt.plot(x,-1*(x**2))
