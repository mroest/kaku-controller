import sys
import mock

class TestMain(object):

    def test_index(self, testapp):
        """ Test if the homepage loads """
        resp = testapp.get('/')

        assert resp.status_code == 200

    def test_switch_get(self, testapp):
        """ Test if the switch works """
        resp = testapp.get('/switch')

        # Response should not be allowed
        assert resp.status_code == 405

    def test_switch_post(self, testapp):
        # Mock transmitter
        sys.modules['app.kaku.transmitter'] = mock.Mock()

        # Response should be OK for post and give redirect
        resp = testapp.post('/switch')
        assert resp.status_code == 302
