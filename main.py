# Line Charts
# import matplotlib.pyplot as plt
# decades = ["1970", "1980", "1990", "2000","2010"]
# average_price = [26.60, 76.40, 149.80, 207.00, 272.90]
# plt.plot(decades,average_price, color = "#F16059")
# plt.xlabel("Decade", fontsize=16)
# plt.ylabel("Home Price in Thousands", fontsize=16)
# plt.title("Average New Home Price in the U.S.")
# plt.savefig("home_cost.png")

# Bar Charts
import matplotlib.pyplot as plt
cities=["Seattle", "Chicago", "Miami", "New York"]
average_price = [430, 215,255,410]
plt.bar(cities,average_price,color="#48d1cc")
plt.xlabel("Major Cities")
plt.ylabel("Home Price in Thousands")
plt.title("Average Home Price in Major Cities")
plt.savefig("home_price_cities.png")

# Histograms
import matplotlib.pyplot as plt
singles_release_year = [2012,2012,2012,2012,2014,2015,2015,2019,2019]
bins=10
plt.hist(singles_release_year,bins, histtype="bar", color="#fffacd")
plt.xlabel("Release Year")
plt.ylabel("Number of Singles")
plt.title("Madonna Singles Released from 2010-2019")
plt.xticks(range(2010,2020,1))
plt.yticks(range(0,5,1))
plt.savefig("madonna_singles.png")

# Scatter Plots
import matplotlib.pyplot as plt
phases_moon = ["new moon", "first quarter", "full moon","last quarter"]
high_tide_height = [5.5, 5.3, 6.0, 4.8]
plt.scatter(phases_moon, high_tide_height, color="#7b68ee")
plt.xlabel("Moon Phases")
plt.ylabel("Average High Tide Height (feet)")
plt.title("Moon phases and High Tides")
plt.savefig("moon_high_tides.png")
