import matplotlib.pyplot as plt
import numpy as np


labels = ['bt.C', 'cg.C', 'ft.C', 'lu.C', 'mg.D','sp.C','ua.C']
Docker = [20, 34, 30, 35, 27]
Singularity = [25, 32, 34, 20, 25]
#Podman = [

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Docker, width, label='Men')
rects2 = ax.bar(x + width/2, Singularity, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()
