import unittest
from unittest.mock import patch
from ImageToAscii.ImageToAscii import main as ITAMain
from ImageToAscii.VideoFrameExtract import main as VFEMain


class TestImageToAscii(unittest.TestCase):

    # @patch('builtins.input', return_value=image_path)
    def test_image(self):
        image_path = 'ImageToAscii/naist_logo_sq.jpg'
        result = ITAMain(150, image_path)
        self.assertIsNotNone(result)
        