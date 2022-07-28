
import json
import os

from game.score import Score

class ConfigManager:

    score_file_path = "gamescore.json"

    def __init__(self) -> None:
        
        self.score_file = self.get_score_file()

        self.score_data = []
        
        self.get_score_data()

        

        # Example of score file
        file = [
            {
                "name": "Daniel",
                "bestscores": {
                    "3": 21,
                    "4": 0,
                    "5": 0,
                    "6": 0
                }
            }
        ]

        json_ = json.dumps(file)


        arr = json.loads(json_)

    def update_score(self, username, rings_amount, num_of_movements):

        for score in self.score_data:
            if(score.name == username):
                bestcore = score.bestscores[str(rings_amount)]

                if(bestcore == 0 or num_of_movements < bestcore):
                    score.bestscores[str(rings_amount)] = num_of_movements

    def check_name(self, username):

        for score in self.score_data:
            if(score.name == username):
                return True
        
        self.score_data.append(Score(username, {"3": 0, "4": 0, "5": 0, "6": 0}))
        return False
                
    # Get score file and check if exists
    def get_score_file(self):

        # If the file didn't exists, we open in write mode
        open_mode = "r+" if os.path.exists(self.score_file_path) else "w+"

        return open(self.score_file_path, open_mode)

    # Read the score file content
    def read_score_file(self):
        if(self.score_file):

            lines = self.score_file.readlines()

            if(len(lines) > 0):
                return lines[0] # Return just the first line

        return []

    # Return the last 10 collocated in ascending order
    def get_score_by_rings_amount(self, rings):

        list = []

        for i,score in enumerate(self.score_data):

            if(i >= 10):
                break

            scr = score.get_score_ring(rings)

            if(scr != 0):
                list.append((score.name, scr))

        # Sorting
        return sorted(list, key=lambda x: x[1], reverse=False)


    #newlist = sorted(ut, key=lambda x: x.count, reverse=True)
    # Read the file and save in the memory all the scores
    def get_score_data(self):

        list = self.read_score_file()

        if(len(list) == 0):
            return

        data_array = json.loads(list)

        for data in data_array:
            self.score_data.append(Score(data["name"], data["bestscores"]))

    # Save the score of the memory in the file
    def save_score_data(self):
        
        object = []

        for score in self.score_data:
            object.append({"name": score.name, "bestscores": score.bestscores})

        self.score_file.seek(0)
        self.score_file.write(json.dumps(object))
        self.score_file.truncate()
