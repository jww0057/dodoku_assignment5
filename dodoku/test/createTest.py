from unittest import TestCase
import dodoku.create as create 

class CreateTest(TestCase):
    def test_create_010_ShouldReturnThreeParms(self):
        level1 = {'op': 'create', 'level':'1'}
        expectedResult = {"grid", "integrity", "status"}
        actualResult = create._create(level1)
        self.assertIn("grid", actualResult)
        self.assertIn("integrity", actualResult)
        self.assertIn("status", actualResult)
        