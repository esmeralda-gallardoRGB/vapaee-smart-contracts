#!/usr/bin/env python3

from .constants import TelosProfile, telosprofile


def test_addprofile(telosprofile):
    account, alias = telosprofile.new_profile()

    profile = telosprofile.get_profile(alias)

    assert profile is not None
    assert account in profile['owners']


def test_addprofile_exists(telosprofile):
    account, alias = telosprofile.new_profile()

    ec, out = telosprofile.testnet.push_action(
        TelosProfile.contract_name,
        'addprofile',
        [account, alias],
        f'{account}@active'
    )
    assert ec == 1
    assert 'identical profile exists' in out