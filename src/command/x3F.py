
class x3F:
    def commands(self, args):
        if len(args) ==  0 : return "No arguments"
        else: return args

if __name__ == "__main__":
    print(x3F().commands('a', 'b', 'c', 'd', 'e'))
    print(x3F().commands('1', '2', '3', '4', '5'))
