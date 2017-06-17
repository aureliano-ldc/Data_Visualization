import matplotlib.pyplot as plt


# 用 .plot() 函数绘制函数图
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

plt.show()




# 用 .scatter() 函数绘制散点图
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, 
	edgecolor='none', s=40)

"""
We pass the list of y-values to c and then tell pyplot which colormap to
use through the cmap argument. This code colors the points with lower
y-values light blue and the points with larger y-values dark blue

You can see all the colormaps available in pyplot at http://matplotlib.org/; go to
Examples, scroll down to Color Examples, and click colormaps_reference.

"""

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axes.
plt.axis([1, 1100, 0, 1100000])

plt.show()


# plt.savefig('squares_plot.png', bbox_inches='tight')

"""
If you want your program to automatically save the plot to a file, you can
replace the call to plt.show() with a call to plt.savefig():
The first argument is a filename for the plot image, which will be saved
in the same directory as scatter_squares.py. The second argument trims extra
whitespace from the plot. If you want the extra whitespace around the plot,
you can omit this argument.
"""