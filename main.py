from launchpad import Launchpad
import mido
import time


def main():
    launch = Launchpad()
    launch.lp_init()
    time.sleep(5)
    launch.close()


main()
