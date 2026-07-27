import matplotlib.pyplot as plt
import pandas as pd

x=[1, 2, 3, 4, 5]
y=[2, 3, 5, 7, 11]
plt.plot(x,y)
plt.savefig("chart1.png")
plt.show()

a={
    "Days": [1, 2, 3, 4, 5],
    "Sales": [200, 300, 500, 700, 1100]
}

df=pd.DataFrame(a)
plt.plot(df["Days"], df["Sales"])
plt.savefig("chart2.png")
plt.show()

x=[22, 44, 55, 66, 77]
y=[3000,200, 300, 400, 500]

plt.plot(x,y,color='blue', marker='o', linestyle='--', linewidth=2, markersize=10)
plt.savefig("chart3.png")
plt.show()

plt.plot(x,y,"bo--")
plt.savefig("chart4.png")
plt.show()

'''
blue - b
green - g
red - r
black - k
yellow - y
cyan - c
magenta - m 
circle marker - o
square marker - s
triangle marker - ^
star marker - *
x marker - x
diamond marker - D
line style -
solid line - -
dashed line - --
dotted line - :
dash-dot line - -.
'''

x=[1, 2, 3, 4, 5]  
y1=[2, 3, 5, 7, 11] 
y2=[1, 4, 6, 8, 10]
plt.plot(x,y1,"ro--",label="y1",color='blue',marker='o',linestyle='--',linewidth=2,markersize=10)  
plt.plot(x,y2,"go--",label="y2",color='green',marker='s',linestyle='--',linewidth=4,markersize=10)
plt.xlabel("Months")
plt.ylabel("Items Sold")
plt.legend()
plt.grid(True)
plt.savefig("chart5.png")
plt.show()

x=[1, 2, 3, 4, 5]
y1=[2, 3, 5, 7, 11]
y2=[1, 4, 6, 8, 10]
fig, ax = plt.subplots(1,2,figsize=(10,5))
ax[0].plot(x,y1,color='blue',label="y1")        
ax[0].set_title("Graph 1")
ax[1].plot(x,y2,color='green',label="y2")       
ax[1].set_title("Graph 2")
plt.savefig("chart6.png")
plt.show()

