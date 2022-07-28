
class Score:

    def __init__(self, name, bestscores) -> None:
        self.name = name
        self.bestscores = bestscores

    def get_score_ring(self, ring):
        return self.bestscores[str(ring)]