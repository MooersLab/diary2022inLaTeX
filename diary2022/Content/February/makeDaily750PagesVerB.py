#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division, print_function
import sys, os
Usage=""" 
 ./makeDaily750Pages.py year month startCalDay endCalDay
example:
./makeDaily750Pages.py 2017 'November' 6 30
"""

"""
Purpose: write out the plain text files for the month.
There is one file per day.

Read in from command line the following parameters:

year # as four digit integer
month # as string
startCalDay # as integer 
endCalDay

Thus script initially will write the files for one month or part of a month.

Write out plain tex files for each day with the following first line:
%!TEX root = ../../main.tex

%awk '/^\%TODO/' 22October2017.tex > 22October2017TODOawk.tex
%sed -n '/^\%TODO/p' 22October2017.tex > 22October2017TODOsed.tex
%grep '^\%TODO' 22October2017.tex > 22October2017TODOgrep.tex

Blaine Mooers

5 November 2017

Updated to write boilerplate to a comment environment at the bottom of the page.
This spares the need to use percent signs to comment out the boilerplate.

6 July 2019
"""

def makeDailyPages():
    year=sys.argv[1]
    syear=str(year)
    print(syear)

    month=sys.argv[2]
    smonth=str(month) 
    print(month)

    startCalDay=sys.argv[3]
    sstartCalDay=str(startCalDay)
    istartCalDay=int(startCalDay)
    print(sstartCalDay)

    endCalDay=sys.argv[4]
    sendCalDay=str(endCalDay)
    iendCalDay=int(endCalDay)  
    print(sendCalDay)

    print("Usage: ./makeDaily750Pages.py year month startday endday")
    print("Example: ./makeDaily750Pages.py 2017 'November' 6 30")

    inumAtJobs = ((iendCalDay - istartCalDay) + 1)
    print(str(inumAtJobs))
    writeJobs = [x for x in range(inumAtJobs)]
    day = istartCalDay
    sday =str(day)
    for job in writeJobs:
        sday = str(day)
        newfile = sday + month + syear + ".tex"
        h = open(newfile, 'w')
        h.write(r'%!TEX root = ../../main.tex' + '\n')
        h.write('\n')
        # h.write(r'\subsection{Metadata}' + '\n')
        # h.write(r'\begin{table}[htp]' + '\n')
        # h.write(r'\caption{Metadata.}' + '\n')
        # h.write(r'\label{tab:metadatas'+ sday + smonth + syear + '}' + '\n')
        # h.write(r'\begin{center}' + '\n')
        # h.write(r'\begin{tabular}{ll}' + '\n')
        # h.write(r'% \begin{tabular}{l p{12cm}} % use p when you have to control the column width' + '\n')
        # h.write(r'\toprule' + '\n')
        # h.write(r'SLEEP: & 5.5 \\' + '\n')
        # h.write(r'WALKED: & 0.0 miles \\' + '\n')
        # h.write(r'WEIGHT: & 178.8 \\ ' + '\n')
        # h.write(r'\bottomrule' + '\n')
        # h.write(r'\end{tabular}' + '\n')
        # h.write(r'\end{center}' + '\n')
        # h.write(r'\end{table}' + '\n')
        # h.write('\n')
        # h.write(r'\subsection{Last night}' + '\n')
        # h.write(r'I went to bed at 10:30 PM.' + '\n')
        # h.write('\n')
        # h.write(r'\subsection{This morning}' + '\n')
        # h.write(r'I woke at 3:30 AM.' + '\n')
        # h.write('\n')
        # h.write(r'\subsection{Change me}' + '\n')
        # h.write(r'% \index{Change me}' + '\n')
        # h.write('\n')
        
        # h.write(r'%%%%%%%%%%%%%%Commented out boilerplate %%%%%%%%%%%%%%' + '\n')
        # h.write(r'\begin{comment}' + '\n')
        # h.write(r'\subsection{To Be Done}' + '\n')
        # h.write(r'\begin{enumerate}' + '\n')
        # h.write(r'\item ' + '\n')
        # h.write(r'\item ' + '\n')
        # h.write(r'\item ' + '\n')
        # h.write(r'\item ' + '\n')
        # h.write(r'\item ' + '\n')
        # h.write(r'\item ' + '\n')
        # h.write(r'\end{enumerate}' + '\n')
        # h.write('\n')
        # h.write(r'\subsection{To Be Done}' + '\n')
        # h.write(r'\begin{itemize}' + '\n')
        # h.write(r'\item ' + '\n')
        # h.write(r'\item ' + '\n')
        # h.write(r'\item ' + '\n')
        # h.write(r'\item ' + '\n')
        # h.write(r'\item ' + '\n')
        # h.write(r'\item ' + '\n')
        # h.write(r'\end{itemize}' + '\n')
        # h.write('\n')
        # h.write(r'\subsection{To Be Done}' + '\n')
        # h.write(r'\begin{description} ' + '\n')
        # h.write(r'\item [] ' + '\n')
        # h.write(r'\item [] ' + '\n')
        # h.write(r'\item [] ' + '\n')
        # h.write(r'\item [] ' + '\n')
        # h.write(r'\item [] ' + '\n')
        # h.write(r'\item [] ' + '\n')
        # h.write(r'\end{description}' + '\n')
        # h.write('\n')
        # h.write(r'% No line numbering' + '\n')
        # h.write(r'\begin{code}{}' + '\n')
        # h.write(r'\label{lst:FindByte}' + '\n')
        # h.write(r'\index{copying and pasting code!lost bytes}' + '\n')
        # h.write(r'\caption{Python script to find lost bytes.}' + '\n')
        # h.write(r'\begin{minted}[frame=lines,framerule=2pt]{python}' + '\n')
        # h.write(r'import me' + '\n')
        # h.write(r'\end{minted}' + '\n')
        # h.write(r'\end{code}' + '\n')
        # h.write('\n')
        # h.write(r'% Line numbering on and aligned with left margin. ' + '\n')
        # h.write(r'\begin{code}{}' + '\n')
        # h.write(r'\index{openCV!measureSizes}' + '\n')
        # h.write(r'\label{lst:measureSize}' + '\n')
        # h.write(r'\caption{Contents of measureSizes.py.}' + '\n')
        # h.write(r'\begin{minted}[frame=lines,framerule=2pt,linenos=true,xleftmargin=\parindent,breaklines]{python}' + '\n')
        # h.write(r'import me' + '\n')
        # h.write(r'\end{minted}' + '\n')
        # h.write(r'\end{code}' + '\n')
        # h.write('\n')
        # h.write(r'% Code env with inputminted file.' + '\n')
        # h.write(r'\begin{code}{}' + '\n')
        # h.write(r'\label{lst:quadraticEstimationBinomialPosterior}' + '\n')
        # h.write(r'\index{quadratic estimation of a binomial posterior}' + '\n')
        # h.write(r'\caption{Example of the use of quadratic estimation of a binomial posterior.}' + '\n')
        # h.write(r'\inputminted[frame=lines,framerule=2pt]{R}{./Content/codeListings/McElreath2015quadraticEstPosterior.R}' + '\n')
        # h.write(r'\end{code}' + '\n')
        # h.write('\n')
        # h.write(r'\begin{listing}[H]' + '\n')
        # h.write(r'\begin{pythoncode}' + '\n')
        # h.write(r'import me' + '\n')
        # h.write(r'\end{pythoncode}' + '\n')
        # h.write(r'\end{listing}' + '\n')
        # h.write('\n')
        # h.write(r'\begin{equation}\label{eq:XXXXX}' + '\n')
        # h.write(r'\end{equation}' + '\n')
        # h.write('\n')
        # h.write(r'\begin{align*}\label{eq:XXXXX}' + '\n')
        # h.write(r'\end{align*}' + '\n')
        # h.write('\n')
        # h.write(r'\begin{equation}\label{eq:XXXXX}' + '\n')
        # h.write(r'\begin{split}' + '\n')
        # h.write(r'A &= B' + '\n')
        # h.write(r'&= B' + '\n')
        # h.write(r'\end{split}' + '\n')
        # h.write(r'\end{equation}' + '\n')
        # h.write('\n')
        # h.write(r'\begin{minted}{bash}' + '\n')
        # h.write(r'\end{minted}' + '\n')
        # h.write('\n')
        # h.write(r'\begin{itemize}' + '\n')
        # h.write(r'\item ' + '\n')
        # h.write(r'\item ' + '\n')
        # h.write(r'\end{itemize}' + '\n')
        # h.write('\n')
        # h.write(r'\begin{enumerate}' + '\n')
        # h.write(r'\item ' + '\n')
        # h.write(r'\item ' + '\n')
        # h.write(r'\end{enumerate}' + '\n')
        # h.write('\n')
        # h.write(r'% Figure template' + '\n')
        # h.write(r'\newpage{}' + '\n')
        # h.write(r'\label{fig:workbookCell}' + '\n')
        # h.write(r'\begin{figure}[h]' + '\n')
        # h.write(r'%\centering' + '\n')
        # h.write(r'    \includegraphics[scale=0.2]{RSMCellRecipe}' + '\n')
        # h.write(r'\caption{Cell for one well from the \emph{BigCrystalsFast} \emph{Excel} Workbook. The concentrations and volumes are auto-populated by the workbook. The cells in gray contain the volumes to be aliquoted manually or with a liquid-handling robot. The user can also record the response(s) (crystal(s) size) for the well in the cell next to ``Response.''}' + '\n')
        # h.write(r'\end{figure}' + '\n')
        # h.write('\n')
        # h.write(r'% Table template' + '\n')
        # h.write(r'% needs \usepackage{booktabs}' + '\n')
        # h.write(r'\begin{table}[htp]' + '\n')
        # h.write(r'\caption{This is a test.}' + '\n')
        # h.write(r'\label{two columns}' + '\n')
        # h.write(r'\begin{center}' + '\n')
        # h.write(r'    \begin{tabular}{ll}' + '\n')
        # h.write(r'%    \begin{tabular}{l p{12cm}} % use p when you have to control the column width' + '\n')
        # h.write(r'\toprule' + '\n')
        # h.write(r'LongHeader1 & MediumHeaderX \\ ' + '\n')
        # h.write(r'\multicolumn{1}{c}{(unit1)} & ' + '\n')
        # h.write(r'\multicolumn{1}{c}{(unit2)} \\ \midrule' + '\n')
        # h.write(r'Item1   & X1      \\ ' + '\n')
        # h.write(r'Item2   & X2      \\ ' + '\n')
        # h.write(r'Item1   & X1      \\ ' + '\n')
        # h.write(r'Item2   & X2      \\ \bottomrule' + '\n')
        # h.write(r'\end{tabular}' + '\n')
        # h.write(r'\end{center}' + '\n')
        # h.write(r'\end{table}' + '\n')
        # h.write('\n')
        # h.write(r'%This unnumbered section goes to the end of the chapter' + '\n')
        # h.write(r'\section*{Exercises}' + '\n')
        # h.write(r'\begin{prob}' + '\n')
        # h.write(r'\label{problem:key}' + '\n')
        # h.write(r'problem text' + '\n')
        # h.write(r'\end{prob}' + '\n')
        # h.write(r'\end{comment}' + '\n')
        day = day + 1
        h.close()

if __name__ == '__main__':
    makeDailyPages()

"""
Enhancements could include making folders for each month
and writing the files to each folder.

Alternately, a bash script can be used to run this 
script to generate the files for a year.

#!/usr/bin/bash
./makeDaily750Pages.py 2017 'November' 6 30
./makeDaily750Pages.py 2017 'December' 1 31

"""
