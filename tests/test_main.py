import pytest


class TestMain(object):

    def test_index(self, testapp):
        """ Test if the homepage loads """
        resp = testapp.get('/')

        assert resp.status_code == 200
