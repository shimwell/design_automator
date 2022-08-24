import matplotlib.pyplot as plt
import pandas as pd
from design_automator import requirements


df = pd.read_json('design_successful.json')

iterations = list(range(len(df)))


for key in ['weight_of_vessel', 'tritium_breeding_ratio', 'radius_of_vessel']:
    key_with_spaces = key.replace('_', ' ')
    plt.cla()
    plt.plot(iterations, df[key].values, label='achieved')
    plt.title(f'Improvement of {key_with_spaces} with design iterations')
    plt.xlabel('iteration')
    plt.ylabel(key_with_spaces)

    for requirement in requirements[key]:
        operator = requirement[0]
        truth_val = requirement[1]
        plt.plot(iterations, [truth_val]*len(iterations), ':',label=f'requirement {operator.__name__}', color='black')
    plt.legend()

    plt.savefig(f'improvement_{key}.png')
    plt.close()
