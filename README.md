# millikan
-- Originally for the purpose of automating Imperial College London's Year 2 Physics Lab Experiment --

Recognising charged oil drops in Millikan's oil drop experiment

Millikan's oil drop experiment involves the measurement of several terminal velocities of oil droplets at various conditions to be able to eventually deduce its charge. One would usually look through the microsoft, keeping track of one oil droplet at a time, and record its velocity from observation the change in position over time.

This is time consuming and medieval, and these python scripts were written to:

1. Recognise the oil droplets through the microscope
2. Calculate velocities of oil droplets through the microscope

These were done using trackpy: https://github.com/soft-matter/trackpy, a Python implementation of the Crocker-Grier algorithm which helps with particle tracking across frames
