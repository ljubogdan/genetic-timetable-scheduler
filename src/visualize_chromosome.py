import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
from matplotlib.gridspec import GridSpec
from constants import NUMBER_OF_DAYS, NUMBER_OF_CLASSROOMS

def visualize_best_chromosome(chromosome):
    days = ["Ponedeljak", "Utorak", "Sreda", "Četvrtak", "Petak"]
    number_of_classrooms = NUMBER_OF_CLASSROOMS
    number_of_days = NUMBER_OF_DAYS

    #fig, ax = plt.subplots(figsize=(10,6))

    fig = plt.figure(figsize=(16, 8))
    gs = GridSpec(nrows=2, ncols=1, height_ratios=[10, 1], figure=fig)

    ax = fig.add_subplot(gs[0])
    legend_ax = fig.add_subplot(gs[1])
    legend_ax.axis('off')

    # mapping lectures on colors
    lectures = sorted({item[0] for classroom in chromosome for item in classroom if isinstance(item, tuple)})
    cmap = plt.cm.get_cmap('tab20', len(lectures))
    color_map = {lecture: cmap(i) for i, lecture in enumerate(lectures)}

    for index, classroom in enumerate(chromosome):
        day = index // number_of_classrooms
        classroom_index = index % number_of_classrooms
        y = (number_of_days - day - 1) * number_of_classrooms + classroom_index
        x = 0

        for item in classroom:
            if isinstance(item, tuple):
                lecture, duration = item
                color = color_map[lecture]
                ax.add_patch(patches.Rectangle((x, y), duration, 0.8, edgecolor='black', facecolor=color))
                x += duration
            elif isinstance(item, int):
                ax.add_patch(patches.Rectangle((x, y), item, 0.8, edgecolor='gray', facecolor='lightgray'))
                if item >= 15:
                    ax.text(x + item / 2, y + 0.4, f"Pauza\n{item}min", ha='center', va='center', fontsize=6)
                x += item

    # Y axis - days and classrooms
    yticks = []
    yticklabels = []
    for day in range(number_of_days):
        for classroom in range(number_of_classrooms):
            yticks.append((number_of_days - day - 1) * number_of_classrooms + classroom)
            yticklabels.append(f"{days[day]} - Učionica {classroom + 1}")

    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklabels)
    ax.set_xlabel("Vreme (u minutama)")
    ax.set_title("Optimalni raspored predavanja")

    # legend
    handles = [patches.Patch(color=color_map[naziv], label=naziv) for naziv in lectures]
    #ax.legend(handles=handles, loc='upper center', bbox_to_anchor=(0.5, -0.08), ncol=6, fontsize=7, title="Predavanja")
    legend_ax.legend(handles=handles, loc='center', ncol=6, fontsize=7, title="Predavanja")

    ax.set_xlim(0, 1000)
    ax.set_ylim(-1, len(chromosome) + 1)
    plt.tight_layout()
    plt.show()
    