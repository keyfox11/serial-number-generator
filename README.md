# serial-number-generator

> Aug 15 2023
>
> This script is used to quickly generate a large number of G-Code files for engraving serial numbers.  
> The files currently provided in data/ should be used only as an example and for script testing since they are derived from a project I'm currently working on and **WILL NOT WORK** in your machine!

## What does this do?

serial-number-generator is a utility I threw together to quickly generate serialized engraving programs for a large number of parts. Previously, this was done one-at-a-time in SolidWorks by changing a sketch, rebuilding the model, regenerating the toolpaths in HSMWorks and re-posting to a new file.

This ended up taking a lot of time and was prone to errors so that's where this script comes in. A bit of manual work up front ends up saving a ton of time and effort down the road.

## How to use it

Running serial-number-generator.py will prompt you to enter a beginning and ending serial number.  
The current working range is 0 to 99,999.  
After entering a correct range of numbers, it will grab pieces of code from data/ and stitch together individual files, placing them in NC Programs/
