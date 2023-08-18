""" Programme pour chercher le film ayant reçu le maximum d'évaluations 5* """
from mrjob.job import MRJob
from mrjob.step import MRStep

class CompteEvaluationsFilmMaximum5Etoiles(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_evaluations,
                   reducer=self.reducer_compte_evaluations),
            MRStep(reducer=self.reducer_maximum_evaluations)       ]

    def mapper_get_evaluations(self, _, line):
         
        colonnes = line.split("\t")
        film = colonnes[1]
        eval = colonnes[2]
        if eval=="5" :
            yield film, 1

    def reducer_compte_evaluations(self, film, uns):
         yield  "clé", [sum(uns), film]

    def reducer_maximum_evaluations(self, _, evaluations):
        # transformer un générateur en une liste
        evaluations = [x for x in evaluations]
        # afficher le nombre d'évaluations et la liste des films
        yield  "Maximum est:",  max(evaluations)
if __name__ == '__main__':
    CompteEvaluationsFilmMaximum5Etoiles.run()
