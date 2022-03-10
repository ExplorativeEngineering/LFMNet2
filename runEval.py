args  = [
    "radiometry_frame.png",
    "--radiometry-frame",
    "radiometry_frame.png",
    "--dark-frame",
    "dark_frame.tif",
    "--pixel-size",
    "4.55",
    "--pitch",
    "125",
    "--focal-length",
    "2433",
    "--magnification",
    "20",
    "--na",
    "0.5",
    "--tubelens-focal-length",
    "180.0",
    "--wavelength",
    "510",
    "--medium-index",
    "1.33",
    "--num-slices",
    "5",
    "--um-per-slice",
    "5.0",
    "--supersample",
    "4",
    "-o",
    "calibration.lfc",
    # "--use-single-precision",
]

# import os, sys
# currentdir = os.path.dirname(os.path.realpath(__file__))
# grandparentdir = os.path.dirname(os.path.dirname(currentdir))
# sys.path.append(grandparentdir)

from mainEval import main

main(args)