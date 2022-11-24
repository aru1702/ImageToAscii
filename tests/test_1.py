import unittest
from ImageToAscii.ImageToAscii import main as ITAMain


class TestImageToAscii(unittest.TestCase):
    def test_image(self):
        image_path = 'ImageToAscii/naist_logo_sq.jpg'
        result = ITAMain(150, image_path)
        self.assertIsNotNone(result)
        