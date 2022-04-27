import mainTrain
import argparse
from util.LFUtil import *

# args  = [
#     '--epochs', 50 ,
#     '--valEvery', 0.25,
#     '--imagesToUse', [ 0, 1, 2, 3, 4, 5],
#     '--batchSize', 16,
#     '--validationSplit', 0.1 ,
#     '--biasVal', 0.1,
#     '--learningRate', 0.005,
#     '--useBias', True ,
#     '--useSkipCon', False,
#     '--fovInput', 9,
#     '--neighShape', 3 ,
#     '--useShallowUnet', True,
#     '--ths', 0.03 ,
#     '--datasetPath', "C:/Users/LabOldenbourg/Desktop/BrainImagesJosuePage/brainSubset/brainSubset_1_1.h5",
#     '--outputPath', "runs/" ,
#     '--outputPrefix', ""
# ]
def main():
    # Arguments
    parser = argparse.ArgumentParser()
    # Number of epochs
    parser.add_argument('--epochs', type=int, default=100)  # can be 1000
    # Validate every n percentage of the data
    parser.add_argument('--valEvery', type=float, default=0.25)
    # Image indices to use for training and validation
    parser.add_argument('--imagesToUse', nargs='+', type=int, default=list(range(0,5,1)))
    # List of GPUs to use: 0 1 2 for example
    parser.add_argument('--GPUs', nargs='+', type=int, default=[0])
    # Batch size
    parser.add_argument('--batchSize', type=int, default=32)  # 128
    # Perentage of the data to use for validation, from 0 to 1
    parser.add_argument('--validationSplit', type=float, default=0.1)
    # Bias initialization value
    parser.add_argument('--biasVal', type=float, default=0.1)
    # Learning rate
    parser.add_argument('--learningRate', type=float, default=0.002) # 0.001
    # Use bias flag
    parser.add_argument('--useBias', type=str2bool, default=True)
    # Use skip connections flag
    parser.add_argument('--useSkipCon', type=str2bool, default=False)
    # User selected random seed
    parser.add_argument('--randomSeed', type=int, default=None) 
    # fov of input or neighboarhood around lenslet to reconstruct
    parser.add_argument('--fovInput', type=int, default=9)
    # nT number of lenslets to reconstruct simultaneously use at training time
    parser.add_argument('--neighShape', type=int, default=3)
    # Flag to use shallow or large U-net
    parser.add_argument('--useShallowUnet', type=str2bool, default=True)
    # Lower threshold of GT stacks, to get rid of autofluorescence
    parser.add_argument('--ths', type=float, default=0.03)
    # Path to dataset
    parser.add_argument('--datasetPath', nargs='?', default= "C:/Users/LabOldenbourg/Desktop/BrainImagesJosuePage/brainSubset/brainSubset_1_1.h5")
    # Path to directory where models and tensorboard logs are stored
    parser.add_argument('--outputPath', nargs='?', default="runs/")
    # Prefix for current output folder
    parser.add_argument('--outputPrefix', nargs='?', default="")
    # Path to model in case of continuing a training
    parser.add_argument('--checkpointPath', nargs='?', default=None)

    args = parser.parse_args()
    # import os, sys
    # currentdir = os.path.dirname(os.path.realpath(__file__))
    # grandparentdir = os.path.dirname(os.path.dirname(currentdir))
    # sys.path.append(grandparentdir)

    mainTrain.main(args)


if __name__ == '__main__':
    main()
    