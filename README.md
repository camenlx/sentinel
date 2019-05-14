# 01Coin Sentinel

An all-powerful toolset for 01coin.

Sentinel is an autonomous agent for persisting, processing and automating 01coin governance objects and tasks, and for expanded functions in upcoming 01coin releases.

Sentinel is implemented as a Python application that binds to a local version 0.12.3 zerooned instance on each 01coin Masternode.

This guide covers installing Sentinel onto an existing Masternode in Ubuntu 14.04 / 16.04.

## Installation

The following detailed steps are all condensed into ONE easy command that you can take advantage of if your 01coin Masternode was  previously installed using the scripts provided by the 01coin community (NB: the script requires you have sudo/root password), or manually using the same installation method as the scripts.

    wget https://raw.githubusercontent.com/zocteam/sentinel/master/sentinel-one-line-installer.sh && chmod +x sentinel-one-line-installer.sh && ./sentinel-one-line-installer.sh

### 1. Install Prerequisites

Make sure Python version 2.7.x or above is installed:

    python --version

Update system packages and ensure virtualenv is installed:

    $ sudo apt-get update
    $ sudo apt-get -y install python-virtualenv virtualenv


### 2. Install Sentinel

Clone the Sentinel repo and install Python dependencies.
    
    $ git clone https://github.com/zocteam/sentinel.git zoc_sentinel && cd zoc_sentinel
    $ virtualenv ./venv
    $ ./venv/bin/pip install -r requirements.txt

### 3. Set up Cron

Set up a crontab entry to call Sentinel every minute:

    $ crontab -e

In the crontab editor, add the lines below, replacing '$HOME/sentinel' to the path where you cloned sentinel to:

    * * * * * cd $HOME/zoc_sentinel && SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py >> zoc_sentinel.log >/dev/null 2>&1

### 4. Test the Configuration

Test the config by running all tests from the sentinel folder you cloned into

    $ ./venv/bin/py.test ./test

With all tests passing and crontab setup, Sentinel will stay in sync with zerooned and the installation is complete

## Configuration

An alternative (non-default) path to the `zeroone.conf` file can be specified in `sentinel.conf`:

    zeroone_conf=/path/to/zeroone.conf

## Building

Install pyinstaller `pip install pyinstaller`

Generate output EXE/ELF: `pyinstaller --onefile --paths=lib/ main.py`

## Troubleshooting

To view debug output, set the `SENTINEL_DEBUG` environment variable to anything non-zero, then run the script manually:

    $ SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py

## Contributing

Please follow the [ZeroOneCore guidelines for contributing](https://github.com/zocteam/zeroonecoin/blob/master/CONTRIBUTING.md).

Specifically:

* [Contributor Workflow](https://github.com/zocteam/zeroonecoin/blob/master/CONTRIBUTING.md#contributor-workflow)

    To contribute a patch, the workflow is as follows:

    * Fork repository
    * Create topic branch
    * Commit patches

    In general commits should be atomic and diffs should be easy to read. For this reason do not mix any formatting fixes or code moves with actual code changes.

    Commit messages should be verbose by default, consisting of a short subject line (50 chars max), a blank line and detailed explanatory text as separate paragraph(s); unless the title alone is self-explanatory (like "Corrected typo in main.cpp") then a single title line is sufficient. Commit messages should be helpful to people reading your code in the future, so explain the reasoning for your decisions. Further explanation [here](http://chris.beams.io/posts/git-commit/).

### License

Released under the MIT license, under the same terms as 01coin itself. See [LICENSE](LICENSE) for more info.
This sw was forked from DashCore and follows the same terms.
