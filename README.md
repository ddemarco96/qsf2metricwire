# QSF to MetricWire Conversion
This little snippet is meant to help teams migrating from Qualtrics to MetricWire (specifically, Catalyst). 
It takes a QSF file that can be exported from Qualtrics, which documents the structure and features of a survey. 
After running, a file called `converted_qsf.csv` will be sitting in the same directory and can be uploaded directly 
to MetricWire.

I am not affiliated with either platform and the code is provided as is with no guarantees of any kind. *Use at your own 
risk*, but like I also don't see how anything worse than mild confusion could result from it not working.

## Instructions
Use conda or an environment manager of your choice to download everything specified in `requirements.txt`.
Primarily, these are: Python, BeautifulSoup, and Pandas. 

You can run the converter with the command `python convert.py /path/to/[your_file].qsf`. Your output file should appear 
in the same directory as `converted_qsf.csv`. 

## Notes

This code currently only supports conversions of Qualtrics single choice, text-entry, and text info 
data types.