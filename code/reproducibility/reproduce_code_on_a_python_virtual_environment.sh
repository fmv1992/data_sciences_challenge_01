#! /bin/zsh

# Set script to stop on error.
set -e

# Set low priority.
renice -n 19 $$

# Print file versions.
echo "Reproducing the challenge..."
echo "Python version should be 3.6.1 for ensured reproducibility: $(python3 -V)"
echo "Virtualenv version should be 15.1.0 for ensured reproducibility: $(virtualenv --version)"
export packages="
numpy==1.12.1
pandas==0.19.2
scipy==0.19.0
scikit-learn==0.18.1
matplotlib==2.0.0
seaborn==0.7.1
data-utilities==1.2.6
"

# Install all packages.
echo "Now going to install needed packages to reproduce this challenge: \n$packages"

# Setup folders.
export virtualenvpath=/tmp/virtual_env
set +e  # in case it is the first run this rm command may result in error and halting of the script
rm -rf "$virtualenvpath"
set -e

# Create the virtual env.
virtualenv --no-download --no-site-packages $virtualenvpath
cd $virtualenvpath
source ./bin/activate || :
if [[ "$(which python3)" =~ "virtual_env"  ]]
then
    which python3
else
    echo "Virtual env not correctly initialized"
    which python3
    exit 1
fi

# Install dependencies.
for package in $(echo $packages);
do
    echo "Installing $package..."
    # Ensure a fresh install.
    pip3 --no-cache-dir install -U --force-reinstall  $package
done

# Clone the project.
git clone --depth=1 -b develop https://github.com/fmv1992/data_sciences_challenge_01

# Create a matplotlibrc file
export script_matplotlibrc="$virtualenvpath/matplotlibrc"
export MPLBACKEND=$(python3 ./data_sciences_challenge_01/code/reproducibility/get_matplotlib_backend.py)

# Moment of truth: run the challenge.
cd ./data_sciences_challenge_01/code/
python3 ./main.py
cd $virtualenvpath

# Done! Sucess!
echo "Done! Sucess!"
