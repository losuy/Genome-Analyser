from Bio.Seq import Seq


class Analyser(Seq):
    def __init__(self,to_analyse):
        super().__init__(to_analyse)
        self.seq = to_analyse



    def convert_to_RNA(self):
        return Seq(self).transcribe()

    def convert_to_protein(self):

        return len(Seq(self))

    def convert_to_amino(self):
        return list(self.translate())


