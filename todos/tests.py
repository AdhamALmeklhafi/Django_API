from django.test import TestCase

from .models import Todo

# Create your tests here.


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="first todoc",
            desc="first todoc",
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "first todoc")
        self.assertEqual(self.todo.desc, "first todoc")
