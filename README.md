Resumoid
========

Let Work Speak

## Installation
Get the repo

    git clone git@github.com:garbados/Resumoid.git

Install python requirements

    virtualenv venv --no-site-packages
    source venv/bin/activate
    pip install -r requirements.txt

Resumoid uses `flask-assets`, which requires [node.js](http://nodejs.org/#)

Install more requirements after installing node for your system

    git submodule init
    git submodule update
    cd less.js
    ./configure
    make
    make install
    
Create config.settings

    touch config/settings.py

That should be it! Email me at garbados@gmail.com if it isn't.

## Running Resumoid
`python appy.py run`
