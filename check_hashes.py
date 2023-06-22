import hash_info
import HashTypeObj


class HashChecker:
    """
    Call this with an input to identify hashes
    """

    def __init__(self, nth):
        self.hashinfo_obj = hash_info.HashInformation()
        self.nth = nth
        self.output = []

    def file_input(self, f):
        for nr, line in enumerate(f, start=1):
            line = str(line).strip()
            if not line:
                print(f"Skipped empty line {nr}")
                continue
            self.single_hash(line)
            print(f"{self.output}")

    def single_hash(self, chash: str):
        self.output.append(HashTypeObj.HashType(chash, self.nth, self.hashinfo_obj))
