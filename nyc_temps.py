from pylab import plot,show, xlabel,ylabel,title, legend

nyc_temps = {}
x_legend = []
nyc_temps[2000] = [31.3,37.3,47.2,51.0,63.5,71.3,72.3,72.7,66.0,57.0,45.3,31.1]
nyc_temps[2006] = [40.9,35.7,43.1,55.7,63.1,71.0,77.9,75.8,66.6,56.2,51.9,43.6]
nyc_temps[2012] = [37.3,40.9,50.9,54.8,65.1,71.0,78.8,76.7,68.8,58.0,43.9,41.5]

months = range(1,13)
for k in nyc_temps:
    plot(months,nyc_temps[k])
    x_legend.append(k)


title('Average Monthly Temperatures in NYC')
xlabel('Month')
ylabel('Temperature')
legend(x_legend)    
show()