import FinalRNGen as rng
from tqdm import tqdm

rand_vals_list=rng.ProduceRandomNumsList(low=0, high=20, size=50000000)
x=rand_vals_list[:len(rand_vals_list)//2]
y=rand_vals_list[len(rand_vals_list)//2:]

coordinate_count=len(x)

# we will now see if our x,y values lie within a quater of a circle

counter=0
for i in tqdm(range(coordinate_count)):
    square_sum=(x[i]**2)+(y[i]**2)
    if(square_sum<=20**2):
        counter+=1

pi=(4*counter)/coordinate_count

print(pi)