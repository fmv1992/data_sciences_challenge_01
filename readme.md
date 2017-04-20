# Code challenge easynvest

***(work in progress)***

# Description

This document is a high level description of what is the challenge, what is the
data set, how was the approach and the results.

# The challenge

# The data set

# Approach

# Results ***(work in progress)***

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
