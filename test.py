import unittest
from zip_to_map import zipcode_to_map

class TestZipcodeToMap(unittest.TestCase):
    def test_zipcode_to_map(self):
        zipcodes = ['90210', '10001', '30301']
        try:
            zipcode_to_map(zipcodes, us_map=True)
        except Exception as e:
            self.fail(f"zipcode_to_map raised an exception {e}")
        
if __name__ == "__main__":
    unittest.main()
