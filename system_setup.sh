sudo apt-get install sqlite3
sudo apt-get install libsqlite3-dev
sudo apt-get install libbz2-dev
sudo apt-get install libreadline-dev

git clone https://github.com/pyenv/pyenv.git
cd pyenv
git checkout tags/v2.3.7

./bin/pyenv install 3.7.10
