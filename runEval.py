import mainEval
import argparse
from util.LFUtil import *

# args  = [
#     ['--imagesToUse','int', [1]],
#     '--GPUs', 'int', [0],
#     '--datasetPath', "C:/Users/LabOldenbourg/Desktop/BrainImagesJosuePage/brainSubset/brainSubset_1_1.h5",
#     '--outputPath', "eval/runsMouse/",
#     '--checkpointPath', "runs/2020_10_11__14:23:21_TrueB_0.1bias_5I_128BS_FalseSk_9FOV_3nT_0.03ths_a8d9a2c_commit_",
#     '--checkpointFileName', "model_130",
#     '--writeVolsToH5', True,
#     '--writeToTB', True    
# ]

def main():
    # Arguments
    parser = argparse.ArgumentParser()
    # Image indices to use for training and validation
    parser.add_argument('--imagesToUse', nargs='+', type=int, default= [6])
    # GPUs to use
    parser.add_argument('--GPUs', nargs='+', type=int, default=[0])
    # Path to dataset
    parser.add_argument('--datasetPath', nargs='?', default= "C:/Users/LabOldenbourg/Desktop/BrainImagesJosuePage/brainSubset/brainSubset_1_1.h5")
    # Path to directory where models and tensorboard logs are stored
    parser.add_argument('--outputPath', nargs='?', default="eval/runsMouse/")
    # Path to model to use for testing
    parser.add_argument('--checkpointPath', nargs='?', default="runs/2022_04_27__112343_TrueB_0.1bias_5I_32BS_FalseSk_9FOV_3nT_0.03ths_c849549_commit__")
    # File to use
    parser.add_argument('--checkpointFileName', nargs='?', default="model_0")
    # Write volumes to H5 file
    parser.add_argument('--writeVolsToH5', type=str2bool, default=True)
    # Write output to tensorboard
    parser.add_argument('--writeToTB', type=str2bool, default=True)


    argsTest = parser.parse_args()

    # import os, sys
    # currentdir = os.path.dirname(os.path.realpath(__file__))
    # grandparentdir = os.path.dirname(os.path.dirname(currentdir))
    # sys.path.append(grandparentdir)


    mainEval.main(argsTest)



if __name__ == '__main__':
    main()