from jj_classes.game import Game


def main():
    smb1 = Game(yaml_file="data/smb1.yaml")
    print(smb1.characters)

if __name__ == "__main__":
    main()
