import unittest
from unittest.mock import patch
import time

# Import the function or class that implements the scheduler
from scheduler import Scheduler

class TestScheduler(unittest.TestCase):

    @patch('time.time', return_value=1609459200)  # Mock the system time to a specific timestamp (e.g., January 1, 2021, 00:00:00)
    def test_task_scheduling(self, mock_time):
        # Create an instance of the Scheduler class
        scheduler = Scheduler()

        # Define the delay for the task (in seconds)
        delay = 3600  # 1 hour delay (3600 seconds)

        # Define the expected execution time (T + x)
        expected_execution_time = time.time() + delay

        # Schedule a task to run after the delay
        scheduler.schedule_task(delay)

        # Mock time.time to simulate the passage of time until the expected execution time
        with patch('time.time', return_value=expected_execution_time + 1):  # Add 1 second to ensure the task has enough time to execute
            # Execute the scheduled tasks (e.g., by calling a method that checks for pending tasks and executes them)
            scheduler.execute_tasks()

            # Assert that the task has been executed
            self.assertTrue(scheduler.task_executed)

if __name__ == '__main__':
    unittest.main()
