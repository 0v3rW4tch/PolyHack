import BannerInfo
import argparse


if __name__ == "__main__":
    banner = BannerInfo.BannerInfo()
    banner.welcome_banner()

    while True:
        user_cmd = input('>PolyHack  ')
        if user_cmd == 'ssh':
            pass



