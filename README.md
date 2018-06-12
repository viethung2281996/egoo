# Install virtualenv 
wget https://bootstrap.pypa.io/get-pip.py

sudo python3 get-pip.py

sudo pip3 install virtualenv

virtualenv -p python3 pyenv

source pyenv/bin/activate

# Install library for project

cd egoo_core

pip install -r requirment.txt
