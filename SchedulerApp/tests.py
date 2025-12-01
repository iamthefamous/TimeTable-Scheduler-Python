from django.test import TestCase

# Create your tests here.
from .views import Schedule, Data

class ScheduleTestCase(TestCase):
    def test_schedule_initialization(self):
        """Test that Schedule can be initialized and generate classes"""
        data = Data()
        schedule = Schedule(data).initialize()
        self.assertIsNotNone(schedule.getClasses())
        self.assertGreaterEqual(schedule.getFitness(), 0)
        self.assertLessEqual(schedule.getFitness(), 1)