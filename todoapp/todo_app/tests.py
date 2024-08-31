from django.test import TestCase
from .models import Task, Author
from django.utils import timezone

class TaskModelTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name='Georges Tester',
            email='test@gmail.com'
        )

    def test_task_str(self):
        task = Task(
            title="Write tests",
            description="Ensuring all model attributes have correct tests",
            due_date=timezone.now().date(),
            author=self.author,
            status="Complete"  # Ensure status is set for the test
        )
        
        expected_str = "title: Write tests\nstatus: Complete"  # Updated expected string
        
        self.assertEqual(str(task), expected_str)
