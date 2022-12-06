#!/usr/bin/env python3

from subprocess import run
from datetime import datetime
from time import sleep
import argparse
from os.path import exists


class PlayTime:
    def __init__(self, play_file, play_limit):
        self.date_format = '%d-%m-%Y'
        self.today = datetime.today().date().strftime(self.date_format)
        self.times_play = 0
        self.play_file = play_file
        self.play_limit = play_limit

    def read_play_time(self) -> None:
        if exists(self.play_file):
            with open(self.play_file, 'r') as kid_fd:
                text = kid_fd.readlines()
            if text:
                date, counter = text[-1].split(':')
                date_str = datetime.strptime(date, self.date_format).strftime(self.date_format)
                if date_str == self.today:
                    self.times_play = int(counter.strip())

    def write_play_time(self) -> None:
        self.read_play_time()
        with open(self.play_file, 'a') as kid_fd:
            kid_fd.write(f"{self.today}: {self.times_play + 1}\n")
            self.shutdown_computer()

    def stop_playing(self) -> None:
        self.read_play_time()
        if self.times_play >= self.play_limit:
            self.shutdown_computer()
            exit(0)

    def run(self):
        while True:
            self.stop_playing()
            # Sleep 35 minutes
            sleep(60 * 35)
            self.write_play_time()

    @staticmethod
    def shutdown_computer():
        run(['bash', '-c', 'shutdown', 'now'])


if __name__ == '__main__':

    play_parser = argparse.ArgumentParser('Setup playtime for your child')

    play_parser.add_argument('--play_time',
                             default=2,
                             type=int,
                             required=False,
                             help='X number of times you want your child to play (35 minutes each time)')
    play_parser.add_argument('PLAY_TIME_FILE',
                             type=str,
                             help='Path to file plus desired filename, i.e. /tmp/my_kids_name.txt')

    play_args = play_parser.parse_args()

    play = PlayTime(play_args.PLAY_TIME_FILE, play_args.play_time)
    play.run()
