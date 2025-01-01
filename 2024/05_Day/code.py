import unittest

# Helper Functions and Solutions


def get_input(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def format_input(input_data):
    rules, updates = input_data.strip().split("\n\n")

    rules = [
        {"left": int(line.split('|')[0]), "right": int(line.split('|')[1])}
        for line in rules.split('\n')
    ]

    updates = [
        list(map(int, line.split(','))) for line in updates.split('\n')
    ]

    return {"rules": rules, "updates": updates}


def index_rules(rules):
    result = {}

    for rule in rules:
        left, right = rule["left"], rule["right"]

        if left not in result:
            result[left] = set()

        result[left].add(right)

    return result


def validate_update(update, rules_index):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            left, right = update[i], update[j]

            if right not in rules_index.get(left, set()):
                return False

    return True


def get_middle(arr):
    return arr[len(arr) // 2]


def solution1(input_data):
    data = format_input(input_data)
    rules = data["rules"]
    updates = data["updates"]

    rules_index = index_rules(rules)

    valid_updates = [
        update for update in updates if validate_update(update, rules_index)]

    middles = [get_middle(update) for update in valid_updates]

    return sum(middles)


def fix_update(update, rules_index):
    return sorted(update, key=lambda x: [1 if x in rules_index and y in rules_index[x] else -1 for y in update])


def solution2(input_data):
    data = format_input(input_data)
    rules = data["rules"]
    updates = data["updates"]

    rules_index = index_rules(rules)

    invalid_updates = [
        update for update in updates if not validate_update(update, rules_index)]

    fixed_updates = [fix_update(update, rules_index)
                     for update in invalid_updates]

    middles = [get_middle(update) for update in fixed_updates]

    return sum(middles)



class TestSolutions(unittest.TestCase):

    def setUp(self):
        self.input_data = get_input('input.txt')

    def test_solution1(self):

        result = solution1(self.input_data)
        print(result)

    def test_solution2(self):

        result = solution2(self.input_data)
        print(result)

if __name__ == "__main__":
    unittest.main()
