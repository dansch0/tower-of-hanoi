
import json
import os

class ConfigManager:

    score_file_path = "gamescore.json"

    def __init__(self) -> None:
        
        self.score_file = self.get_score_file()
        

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

    
    # Get score file and check if exists
    def get_score_file(self):

        # If the file didn't exists, we open in write mode
        open_mode = "r+" if os.path.exists(self.score_file_path) else "w+"

        return open(self.score_file_path, open_mode)

    # Read the score file content
    def read_score_file(self):
        if(self.score_file):
            return self.score_file.readlines()

        return []

    def get_score_data(self):
        pass

    def save_score_data(self):
        pass