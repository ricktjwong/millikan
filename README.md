# millikan
-- Originally for the purpose of automating Imperial College London's Year 2 Physics Lab Experiment --

Recognising charged oil drops in Millikan's oil drop experiment

Millikan's oil drop experiment involves the measurement of several terminal velocities of oil droplets at various conditions to be able to eventually deduce its charge. One would usually look through the microscope, keeping track of one oil droplet at a time, and record its velocity from observation the change in position over time.

This is time consuming and medieval, and these python scripts were written to:

1. Recognise the oil droplets through the microscope
2. Calculate velocities of oil droplets through the microscope

These were done using trackpy: https://github.com/soft-matter/trackpy, a Python implementation of the Crocker-Grier algorithm which helps with particle tracking across frames

To get started - clone the repo: git clone https://github.com/ricktjwong/millikan.git. Download Python v3.6 and install trackpy and it's dependencies.

The first file to run will be Python/extract.py, which reads the sample MOV file from test_video, recognises the oil droplets and tracks them, and extracts the important data into a csv as csv/extract.csv. This might take a while as processing is done on most frames in the video.

After that is done, run Python/transform.csv, which filters the oil droplets which did not change direction upon the removal of electric field, and calculates useful fields such as velocity and saves it into a csv as csv/transform.csv.
