from apps.monitoreo.application.repositories_interfaces.rsa_repository_interface import RsaRepositoryInterface
from apps.monitoreo.domain.models.rsa_model import RsaModel
from core.domain.models.congruence_solver import CongruenceSolver
from core.domain.models.rsa_solver import RsaSolver
class RsaRepository(RsaRepositoryInterface):
    def __init__(self):
        self.congruence_solver = CongruenceSolver()
        super().__init__()

    def do_rsa(self, rsa_model: RsaModel):
        return rsa_model

    def undo_rsa(self, rsa_model: RsaModel):
        return rsa_model

    def set_test_list(self, rsa_model: RsaModel):
        rsa_model.list = [
            RsaSolver(
                array=[
                    ['A',0],['B',1],['C',2],['D',3],['E',4],
                    ['F',5],['G',6],['H',7],['I',8],['J',9],
                    ['K',10],['L',11],['M',12],['N',13],['O',14],
                    ['P',15],['Q',16],['R',17],['S',18],['T',19],
                    ['U',20],['V',21]
                ]
            )
        ]
        return rsa_model

    def test_rsa(self, rsa_model: RsaModel):
        for rsa_solver in rsa_model.list:

            mcd = self.congruence_solver.mcd(rsa_solver.a, rsa_solver.b)





        return rsa_model

