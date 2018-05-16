from correlate import find_corr_x_y
import matplotlib.pyplot as plt
import csv


def scatter_plot(x,y):
	plt.scatter(x,y)
	plt.xlabel('Number')
	plt.ylabel('Square')
	plt.show()

def read_csv(filename):
	with open(filename) as f:
		reader = csv.reader(f)
		next(reader)
		
		homelessness = []
		highest_corr = []
		for row in reader:
			try:
				homelessness.append(float(row[1]))
				highest_corr.append(float(row[2]))
			except IndexError:
				pass
	return homelessness,highest_corr
	
if __name__	== '__main__':
	homelessness, highest_corr = read_csv('correlate-HOMELESSNESS.csv')
	corr = find_corr_x_y(homelessness, highest_corr)
	print('Highest Correlation: {0}'.format(corr))
	scatter_plot(homelessness,highest_corr)
