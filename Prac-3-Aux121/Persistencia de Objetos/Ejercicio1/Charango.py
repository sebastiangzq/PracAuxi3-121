import json

class Charango:
    def __init__(self, material, nroCuerdas, cuerdas):
        self.material = material
        self.nroCuerdas = nroCuerdas
        self.cuerdas = cuerdas  

    def to_dict(self):
        return {
            "material": self.material,
            "nroCuerdas": self.nroCuerdas,
            "cuerdas": self.cuerdas
        }

    @staticmethod
    def from_dict(d):
        return Charango(d["material"], d["nroCuerdas"], d["cuerdas"])