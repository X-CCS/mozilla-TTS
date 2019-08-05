import librosa
import argparse
import os
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count

workers = cpu_count()
print("Using {} workers".format(workers))
executor = ProcessPoolExecutor(max_workers=cpu_count())

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
    help="path to input folder of images")
ap.add_argument("-o", "--output", required=True,
    help="path to output folder of images")
ap.add_argument("-r", "--rate", required=True, type=int,
    help="output sample rate")
args = vars(ap.parse_args())

INPUT_FOLDER = args["input"]
OUTPUT_FOLDER = args["output"]
RATE = int(args["rate"])
print("Changing sample rate to", RATE, "Hz")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

file_list = os.listdir(INPUT_FOLDER)

def task(file):
    print(file)
    dir = os.path.join(INPUT_FOLDER, file)
    try:
        y, s = librosa.load(dir, sr=RATE)
    except:
        print("Skipped..")
        return
    librosa.output.write_wav(os.path.join(OUTPUT_FOLDER, file), y, s)

for file in file_list:
    executor.submit(task(file))

executor.shutdown()
print("DONE")
