# Code challenge easynvest

***(work in progress)***
***(see results section below for indication of partial results)***

# Description

This document is a high level description of what is the challenge, what is the
data set, how was the approach and the results.

# The challenge

***(work in progress)***
***(see results section below for indication of partial results)***

# The data set

***(work in progress)***
***(see results section below for indication of partial results)***

# Approach

***(work in progress)***
***(see results section below for indication of partial results)***

# Results

A partial result is available on `output/partial_results/*`.

The results are crafted with the `output/output.md` using pandoc. Thus they are
available on a couple of different formats.

```
pandoc  --dpi 300 --from markdown+compact_definition_lists+example_lists
--css=$(cygpath -w ~/.pandoc/css/github.css ) --columns 79 --atx-headers
--data-dir=$(cygpath -w ~/.pandoc/templates/ )  --self-contained
--standalone  -s ./*md -o $(cygpath -w /tmp/output.html)
```

I recommend the html version which is the one I've been using to get feedback.

**Do not read the markdown version as it is a pandoc markdown syntax and thus
not properly rendered by github.**

For your convenience the website <http://htmlpreview.github.io/> can render
html files on github.
