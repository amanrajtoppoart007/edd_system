# tests/test_jobs.py
import unittest
from models.job import Job

class TestJob(unittest.TestCase):
    def test_job_creation(self):
        job = Job("Replace battery")
        job.save()
        jobs = Job.get_all()
        self.assertTrue(any(j[1] == "Replace battery" for j in jobs))

if __name__ == '__main__':
    unittest.main()