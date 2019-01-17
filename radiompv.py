#!/usr/bin/env python3

import requests
import subprocess
import argparse

from bs4 import BeautifulSoup

urls = {
    "radio2": ("BBC Radio 2", "https://www.bbc.co.uk/radio2", "http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_two.m3u8"),
    "radio3": ("BBC Radio 3", "https://www.bbc.co.uk/radio3", "http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_three.m3u8"),
    "radio4": ("BBC Radio 4", "https://www.bbc.co.uk/radio4", "http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_fourfm.m3u8"),
    "radio5": ("BBC Radio 5 Live", "https://www.bbc.co.uk/5live", "http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_five_live.m3u8"),
    "radio6": ("BBC Radio 6 Music", "https://www.bbc.co.uk/6music", "http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_6music.m3u8"),
}


def main(station):
    r = requests.get(station[1])
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.title.text
    on_now_cls = soup.find_all("div", class_="on-air__track-now-playing__details")[0].text
    msg = "\033[1;96mCurrent programme: \33[0m"
    print("\033[1;95m" + title + "\33[0m")
    print(" ".join([msg, "\033[1;33m", on_now_cls, "\033[0m"]))
    print("\nCtrl-C to quit\n")
    subprocess.run(["mpv", station[2]])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Stream BBC radio - requires mpv")
    parser.add_argument("station", type=str, nargs=1, help="Name of station: radio2, radio3, radio4, radio5, radio6")
    args = vars(parser.parse_args())
    try:
        main(urls.get(args['station'][0]))
    except TypeError:
        print("Don't recognise that radio station")

