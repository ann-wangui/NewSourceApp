import unittest
from app.models_articles import Source

class SourcesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.new_source = Source("1234","BBC News")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))
