import check_hashes
import hash_namer
import hashes


def main(kwargs):
    print("Called main ")
    # nth = the object which names the hash types
    nth = hash_namer.Name_That_Hash(hashes.prototypes)
    hashChecker = check_hashes.HashChecker(nth)
    output = []
    # Check textarea and file and use as specified
    textarea = document.getElementById("hashlist")
    file_input = document.getElementById("hashlist_file")
    if textarea.value.length > 0:
        hashChecker.single_hash(textarea.value)
        output = hashChecker.output
    elif file_input.value.length > 0:
        hashChecker.file_input(file_input.value)
        output = hashChecker.output
    print(output)


def turn_hash_objs_into_dict(objs):
    outputs_as_dict = {}
    for y in objs:
        outputs_as_dict.update(y.hash_obj)
    return outputs_as_dict


def greppable_output(objs):
    return turn_hash_objs_into_dict(objs)


def api_return_hashes_as_json(chash):
    return greppable_output(compute_hashes_for_api(chash))


def compute_hashes_for_api(chash):
    # nth = the object which names the hash types
    nth = hash_namer.Name_That_Hash(hashes.prototypes)
    hashChecker = check_hashes.HashChecker(nth)
    for i in chash:
        hashChecker.single_hash(i)
    return hashChecker.output


submit = document.getElementById("submit")
submit.addEventListener("click", main)
