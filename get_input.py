#!/usr/bin/python3
import argparse
import subprocess
import sys
import requests

# Usage: ./get_input.py > 1.in
# You must fill in SESSION following the instructions below.
# DO NOT run this in a loop, just once.

# You can find SESSION by using Chrome tools:
# 1) Go to https://adventofcode.com/2022/day/1/input
# 2) right-click -> inspect -> click the "Application" tab.
# 3) Refresh
# 5) Click https://adventofcode.com under "Cookies"
# 6) Grab the value for session. Fill it in.
SESSION = "53616c7465645f5f36664b9d90ebc978c55111798003eeffe810febc176f18c8a7847d4a3836ce269fc3bcf53fbf0aaace5966ac0bb1e70584a173afe6220a07"

useragent = "https://github.com/kitmacleod/advent-of-code/blob/master/get_input.py by kitmacleod@gmail.com"
parser = argparse.ArgumentParser(description="Read input")
parser.add_argument("--year", type=int, default=2023)
parser.add_argument("--day", type=int, default=1)
args = parser.parse_args()

cmd = f"curl https://adventofcode.com/{args.year}/day/{args.day}/input --cookie \"session={SESSION}\" -A '{useragent}'"
output = subprocess.check_output(cmd, shell=True)
output = output.decode("utf-8")
print(output, end="")
print("\n".join(output.split("\n")[:10]), file=sys.stderr)
