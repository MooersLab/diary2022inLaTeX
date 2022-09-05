# Diary for 2022 in LaTeX

## What is this?

This repo contains a template book with 365 blank tex files, one for each day of the year.
These tex files are collated and rendered into a PDF with latex and bibtex compilers.
It is set up for 2022.
It is configured to automatically generate the following:

- Chapter headings and section headings (add subsections and lower in your daily writing).
- Chapters and sections are automatically numbered.
- Table of Contents, hyperlinked
- References Cited, hyperlinked
- Index, hyperlinked
- Lists of code listings, hyperlinked
- List of Figures, hyperlinked
- List of Tables, hyperlinked
- An appendix that uses chapters that are arranged in alphabetical order by letters instead of numbers.
- Page numbers
- Epigraphs for Chapter header pages
- Urls in footnotes to prevent them from running into the right margin.
- Syntax highlighting of code via the minted package
- Supports the use of equations with captions (i.e., makes it is possible generate lists of equations).


The document is based on the Springer book format, but it has a 7 by 9 inch area for writing with conservative margins to save paper.


## What is this good for?

This can be used for the following purposes:

- diary
- laboratory notebook
- log book
- managing todo lists and plans
- provide material for an autobiography, biography, or to stimulate nonfiction and fiction books.
- to document one's life to inspire one's descendents
- storage site for daily writing on sites like 750words.com

This document's design was stimulated by the last use.
I wanted an independent place to store my daily writing on [750words.com](https://750words.com) where is it stored in plain text files that are hard to search.
I wanted that writing to be indexable and searchable in a single PDF for a calendar year rather than in 365 files.
This documet has been very useful for finding information, including data wrangling protocols and computer code, that I used in the past.
If it is used as a *Captian's log'* of ones own *Enterprise*, it can be used to gather information for annual reports.
For example, lists of accomplishments can be stored in the Appendices.

## Prior Experience

I have been using something like this since 2012 and this document in its current format since 2015.
Each year's document has run about 1000-1200 pages in length.
It is part of my daily routine to paste the day's writing into this document before retiring for the day or first thing in the following morning.

## Limitations

Writing in LaTeX has some limitations:

- The document is limited by computer RAM to one year. 
- The document is limited by RAM in terms of the number of lists and indices that can be generated at a time.
- Debugging can sometimes involve commenting out chapters in the 0AAAContent document to isolate the error. 

Not to worry! The debugger on Overleaf will locate the bug by document name and line number. 
A click on an arrow will take you to the bug in the correct file.

I generally fall behind on my debugging and will comment out earlier chapters to prevent their errors from stopping compiling.
I debug the old writing occassionally during the year when too tired to do anything else and during winter break before the start of the new year.

## Compiling

The *main.tex* document is feed to the compiler.

Compile with lualatex and the `-escape-shell` key (for the minted package).
The compile.sh script is run in the top level of the folder `2023diary`, which you can rename.
The document is easy to compile with the click of a button using the Overleaf website.
The empty shell document takes several seconds to compile.
A 1000-page document will compile in about 60 seconds.

This long compile time is another advantage of the modular approach as opposed to having everything in one tex file.
I comment out the inactive months in the *0AAAContents.tex* file to shorten the compile time to a few seconds.

## Role of the 0AAAContents.tex file.

The *0AAAContents.tex* file is the cental nervous system of the document.
It is trival to comment out entire chapters via a single percent sign.
It is also trival in Emacs to shuffle the order of the chapters by moving lines up or down.
You can add prose to the *0AAAContents.tex* file, but I find it adds clutter to this file.

## Configuration

- Edit the title and author at the top of the A000Contents.tex file in the Content subfolder.
- Change the cover figure to suit by loading a new image into the ./Content/Figures subfolder and by editing the path to the image to specify this new figure. Some image file formats like tiff are not supported. Png  and PDF are reliable.
- Comment out the lists that you do not intend to use in 0AAAContent. For example, if you do not save computer code, the list of listings will not be used.
- A your new appendices like your annual plan to the Appendix as a tex file.

## Daily use

The documents to be edited are in chapter subfolders in the Content subfolders.
Each day's entry is in a separate tex file.
Navigate to the file corresponding to the current date and start writing on line two.
The code on the first line must remain in place for the document to compile.

Each file forms a section of a chapter.
This book has one chapter per month.
All sections for a month are in a chapter subfolder in the Content folder.

## On-line editor

I recommend using the on-line editor Overleaf for the smoothest operation.
I have been editing this document on Overleaf for six years.
You do NOT have to run each of the steps of compiling separately.
You just click a button and the latex and bibtex compilers are run seemlessly.
I store the URL for this project in my private home page for rapid access.

You can compile the entire document with any document open in the tex area because the main document is set in a the menu panel on the left.
This meanu is also where you configure the compiler, key bindings, color theme, and so on.

## Local editors

In terms of local editing, there are many text editors (>20) that are freely available and have great support for editing documents in LaTeX.
The following are perhaps the most popular general purpose editors that have great support for LaTeX:

- TextMate for the Mac (very easy to compile with `cmd-R`)
- Sublime Text
- VSC
- Vim
- Emacs

TextMate for the Mac does not get enough love these days.
It starts lightning fast.
It is still the editor that I open most frequently, although I am trying to migrate to Emacs.

Emacs is the most configurable editors, thanks to elisp and a dedicated developer community.

### Emacs

Must be configured to use laulatex and -escape-shell. 
It might be easiest to call the shell with `M-!` and enter `compile.sh main.tex` to compile and open in you default PDF viewer.
Or just run the compile.sh script externally to Emacs.

See the `latex-emacs` repo for a sample configuration.
If you have citations, you will have to run bibtex on main.tex.

## Best of both worlds: use local editor to edit today entry on Overleaf

The Google Chrome extension [GhostText](https://ghosttext.fregante.com/) supports the use of several kinds of local editors to edit text areas in web browsers.
The opened *toadayDate.tex* file is a text area in Overleaf.
You can bring you favorite LaTeX snippets to bear on Overleaf, which does not support snippets directly.

For example, I start the day by opening Emacs, logging into 750words, and clicking on the GhostText icon to open the connection to Emacs.
In Emacs in the **Write your words** buffer, I enter `start` and hit `TAB` or `C-o`. 
This action inserts the following boilerplate from the `start` snippet file, which is available above.
I have [configured](https://github.com/MooersLab/latex-emacs) the Emacs package [atomic-chrome](https://github.com/alpha22jp/atomic-chrome) to open `Write your words` in the latex-mode so that I can have access to my latex-mode snippets, which are available [here](https://github.com/MooersLab/snippet-latex-mode).

```latex
\subsection{Last night}
change me


\subsection{This morning}
change me


\subsection{To Be Done Today}
\index{To Be Done!2022-09-04}
\begin{itemize}
\item change me
\item change me
\item change me
\item change me
\item change me
\item change me
\item change me
\item change me
\item change me
\item change me
\end{itemize}

```

The cursor advances to `change me` under *Last night*.
I make some notes about what I did.
Then I hit tab to advance to the next `change me` to make notes about the morning.
I hit tab again to advance to the first item in my TODO list for the day.
When I reach the bottom of the list, I enter `C-c C-j` to enter the next **\item** properly aligned and with the cursor in the right postion.

A called to a macro inside the yasnippet snippet called *start* inserts the correct date in the index key.
I create an index key without lifting a finger.
**See, Life can be Good in Emacs!**

See the end of this [slideshow](https://github.com/MooersLab/BerlinEmacsAugust2022) for the application of GhostText to LaTeX editing with Emacs.
For the Jupyter users, you can likewise use GhostText to edit code and markdown cells with your favorite editor.
See [slideshow](https://github.com/MooersLab/DSW22ghosttext) about this exciting topic.
See corresponding [video](https://mediasite.ouhsc.edu/Mediasite/Channel/python/watch/4da0872f028c4255ae12935655e911321d).

