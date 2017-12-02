# FileTypeCounter
A simple python program to collect the frequency of a file type within a directory

Created by Noah B Johnson
noahbjohnson@outlook.com

## Introduction
This is a very simple and poorly documented tool that I wrote while recovering data from a corrupted hard drive using PhotoRec. PhotoRec dumps every file it recovers into one of the hundreds of sub-directories. I had written another (shell) script to copy all the files of a certain type, but I needed a way to determine what file types were recovered.

## Installation
##### NOTE: This program has not been tested on a non-unix system!
The only requisite for this program is Python 3.x.

1: Download the python file containing the program:  FileTypeCounter/filecount.py

2: Move the program to the direcetory being analyzed (optional)

3: Navigate to the program's location in shell and execute "Python filecount.py"

## Use

The use of this tool is very straightforward. You will have the option to choose the directory to analyze, whether or not to include sub-directories, and where to save the "output.csv" file.

#### The tool only currently supports one level of subdirectories
