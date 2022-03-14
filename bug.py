
class Bug():
    genes = []
    fitness = 0

    def __init__(self, genes):
        self.genes = genes

    def build_body(self):
        body = ""
        for gene in self.genes:
            body += gene.value
        return body
class BodyMaterial():
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Fat(BodyMaterial):
    pass
