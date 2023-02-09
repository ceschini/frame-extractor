"""frameExtractor

Simple frame extractor using openCV. Extract frames from videos by specifying
seconds, minutes or time interval.

The project could be expanded by a command-line interface with a config file,
but for the time being this is a working version.

Please refer to the README.md file for instructions on how to install and run.
"""

import os
import argparse
import cv2


class frameExtractor:
    def __init__(self, filename, seconds, minutes, interval):
        self.fn = filename
        self.sec = seconds
        self.min = minutes
        self.interval = interval

    def processTime(self, second, minute):
        secs = 0
        if minute:
            secs = int(minute) * 60000
        ms = (int(second) * 1000) + secs
        return ms

    def loadVideo(self, filename):
        if os.path.exists(filename):
            vidcap = cv2.VideoCapture(filename)
            return vidcap
        else:
            return -1

    def extractFrame(self, second, minute):
        ms = self.processTime(second, minute)
        vidcap = self.loadVideo(self.fn)
        vidcap.set(0, ms)

        fname = self.fn.split('.')[0]
        if minute:
            out_name = f'frames/{fname}-{minute}:{second}-frame.png'
        else:
            out_name = f'frames/{fname}-0:{second}-frame.png'
        success, image = vidcap.read()
        if success:
            cv2.imwrite(out_name, image)
            print(f'Frame extracted and saved at {out_name}\n')
            return 0
        else:
            print(f'failed to read {self.fn}')
            return -1

    def extract(self):
        if self.interval:
            start, finish = self.interval.split('-')
            start = int(start)
            finish = int(finish)
            for i in range(start, finish + 1):
                self.extractFrame(i, self.min)
        else:
            self.extractFrame(self.sec, self.min)


class CLIFrameExtractor:
    def __init__(self):
        self.running = True

    def load_file(self):
        self.fn = input("Please enter local filename or full filepath:\n")
        if not os.path.exists(self.fn):
            print('Path unknown')
            return -1

    def cli_run(self):
        mins = input("Please inform frame minutes (default = 0):\n")
        interval_choice = input("Do you like to inform an interval? (y/N):\n")
        if interval_choice == 'y':
            secs = None
            interval = input(
                "Please inform time interval, in seconds (ex: '0-5'):\n")
        else:
            interval = None
            secs = input("Please inform frame seconds:\n")
        fe = frameExtractor(self.fn, secs, mins, interval)
        fe.extract()

    def main(self):
        print("##############################################################")
        print("##                                                          ##")
        print("##  Welcome to the Frame Extractor Command-Line Interface!  ##")
        print("##                                                          ##")
        print("##############################################################\n")
        self.load_file()
        while self.running:
            self.cli_run()
            again = input("Would you like to run it again? (Y/n):\n")
            if again == 'n':
                self.running = False
            else:
                new_f = input("Load new file? (y/N):\n")
                if new_f == 'y':
                    self.load_file()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='FrameExtractor',
        description='Extract frames from video at a specified time',
    )

    parser.add_argument(
        '-f',
        '--filename',
        help='local filename or full filepath'
    )

    parser.add_argument(
        '-s',
        '--seconds',
        help='Exact second for frame extracted'
    )

    parser.add_argument(
        '-m',
        '--minutes',
        help='Exact minute for frame extracted',
        default=0
    )

    parser.add_argument(
        '-i',
        '--interval',
        help='Interval in seconds (ex: 5-6)',
        default=0
    )

    parser.add_argument(
        '-cli',
        help='Start Command Line Interface',
        action='count'
    )

    args = parser.parse_args()
    if args.cli:
        cli = CLIFrameExtractor()
        cli.main()
    else:
        fe = frameExtractor(args.filename, args.seconds,
                            args.minutes, args.interval)
        fe.extract()
