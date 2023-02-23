import time

from main import print_hi


def test_print_hi(capsys):
    print_hi('TeamCity')
    captured = capsys.readouterr()
    assert 'Hi, TeamCity' in captured.out


def test_slow_test():
    time.sleep(60)
    print('This test is slow - it just sleeps for 60 seconds')


def test_failing_test():
    print('This test always fail')
    assert False
