
import json


class x3F:
    def __init__(self):
        self.dName  = 'data/0x3F.json'

        with open(self.dName) as f:
            self.Jx3F = json.load(f)

    def commands(self, args):
        if len(args) ==  0 : return "No arguments"
        elif args[0] == 'd': return self.set_deleted(int(args[1]))
        elif args[0] == 'l': return self.get_list()
        elif args[0] == 'u': return self.get_unwatched()
        elif args[0] == 'w': return self.set_watched(args[1:])
        else: return args

    def get_list(self):
        msg, index = "", 0
        for l in self.Jx3F['lists']:
            index += 1
            msg += f'> {index}. {l}\n'
        return msg[:-1]

    def get_unwatched(self):
        msg, index = "", 0
        ls = self.Jx3F['lists']
        for l in ls:
            if len(ls[l]['U']):
                index += 1
                msg += f'**{index}. {l}**\n'
                for ep in ls[l]['U']:
                    msg += f'> EP.{ep}\n'
                msg += '\n'
        return msg[:-1]

    def set_deleted(self, index):
        res, i = "Fail", 0
        for l in self.Jx3F['lists']:
            i += 1
            if i == index:
                self.Jx3F['lists'].pop(l)
                self.set_json(self.Jx3F)
                res, index = "Success", l
                break
        return f"{self.get_list()}\n**[{res}] to delete \"{index}\"**"

    def set_json(self, data):
        with open(self.dName, "w") as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

    def set_watched(self, args):
        ls = self.Jx3F['lists']

        if len(args) != 2:
            msg = ""
            for l in ls:
                W = ls[l]['W']
                if len(W):
                    msg += f'{l}\n'
                    for ep in W:
                        msg += f'> EP.{ep}\n> =TEXTJOIN(", ", "True", TEXT(DATE({W[ep][0]},{W[ep][1]},{W[ep][2]}),"yyyy/mm/dd/[$-ko-KR]ddd"))\n'
                    msg += '\n'
            return msg
        else:
            index, ep = int(args[0]), int(args[1])
            res, i = "Fail", 0
            for l in ls:
                U = ls[l]['U']
                if len(U):
                    i += 1
                    if i == index:
                        if ep in U:
                            U.remove(ep)
                            from datetime import date
                            today = date.today()
                            ls[l]['W'][str(ep)] = [today.year, today.month, today.day]
                            self.set_json(self.Jx3F)
                            res = "Success"
                        break
            return f"**[{res}] to set {l} EP.{ep} watched**\n{self.get_unwatched()}"


if __name__ == "__main__":
    print("('l')")
    print(x3F().commands(('l')))

    print("('d', '4')")
    print(x3F().commands(('d', '4')))
