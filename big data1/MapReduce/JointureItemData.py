""" Programme pour faire la jointure de u.Item et u.data et afficher pour chaque film, son titre et ses évaluations"""
from mrjob.job import MRJob
from mrjob.step import MRStep

class JointureItemdata(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_evaluations,
                   reducer=self.reducer_compte_evaluations)       ]

#lecture des fichiers u.item et u.data dans cet ordre
    def mapper_get_evaluations(self, _, line):
        
        #est-ce une ligne u.item
        if "|" in line:
            colonnes = line.split("|")
            film = colonnes[0]
            titre = colonnes[1]
            yield film, titre
        else: #c'est une ligne data
            colonnes = line.split("\t")
            film = colonnes[1]
            eval = colonnes[2]
            yield film, eval
        
#calculer le nombre d'évaluations pour chaque film
    def reducer_compte_evaluations(self, film, titresEvals):
           titresEvals = [x for x in titresEvals]
           yield film, titresEvals

# on voudrait modifier ce programme pour afficher des lignes composées uniquement de deux colonnes, 
# une colonne pour le titre du film et une colonne pour l'évaluation

if __name__ == '__main__':
    JointureItemdata.run()
