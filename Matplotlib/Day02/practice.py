import matplotlib.pyplot as plt
import numpy as np

x=[1, 2, 3, 4, 5]
y1=[2, 3, 5, 7, 11]
y2=[1, 4, 6, 8, 10]

figure, ax=plt.subplots(2,2,figsize=(8,6))
ax[0,0].plot(x,y1)
ax[0,0].set_title("Top Left")
ax[0,1].scatter(x,y1)
ax[0,1].set_title("Top Right")
ax[1,0].bar(x,y2)
ax[1,0].set_title("Bottom Left")
ax[1,1].hist(x,y2)
ax[1,1].set_title("Bottom Right")
plt.tight_layout()
plt.savefig("chart7.png")
plt.show()


subjects=["Maths","Science","English","History"]
scores=[90,80,70,60]

colors=['blue','green','red','orange']
plt.bar(subjects,scores, color=colors)
plt.title("Bar Graph")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.savefig("chart8.png")
plt.show()  

x={
    "Days": [1, 2, 3, 4, 5],
    "Sales": [200, 300, 500, 700, 1100]
}
category={
    "Days": [1, 2, 3, 4, 5],
    "Sales": [150, 250, 400, 600, 900]
}

x=np.arange(len(category["Days"]))
width=0.35
plt.bar(x-width/2, category["Sales"], width, label="Category A", color='blue') 
plt.bar(x+width/2, category["Sales"], width, label="Category B", color='green')
plt.legend()
plt.title("Bar Graph")
plt.xlabel("Days")  
plt.ylabel("Sales")
plt.savefig("chart9.png")
plt.show()


student_a = {
    "hours": [1, 2, 3, 4, 5],
    "marks": [10, 20, 30, 40, 50]
}
student_b = {
    "hours": [1, 2, 3, 4, 5],
    "marks": [15, 25, 35, 45, 55]
}
x = np.arange(len(student_a["hours"]))
width = 0.35

# Plot bars
plt.bar(x - width/2, student_a["marks"], width=width, color="blue", label="Student A")
plt.bar(x + width/2, student_b["marks"], width=width, color="green", label="Student B")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.title("Comparison of Student Marks")
plt.legend()
plt.savefig("chart10.png")
plt.show()


