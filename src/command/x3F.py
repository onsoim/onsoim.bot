
class x3F:
    def __init__(self):
        self.dName  = 'data/0x3F.json'

        import json
        with open(self.dName) as f:
            self.Jx3F = json.load(f)

    def commands(self, args):
        if len(args) ==  0 : return "No arguments"
        elif args[0] == 'l': return self.get_list()
        else: return args

    def get_list(self):
        msg, index = "", 0
        for l in self.Jx3F['lists']:
            index += 1
            msg += f'{index}. {l}\n'
        return msg[:-1]


if __name__ == "__main__":
    print("('l')")
    print(x3F().commands('l'))
