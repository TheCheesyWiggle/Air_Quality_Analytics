import numpy as np
import matplotlib.pyplot as plt

# style of the plot
plt.style.use('dark_background')

#data
pollutants = ['CO', 'NO2', 'O3', 'PM10', 'PM25', 'SO2']
station_1=[60,40,68,94,27,60]
station_2=[81,30,75,37,46,50]


# getting angles
# starts at 0 and goes to 2pi ==360 degrees
angles = np.linspace(0,2*np.pi,len(pollutants), endpoint=False)
angles=np.concatenate((angles,[angles[0]]))
# makes data circular for consistancy when plotting
pollutants.append(pollutants[0])
station_1.append(station_1[0])
station_2.append(station_2[0])
# plotting station 1
fig=plt.figure(figsize=(7,7))
ax=fig.add_subplot(polar=True)
ax.plot(angles, station_1)
ax.plot(angles,station_1, 'o-', color='cyan', label='BG1')
ax.fill(angles, station_1, alpha=0.25, color='cyan')
#plotting station 2
ax.plot(angles, station_2)
ax.plot(angles,station_2, 'o-', color='magenta', label='MY1')
ax.fill(angles, station_2, alpha=0.25, color='magenta')
ax.set_thetagrids(angles * 180/np.pi, pollutants)#type: ignore
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()