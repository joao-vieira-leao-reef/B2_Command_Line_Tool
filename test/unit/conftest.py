######################################################################
#
# File: test/unit/conftest.py
#
# Copyright 2023 Backblaze Inc. All Rights Reserved.
#
# License https://www.backblaze.com/using_b2_code.html
#
######################################################################
from test.unit.helpers import RunOrDieExecutor
from unittest import mock

import pytest
from b2sdk.raw_api import REALM_URLS

from b2.console_tool import _TqdmCloser


@pytest.fixture(autouse=True, scope='session')
def mock_realm_urls():
    with mock.patch.dict(REALM_URLS, {'production': 'http://production.example.com'}):
        yield


@pytest.fixture
def bg_executor():
    """Executor for running background tasks in tests"""
    with RunOrDieExecutor() as executor:
        yield executor


@pytest.fixture(autouse=True)
def disable_tqdm_closer_cleanup():
    with mock.patch.object(_TqdmCloser, '__exit__'):
        yield
