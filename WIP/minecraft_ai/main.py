from typing import List

class seed(object):
    def __init__(self, seed: int, worldType: int) -> None:
        self.seed = seed
        self.worldType = worldType

class _seeds(object):
    def __init__(self) -> None:
        self.seeds: List[seed] = list()
    
    def get_mountain_seeds(self) -> List[seed]:
        mountain_seeds = []
        for i in range(len(self.seeds)):
            if self.seeds[i].worldType == 0: mountain_seeds.append(self.seeds[i])
            else: continue
        
        return mountain_seeds

    def parse_seed(self, data: str) -> seed:
        new_data = data.strip().split(",")
        return seed(int(new_data[1]), int(new_data[0]))
    
    def __str__(self) -> List[seed]:
        return self.seeds

seeds = _seeds()


with open("data/seed_table.csv", "r") as file:
    buffer_data: List[str] = seeds.parse_seed(file.readline())


    while len(buffer_data) > 1:
        seeds.seeds.append(seeds.parse_seed())

        buffer_data = seeds.parse_seed(file.readline())

print(seeds.get_mountain_seeds())
