
import json


class SCRAPER:
    def get_new(self):
        return self.new

    def get_json(self):
        with open(self.dName) as f:
            return json.load(f)
 
    def set_json(self, data):
        with open(self.dName, "w") as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )
