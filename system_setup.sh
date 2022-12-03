sudo apt-get install gcc
sudo apt-get install make
sudo apt-get install sqlite3
sudo apt-get install libsqlite3-dev
sudo apt-get install libbz2-dev
sudo apt-get install libreadline-dev
sudo apt-get install zlib1g-dev
sudo apt-get install libssl-dev
sudo apt-get install libffi-dev
sudo apt-get install liblzma-dev
sudo apt-get install python3-virtualenv

git clone https://github.com/pyenv/pyenv.git
cd pyenv
git checkout tags/v2.3.7

echo 'export PYENV_ROOT="$HOME/volume-xc/.pyenv"' >> ~/.bashrc

./bin/pyenv install 3.7.10
