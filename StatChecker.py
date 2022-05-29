import FinalRNGen as rng
import matplotlib.pyplot as plt

random_nums_list=rng.ProduceRandomNumsList()

plt.hist(random_nums_list, bins=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(0, 20)
plt.show()