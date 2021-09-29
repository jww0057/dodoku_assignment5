import unittest
import dodoku.info as info

class InfoTest(unittest.TestCase):
    def test_info_010_ShouldReturnMyUsername(self):
        expectedResult = {'info': 'jww0057'}
        parms = {'op': 'info'}
        actualResult = info.info(parms)
        self.assertDictEqual(expectedResult, actualResult)