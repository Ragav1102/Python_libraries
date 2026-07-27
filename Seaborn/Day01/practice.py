import seaborn as sns
import matplotlib.pyplot as plt

a=sns.load_dataset('tips')

print(a.head())

sns.scatterplot(x='total_bill', y='tip', data=a,hue='sex',size='size')
plt.title('Scatter plot of Total Bill vs Tip')
plt.savefig("chart1.png")
plt.show()


a=sns.load_dataset('flights')
sns.lineplot(x='year', y='passengers', data=a)
plt.title('Line plot of Year vs Passengers')
plt.savefig("chart2.png")
plt.show()

b=sns.load_dataset('tips')
print(b.head())
sns.relplot(x='total_bill', y='tip', data=b, hue='smoker')
plt.savefig("chart3.png")
plt.show()

sns.barplot(x='day', y='total_bill', data=b, hue='sex',errorbar=None)
plt.savefig("chart4.png")
plt.show()

sns.countplot(x='day',data=b,hue='sex')
plt.savefig("chart5.png")
plt.show()

sns.boxplot(x='day',y='total_bill',data=b,hue='smoker')
plt.savefig("chart6.png")
plt.show()

sns.violinplot(x='day',y='total_bill', data=b,hue='sex',split=True)
plt.savefig('chart7.png')
plt.show()