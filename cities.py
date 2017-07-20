import numpy as np
import matplotlib.pyplot as plt
import sys, itertools
from matplotlib.patches import Rectangle
import time

#### HELPER FUNCTIONS #####
def distance(coord1, coord2):
	"""
	Generic n-dimensional Euclidean distance function.
	"""
	if len(coord1) != len(coord2):
		return 0

	sq_diff = [ (c[0] - c[1])**2 for c in zip(coord1,coord2)]
	return np.sqrt(np.array(sq_diff).sum())

def routeLength(arr):
	"""
	Calculates the distance of list in order, connecting from final element
	to first element.
	"""
	if len(arr) <= 1:
		print("List is too short")
		return 0

	total_distance = 0
	previous_element = arr[-1]

	for element in arr:
		total_distance += distance(previous_element, element)
		previous_element = element

	return total_distance

class grid_2d_cities():
	"""
	Generates random cities in 2D and finds the route with minimum path where 
	each city is exactly visited once and returns to origin city.
	"""

	# For n cities, we search (n-1)! routes.
	maxBruteN = 12
	
	def __init__(self, *args):
		if len(args) == 0:
			print("Must pass at least one integer to constructor. Exiting....")
			sys.exit()

		self.ncities = args[0]
		self.xlength = self.ylength = self.ncities

		if len(args) > 1:
			self.xlength = args[1]

		if len(args) > 2:
			self.ylength = args[2]

		
		self.coords = [] # List to store coordinate pairs
		self.bruteshortest = [] # List to store brute force shortest route
		self.generateCities()

	def generateCities(self):
		"""
		Put n cities on [0, xlength-1] X [0, ylength-1] integer grid
		"""
		if self.ncities > (self.xlength * self.ylength):
			print("The product of xlength and ylength must be greater than ncities.")
			print("Cities won't generate.")
		else:
			for i in range(self.ncities):
				x = int(np.random.uniform(0, self.xlength))
				y = int(np.random.uniform(0, self.ylength))
				
				# We need to make sure every point coordinate is unique
				if (x,y) in self.coords:
					while (x,y) in self.coords:
						x = int(np.random.uniform(0, self.xlength))
						y = int(np.random.uniform(0, self.ylength))

				self.coords.append((x,y))

	def bruteShortest(self):
		"""
		Here we are interested in unique routes, i.e the same path woth a different starting
		point or directionality should not be considered.

		To reduce redundacy, for n cities labelled 0 to n-1, we assume that city 0 be starting
		point. There are many routes, also reversals leads to identical distances.
		"""
		if self.ncities > grid_2d_cities.maxBruteN:
			print("There are too many cities to find a brute force solution.")
			print("n cities = {}, which means {} possible paths.".format(self.ncities, np.math.factorial(self.ncities - 1)))
		else:
			min_distance = -1
			min_distance_indices = []

			# Looping over all permutations of (1, 2,...., ncities-1)
			for perm in itertools.permutations(range(1,self.ncities)):
				# Store indices of each permuatation in list
				indices = [ index for index in perm]
				# Adding start node at last
				indices.append(0)

				# calculating distance of the new route
				new_route = [ self.coords[i] for i in indices ]
				new_distance = routeLength(new_route)

				# check whether new distance < current minimum distance
				if new_distance < min_distance or not min_distance_indices:
					min_distance = new_distance
					min_distance_indices = indices

			self.bruteshortest = [ self.coords[i] for i in min_distance_indices]
			print("Brute force solution has length: {:.3f}".format(min_distance))

	def drawCities(self, route=[]):
		"""
		Draw cities as they appear on the grid. If route is passed, this will
		be drawn as a collection of arrows linking the cities.
		"""

		if not route and self.bruteshortest:
			route = self.bruteshortest

		fig = plt.figure()
		ax = fig.gca()
		ax.set_xticks(np.arange(-1, self.xlength))
		ax.set_yticks(np.arange(-1, self.ylength))

		# Unpack coordinate pairs
		x, y = zip(*self.coords)
		
		# Plot coordinates
		plt.scatter(x[0], y[0], s=30, c='r', marker='D')
		plt.scatter(x[1:], y[1:], marker='o')

		plt.xlim(-0.5, self.xlength-0.5)
		plt.ylim(-0.5, self.ylength-0.5)

		# Add rectangle
		ax.add_patch(Rectangle((0,0), self.xlength-1, self.ylength-1, alpha=0.3, color='gray'))
		plt.grid()

		if route:
			self.addArrows(ax, route)

		plt.show()

	def addArrows(self, ax, route):
		"""
		Add arrows to plot showing the specfied route.
		"""
		# Start with last point
		prev = route[-1]

		for point in route:
			dx, dy = point[0]-prev[0], point[1]-prev[1]
			#scale = 1 - 0.3/np.sqrt(dx**2 + dx**2)
			scale = 0.95
			ax.arrow(prev[0], prev[1], scale*dx, scale*dy, head_width=0.1)

			prev = point



if __name__ == '__main__':
	
	mycities = grid_2d_cities(9, 12, 12)
	print(mycities.coords)
	start = time.time()
	mycities.bruteShortest()
	end = time.time() - start
	print("Time : {:.2f} sec".format(end))
	mycities.drawCities()