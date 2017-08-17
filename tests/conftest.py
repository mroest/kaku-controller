import pytest
import mock
import sys

from app import create_app


@pytest.fixture()
def testapp(request):
    app = create_app('app.settings.TestConfig')
    client = app.test_client()
    return client


@pytest.fixture()
def transmitter():
    mocked = mock.Mock()
    mocked.Transmitter = mock.MagicMock()
    return mocked
