import seaborn as sns
import matplotlib.pyplot as plt

a=sns.load_dataset("tips")
sns.stripplot(x='day',y='total_bill',data=a)
plt.savefig("chart8.png")
plt.show()

sns.swarmplot(x='day',y='total_bill',data=a)
plt.savefig("chart9.png")
plt.show()

sns.histplot(x='total_bill',data=a,kde=True)
plt.savefig('chart10.png')
plt.show()

sns.kdeplot(x='total_bill',fill=True,data=a,hue='sex')
plt.savefig('chart11.png')
plt.show()

sns.displot(x='total_bill',data=a,col='time',hue='sex')
plt.savefig('chart11.png')
plt.show()

sns.regplot(x="total_bill",y='tip',data=a)
plt.savefig('chart12.png')
plt.show()

sns.lmplot(x="total_bill",y='tip',data=a,hue='sex')
plt.savefig('chart13.png')
plt.show()

b=a.corr(numeric_only=True)
sns.heatmap(b,annot=True,cmap='coolwarm')
plt.savefig('chart14.png')
plt.show()

c=sns.load_dataset('iris')
sns.pairplot(c,hue='species')
plt.savefig('chart14.png')
plt.show()

sns.jointplot(x='total_bill',y='tip',data=a,kind='hex')
plt.savefig('chart14.png')
plt.show()

r=sns.FacetGrid(a,col='time',row='sex')
r.map(sns.scatterplot,'total_bill','tip')
sns.set_style('darkgrid')
sns.set_context('talk')
sns.set_palette('pastel')
plt.savefig('chart14.png')
plt.show()

'''
whitegrid - white background with grid
Darkgrid - grey background with grid
darkwhitegrid -
whitegrid
ticksgrid
'''