
import json


class ConfigManager:

    score_file_path = "gamescore.cfg"

    def __init__(self) -> None:
    

        # Example of score file
        file = [
            {
                "name": "Daniel",
                "bestscores": {
                    "3": 300,
                    "4": 0,
                    "5": 0,
                    "6": 0
                }
            }
        ]

        json_ = json.dumps(file)

        print(json_)

        arr = json.loads(json_)

        print(arr[0]["name"])
    
    # Read all lines of score file
    def read_score_file(self):
        return open(self.score_file_path).readlines()