import FinalRNGen as rng
import matplotlib.pyplot as plt

random_nums_list=rng.ProduceRandomNumsList(low=-20,high=30)

plt.hist(random_nums_list, bins=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(-25, 35)
plt.show()