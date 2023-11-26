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
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        print(filename)
        
        acc_path = os.path.join(input_folder, filename)

        # Extract the name without extension
        file_name_without_extension = os.path.splitext(filename)[0]

        # Construct the output path with the same name but with .mp3 extension
        mp3_path = os.path.join(output_folder, f"{file_name_without_extension}.mp3")

        print(f"Converting: {acc_path} to {mp3_path}")

        try:
