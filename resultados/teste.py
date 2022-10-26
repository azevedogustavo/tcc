from cmath import sin
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st


def average(num):
    Sum = sum(num)
    print(Sum)
    Average = Sum/len(num)
    print(Average)
    return Average

# colocar uma função que junta listas e faça uma lista de listas
# e retorne uma lista com a média de todas as listas e uma outra lista com os erros 
docker_btC= [142.06, 140.86, 145.64, 141.42, 141.14, 141.40, 146.31, 140.33, 141.17, 140.34, 140.33, 141.03, 141.89, 140.76, 146.44, 144.09, 144.49, 140.01, 141.23, 146.44, 142.54, 141.98, 145.45, 141.81, 146.43, 141.23, 146.89, 140.61, 142.27, 145.25, 146.17]
docker_cdc= [47.36, 45.90, 46.61, 46.45, 46.59, 45.79]

singularity_btC=[146.33, 141.98, 142.87, 141.54, 145.43, 142.05]
singularity_cgc=[45.59, 45.56, 45.50, 45.70, 45.48, 45.67]

saida = st.t.interval(alpha=0.90, df=len(docker_btC)-1, loc=np.mean(docker_btC), scale=st.sem(docker_btC))
saida2 = st.t.interval(alpha=0.99, df=len(singularity_cgc)-1, loc=np.mean(singularity_cgc), scale=st.sem(singularity_btC))
print("docker",saida)
print("singularity",saida2)



m_docker_btC=average(docker_btC)
m_singularity_btc=average(singularity_btC)


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 20, 20, 20, 21]
women_means = [25, 32, 34, 20, 25]
men_std = [2, 3, 4, 1, 2]
women_std = [3, 5, 2, 3, 3]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

# # print(st(men_means))

# # fig, ax = plt.subplots()
# # rects1 = ax.bar(x - width/2, men_means, width, yerr=sem(men_means), label='Docker')
# # rects2 = ax.bar(x + width/2, women_means, width, yerr=women_std, label='Singularity')
# # #rects3 = ax.bar(x + width)

# # # Add some text for labels, title and custom x-axis tick labels, etc.
# # ax.set_ylabel('Scores')
# # ax.set_title('Scores by group and gender')
# # ax.set_xticks(x, labels)
# # ax.legend()

# # ax.bar_label(rects1, padding=3)
# # ax.bar_label(rects2, padding=3)

# # fig.tight_layout()

# # plt.show()