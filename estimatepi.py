from matplotlib import pyplot as plt 
import random


# here I am creating a figure with a single axis (that is one plot).
fig, ax = plt.subplots(figsize=(5,5)) # default 1 x 1

# generate x and y coordinates here
#number_of_points = 100 
#x = [random.random() for _ in range(number_of_points)]
#y = [random.random() for _ in range(number_of_points)]

circle_x = 0.5;
circle_y = 0.5;
# making the center of the circle
rad = 0.5;
# the radius of the circle 

in_cirlcle = 0
out_circle = 0
total_pts = 0
interval = 100
for i in range(interval):

   x = random.random()
   y = random.random()
# plot the points as a scatter plot here
   ax.scatter(x,y)

 #using the center of the circle and distance to see what is in and what is not 
   if ((x - circle_x) * (x - circle_x) +
        (y - circle_y) * (y - circle_y) <= rad * rad):
       #print ('in')
       in_cirlcle = in_cirlcle + 1
   else:
       #print ('out')
       out_circle = out_circle + 1



# here I am defining a circle of radius 0.5 that is centered at (0.5, 0.5)
my_circle = plt.Circle((0.5,0.5), radius=0.5, fill=False)
# this plots the circle on the graph
ax.add_patch(my_circle)

total_pts = out_circle + in_cirlcle
pointsdiv = in_cirlcle / total_pts
pi_val = pointsdiv * 4
print(pi_val)
print(str(total_pts) + " points in the plot")






# need to write code to only use points within the circle 
# count the points inside and outside the circle 
# code to find what r^2 is 
# pi = (number of points inside the circle / total number of point)/r^2


# display the plot
plt.show()