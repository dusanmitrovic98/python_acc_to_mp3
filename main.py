import os
import subprocess
import sys


def convert_acc_to_mp3(input_folder, output_folder):
    """
    This function converts ACC files to MP3 files in the specified input_folder
    and saves them in the output_folder. Input folder needs to contain only ".acc" files.
