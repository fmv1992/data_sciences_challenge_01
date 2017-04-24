# Easynvest Code challenge

The publishing of the challenge and results were authorized by Easynvest
staff.

# Description

This file is a high level description of what is the challenge, what is the
data set, how was the approach and the results.

***The full results and discussion are in
`./output/final_results/output.html`.***  
In order to view the final results please open the file (do not load the github
file as github does not render html files but rather it shows its code):
`./output/final_results/output.html`.

# The challenge

The challenge is to interpret and group a given data set. Interpretation,
coding quality, reproducibility and presentation of the results are some of the
assessment criteria.

See `./challenge_description/challenge_description.pdf` for description.

# The data set

The original dataset was given as a xlsx spreadsheet and was converted to csv
format for convenience.

# Approach

A high level definition of the approach is:

* Understanding and investigating the data set (exploratory analysis)
* Choice of clusterization algorithm and choice of the number of clusters
* Carrying out the interpretation

Methods and tools:

* Python was used to perform data analysis
* Pandoc and pandoc markdown were used to craft the report
* Vim and unixes tools were used to manage the project (git, other unixes
    programs such as less, cat, time, grep, etc)

# Results

A partial result is available on `./output/partial_results/*`.

A final result is available on `./output/final_results/output.html`.

The results are crafted using pandoc. Thus they are available on a couple of
different formats.

```
pandoc  --dpi 300 --from markdown+compact_definition_lists+example_lists
--css=$(cygpath -w ~/.pandoc/css/github.css ) --columns 79 --atx-headers
--data-dir=$(cygpath -w ~/.pandoc/templates/ )  --self-contained
--standalone  -s ./*md -o $(cygpath -w /tmp/output.html)
```

***I recommend the html version which is the one I've been using to get
feedback.***  
Docx and pdf versions are provided for convenience. Their rendering fidelity to
the final deliverable is not warranted though.

# Reproducibility

This project is easily reproducible. In order to do that one just needs to run:
`zsh ./code/reproducibility/reproduce_code_on_a_python_virtual_environment.sh`.
The script will:

1. **Clean the `/tmp/virtual_env` path.**
1. Setup a virtual environment.
1. Install dependencies using pip.
1. Clone this project.
1. Execute the project. If sucessfull the last message will be: `Done! Sucess!`
