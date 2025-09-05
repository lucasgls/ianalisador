import unittest
from src.ianalisador.utils.jobs_database import JobsDatabase

class TestJobsDatabase(unittest.TestCase):
    def setUp(self):
        self.db = JobsDatabase()
    
    def test_get_jobs(self):
        jobs = self.db.get_jobs()
        self.assertIsInstance(jobs, list)
        self.assertGreater(len(jobs), 0)
        self.assertIn('titulo_vaga', jobs[0])
        pass
    
    def test_get_job_by_title(self):
        job = self.db.get_job_by_title("Assistente de Vendas")
        self.assertIsNotNone(job)
        self.assertEqual(job['titulo_vaga'], "Assistente de Vendas")
    
        job = self.db.get_job_by_title("Título Inexistente")
        self.assertIsNone(job)
        pass

    def test_file_not_found(self):
        self.db.jobs_file = "arquivo_inexistente.json"
        with self.assertRaises(Exception):
            self.db.get_jobs()