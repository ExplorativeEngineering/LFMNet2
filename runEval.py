args  = [
    '--imagesToUse', 1,
    '--GPUs', 0,
    '--datasetPath', "BrainLFMConfocalDataset/Brain_40x_64Depths_362imgs.h5",
    '--outputPath', "eval/runsMouse/",
    '--checkpointPath', "runs/2020_10_11__14:23:21_TrueB_0.1bias_5I_128BS_FalseSk_9FOV_3nT_0.03ths_a8d9a2c_commit_",
    '--checkpointFileName', "model_130",
    '--writeVolsToH5', True,
    '--writeToTB', True    
]

# import os, sys
# currentdir = os.path.dirname(os.path.realpath(__file__))
# grandparentdir = os.path.dirname(os.path.dirname(currentdir))
# sys.path.append(grandparentdir)

from mainEval import main

main(args)