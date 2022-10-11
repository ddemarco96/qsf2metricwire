# QSF to MetricWire Conversion
This little snippet is meant to help teams migrating from Qualtrics to MetricWire (specifically, Catalyst). 
It takes a QSF file that can be exported from Qualtrics, which documents the structure and features of a survey. 
After running, your CSV will be sitting in the /converted directory and can be uploaded directly 
to MetricWire.

I am not affiliated with either platform and the code is provided as is with no guarantees of any kind. *Use at your own 
risk*, but like I also don't see how anything worse than mild confusion could result from it not working.

## Instructions
Use conda or an environment manager of your choice to download everything specified in `requirements.txt`.
Primarily, these are: Python, BeautifulSoup, and Pandas. 

You can run the converter with the command `python convert.py /path/to/[your_file].qsf`. I recommend storing the qsf 
files in `/original`. Your output file should appear in `/converted`.

## Notes

This code currently only supports conversions of Qualtrics single choice, text-entry, and text info 
data types.

Be sure to review your question content, choices, and anchors when you've uploaded the file to Catalyst. BeautifulSoup 
handles most of the HTML that may have existed in the Qualtrics survey, but it does replace newlines with `NBSP` chars.