from django.test import TestCase
from .models import Category, Image, Location
# Create your tests here.
class PhotoTestClass(TestCase):
    def setUp(self):
        self.new_photo = Image('new_url')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_photo, Image))

class LocationTestClass(TestCase):
    def setUp(self):
        self.save_location= Location()

    def test_instance(self):
        self.assertTrue(isinstance(self.save_location, Location))

class CategoryTestClass(TestCase):
    def setUp(self):
        self.save_category= Category()

    def test_instance(self):
        self.assertTrue(isinstance(self.save_category, Category))