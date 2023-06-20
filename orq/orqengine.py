# Third Party Imports
import clips as c # pip install clipspy
# https://clipspy.readthedocs.io/en/latest/index.html


class ORQEngine:
    def __init__(self):
        self.env = c.Environment()
        self.build_fact()
    def build_fact(self):
        fact = """(deffacts initial-fact
                    (animal dog)
                    (animal cat)
                    (animal fish)
                    (animal bird)
                    (defrule list-animals (animal ?name)=>(printout t ?name crlf))
                )"""
        self.env.build(fact)
    def build_rule(self):
        rule = """(defrule determine-gas-level
                
                )"""
    def build_template(self, name: str, slots: dict):
        template = """()"""
        self.env.build()
        
if __name__ == "__main__":
    orqe = ORQEngine()
    exit()