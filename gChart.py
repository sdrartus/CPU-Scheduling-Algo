import matplotlib.pyplot as plt
import numpy as np


# x legends, max X lim, y data, y legends
def chart(xLegends, xMaxLim, yData, yLegends, algo):
    # fig = plt.figure(figsize = (10, 5))
    # plt.xlabel("Duration")
    # plt.ylabel("Processes")
    # plt.title("Gantt Chart for CPU Scheduling")
    x = list(xLegends)
    y = list(yData)
    # plt.bar(x,y, color ='maroon', width = 0.4)
    # plt.grid(True)
    #

    # fig, gnt = plt.subplots()
    # gnt.set_ylim(0, yLegends)
    # gnt.set_xlim(0, xMaxLim)
    # gnt.set_xlabel('Duration (ms)')
    # gnt.set_ylabel('Processes')
    #
    # gnt.set_yticklabels(yData)
    # gnt.broken_barh([(xLegends[0],xLegends)],
    #                 (20, 9),
    #                 facecolors =('tab:red'))
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.barh(x, y)
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)

    ax.grid(b=True, color='grey',
            linestyle='-.', linewidth=0.5,
            alpha=0.2)

    ax.invert_yaxis()

    for i in ax.patches:
        plt.text(i.get_width() + 0.2, i.get_y() + 0.5,
                 str(round((i.get_width()), 2)),
                 fontsize=10, fontweight='bold',
                 color='grey')

    # Add Plot Title
    ax.set_title(f'Gantt Chart for CPU Scheduling Algorithm for {format(algo)}',
                 loc='center', )

    plt.show()
