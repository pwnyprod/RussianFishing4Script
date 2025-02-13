import logging

from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator

from notification_provider.abstract_messaging_method import MessagingMethod
from timer import Timer

logger = logging.getLogger(__name__)
class PlotMethod(MessagingMethod):
    timer: Timer

    def __init__(self, timer: Timer):
        self.timer = timer

    def send_message(self, message: str):
        """Plot and save an image using rhour and ghour list from timer object."""

        cast_rhour_list, cast_ghour_list = self.timer.get_cast_hour_list()
        _, ax = plt.subplots(nrows=1, ncols=2)
        # _.canvas.manager.set_window_title('Record')
        ax[0].set_ylabel("Fish")

        last_rhour = cast_rhour_list[-1]  # hour: 0, 1, 2, 3, 4, "5"
        fish_per_rhour = [0] * (last_rhour + 1)  # idx: #(0, 1, 2, 3, 4, 5) = 6
        for hour in cast_rhour_list:
            fish_per_rhour[hour] += 1
        ax[0].plot(range(last_rhour + 1), fish_per_rhour)
        ax[0].set_title("Fish Caughted per Real Hour")
        ax[0].set_xticks(range(last_rhour + 2))
        ax[0].set_xlabel("Hour (real running time)")
        ax[0].yaxis.set_major_locator(MaxNLocator(integer=True))

        fish_per_ghour = [0] * 24
        for hour in cast_ghour_list:
            fish_per_ghour[hour] += 1
        ax[1].bar(range(0, 24), fish_per_ghour)
        ax[1].set_title("Fish Caughted per Game Hour")
        ax[1].set_xticks(range(0, 24, 2))
        ax[1].set_xlabel("Hour (game time)")
        ax[1].yaxis.set_major_locator(MaxNLocator(integer=True))

        # plt.tight_layout()
        plt.savefig(f"../logs/{self.timer.get_cur_timestamp()}.png")
        print("The Plot has been saved under logs/")
