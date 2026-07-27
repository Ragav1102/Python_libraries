import numpy as np
import matplotlib.pyplot as plt

x=np.random.rand(50)
y=np.random.rand(50)
colors=np.random.rand(50)
sizes=np.random.randint(20,200,50)
plt.scatter(x,y,c=colors,s=sizes,alpha=0.5)
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.savefig("chart11.png")
plt.show()

labels=["Rent","Food","Transport","Entertainment","Savings"]
Expences=[20,30,15,10,25]

plt.pie(Expences,labels=labels,autopct="%1.1f%%",startangle=90,colors=["blue","Red","Green","Yellow","pink"])
plt.savefig("chart12.png")
plt.show()

print (plt.style.available)