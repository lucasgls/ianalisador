import json
import os

class JobsDatabase:
    
    def __init__(self):
        self.jobs_file = "src/ianalisador/utils/jobs.json"

    def _ler_json(self):
        try:
            with open(self.jobs_file, encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            raise Exception("Arquivo não encontrado" + self.jobs_file)

    def get_jobs(self):
        vagas = self._ler_json()
        return vagas
    
    def get_job_by_title(self, titulo):
        vagas = self._ler_json()
            
        for vaga in vagas:
            if vaga["titulo_vaga"] == titulo:
                return vaga
    
    