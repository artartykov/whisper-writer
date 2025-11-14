import os
import sys
import subprocess
import argparse
from dotenv import load_dotenv

parser = argparse.ArgumentParser()
parser.add_argument('--start', action='store_true', help='Start listening immediately')
args = parser.parse_args()

print('Starting WhisperWriter...')
load_dotenv()

cmd = [sys.executable, os.path.join('src', 'main.py')]
if args.start:
    cmd.append('--start')
subprocess.run(cmd)
