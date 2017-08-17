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

    def test_switch_post_redirect(self, testapp, transmitter):
        with mock.patch.dict(sys.modules, {'app.kaku.transmitter': transmitter}):
            resp = testapp.post('/switch')
            assert resp.status_code == 302
            transmitter.Transmitter.assert_not_called()

    def test_switch_post_off(self, testapp, transmitter):
        with mock.patch.dict(sys.modules, {'app.kaku.transmitter': transmitter}):
            resp = testapp.post(
                '/switch',
                data={'operation': 'Off'},
                follow_redirects=True)
            assert resp.status_code == 200
            transmitter.Transmitter.assert_called()

    def test_switch_post_on(self, testapp, transmitter):
        with mock.patch.dict(sys.modules, {'app.kaku.transmitter': transmitter}):
            resp = testapp.post(
                '/switch',
                data={'operation': 'On'},
                follow_redirects=True)
            assert resp.status_code == 200
            transmitter.Transmitter.assert_called()
