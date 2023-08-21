# Requirements for acronym tool
This file describes in high level what the tool needs to accomplish

## File management
- The tool shall analyze all files below the source address
- The tool shall be able to analyze microsoft office formats (.xls, .doc, .ppt)
- The tool shall not change the analyzed files

## Acronym dictionary
- The tool shall have a dictionary of previously identified acronyms
- The tool shall have a dictionary of previously identified false positives
- The tool shall suggest new additions to the dictionaries when applicable

## Acronyms management
- The tool shall look for all acronyms identified in its dicitionary
- The tool shall look for acronyms with between 2 and 4 letters (inclusive)
- The tool shall look for acronyms with at least 2 uppercase letters
- The tool shall treat special characters (/, -, *, ...) as spaces

## User interface
- The tool shall generate a list of acronyms in .doc format
- The tool shall make it possible to change the dictionaries using GUI
