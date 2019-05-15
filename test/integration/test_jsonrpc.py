import pytest
import sys
import os
import re
os.environ['SENTINEL_ENV'] = 'test'
os.environ['SENTINEL_CONFIG'] = os.path.normpath(os.path.join(os.path.dirname(__file__), '../test_sentinel.conf'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'lib'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import config

from zerooned import ZeroOneDaemon
from zeroone_config import ZeroOneConfig


def test_zerooned():
    config_text = ZeroOneConfig.slurp_config_file(config.zeroone_conf)
    network = 'mainnet'
    is_testnet = False
    genesis_hash = u'00000c8e2be06ce7e6ea78cd9f6ea60e22821d70f8c8fbb714b6baa7b4f2150c'
    for line in config_text.split("\n"):
        if line.startswith('testnet=1'):
            network = 'testnet'
            is_testnet = True
            genesis_hash = u'00000ebe61e5bc70bc968b9cf4e5ed85ec996a85a68853361557876ae37a1648'

    creds = ZeroOneConfig.get_rpc_creds(config_text, network)
    zerooned = ZeroOneDaemon(**creds)
    assert zerooned.rpc_command is not None

    assert hasattr(zerooned, 'rpc_connection')

    # ZeroOne testnet block 0 hash == 00000ebe61e5bc70bc968b9cf4e5ed85ec996a85a68853361557876ae37a1648
    # test commands without arguments
    info = zerooned.rpc_command('getinfo')
    info_keys = [
        'blocks',
        'connections',
        'difficulty',
        'errors',
        'protocolversion',
        'proxy',
        'testnet',
        'timeoffset',
        'version',
    ]
    for key in info_keys:
        assert key in info
    assert info['testnet'] is is_testnet

    # test commands with args
    assert zerooned.rpc_command('getblockhash', 0) == genesis_hash
