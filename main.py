import os
import subprocess
import sys


def convert_acc_to_mp3(input_folder, output_folder):
    """
    This function converts ACC files to MP3 files in the specified input_folder
    and saves them in the output_folder. Input folder needs to contain only ".acc" files.

    Args:
        input_folder (str): The path to the folder containing ACC files.
        output_folder (str): The path to the folder where the converted MP3 files will be saved.
    """
