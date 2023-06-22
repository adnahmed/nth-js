class Name_That_Hash:
    """
    The main class which deals with hash identification
    """

    def __init__(self, prototypes: list):
        self.prototypes = list(prototypes)

    def identify(self, chash: str):
        # console.log(chash)
        chash = chash.strip()
        output = []
        for prototype in self.prototypes:
            if prototype.regex.match(chash):
                for mode in prototype.modes:
                    output.append(mode)
        return output

    def identify_all(self, chash: str):
        # console.log(f"In identify all with {chash}")
        chash = chash.strip()
        output = []
        for prototype in self.prototypes:
            if prototype.regex.findall(chash):
                # console.log(f"Found all matched a regex {prototype.regex}")
                for mode in prototype.modes:
                    output.append(mode)
        return output
