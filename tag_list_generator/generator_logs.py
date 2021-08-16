"""Blah blah."""

import logging
import time
import locale
import os
import re
from itertools import zip_longest


def create_logs():
    locale.setlocale(locale.LC_ALL, "")
    timestamp = time.strftime("%x").replace("/", "-")


    def sort_logs(log: str):
        date = log.split()[0].replace("-", "/")
        date = time.strptime(date, "%x")

        sequence = re.split("\s|\.", log)[-2]
        log = (date, sequence)
        return log
    

    directory = "tag_list_generator/logs"
    today_logs = []
    previous_log_exists = False
    count = 0

    if not os.path.exists(directory):
        os.mkdir(directory)
        count = 1
        
    elif os.path.exists(directory) and not os.path.isfile(directory):
        if os.listdir(directory):
            previous_log_exists = True
            existing_logs = os.listdir(directory)
            existing_logs.sort(key=sort_logs)

            for filename in existing_logs:
                if re.search(timestamp, filename):
                    today_logs.append(filename)

            if today_logs:
                today_logs.sort(key=sort_logs)
                previous_log = today_logs[-1]
                previous_log_count = re.split("\s|\.", str(previous_log))[-2]
                count = int(previous_log_count) + 1

            else:
                previous_log = existing_logs[-1]
                count += 1
        else:
            previous_log = ""
            count += 1
    else:
        print("Path is a file.")

    logging.basicConfig(
        filename=f"tag_list_generator/logs/{timestamp} {count}.log",
        filemode="w+", level=logging.INFO
        )

    if previous_log_exists:
        previous_log = f"tag_list_generator/logs/{previous_log}"
    new_log = f"tag_list_generator/logs/{timestamp} {count}.log"
    
    return new_log, previous_log


def cross_reference_logs(new_log, previous_log=""):

    l1 = "Last two log files contain different results. Selected "
    l2 = "localization file may contain unhandled formatting."
    warning_message = (l1 + l2)


    def log_lines(log):
        with open(log) as infile:
            for line in infile:
                if line == f"WARNING:root:{warning_message}\n":
                    break
                else: yield line


    if previous_log == "":
        pass

    else:
        paired_lines = zip_longest(log_lines(new_log),
                                    log_lines(previous_log))
        
        mismatch = False
        for i, (line0, line1) in enumerate(paired_lines):
            if line0 != line1:
                print("Log mismatch at line", i)
                mismatch = True
        
        if mismatch:
            logging.warning(warning_message)