import subprocess
import unittest
import shutil
import os


def rmfile(filename):
    os.remove(filename) if os.path.exists(filename) else None

class TestCmdLine(unittest.TestCase):

    def test_00(self):
        rmfile('/tmp/op1')
        rmfile('/tmp/op2')
        subprocess.check_output('ci-yml', shell=True)
        assert os.path.exists('/tmp/op1')

    def test_10(self):
        """ test1 should raise exception """
        rmfile('/tmp/fail_test1')
        try:
            subprocess.check_output('ci-yml test1', shell=True)
        except:
            assert os.path.exists('/tmp/fail_test1')

    def test_20(self):
        rmfile('/tmp/build_doc')
        subprocess.check_output('ci-yml build_doc', shell=True)
        assert os.path.exists('/tmp/build_doc')

    def test_30(self):
        rmfile('/tmp/deployed')
        subprocess.check_output('ci-yml deploy', shell=True)
        assert os.path.exists('/tmp/deployed')

    def test_40(self):
        assert 'env_test' in subprocess.check_output('ci-yml env_test', shell=True)

    def test_50(self):
        user = os.environ['USER']
        rmfile('/tmp/{}'.format(user))
        subprocess.check_output('ci-yml env_test', shell=True)
        assert os.path.exists('/tmp/{}'.format(user))

if __name__ == '__main__':
    unittest.main()
