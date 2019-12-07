import mock
import time

import pytest

import reeeeeeeeee as reee


# Prevent calls to sleep
class SleepMock(object):
    def __init__(self):
        self.mock_obj = mock.MagicMock()

    def __call__(self, *args):
        self.mock_obj(*args)


time.sleep = SleepMock()


@pytest.fixture()
def curses():
    with mock.patch('reeeeeeeeee.curses') as cur_mock:
        cur_mock.return_value = cur_mock.initscr = cur_mock
        cur_mock.COLS = 79

        yield cur_mock


def test_reeeeeeeeee(curses):
    reee.reeeeeeeeee()

    assert curses.initscr.called
    assert curses.noecho.called
    assert curses.endwin.called
    assert curses.curs_set.call_args == mock.call(0)
    assert curses.nodelay.call_args == mock.call(True)
    assert curses.leaveok.call_args == mock.call(True)
    assert curses.scrollok.call_args == mock.call(False)
