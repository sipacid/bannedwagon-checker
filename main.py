import itertools
import requests
import threading

BASE_URL = 'https://bannedwagon.team/codes/'
LETTERS = ['Q', 'H', 'O', 'C', 'D', 'I', 'P']
CODE_LENGTH = 5
FOUND = []


def generate_combinations(letters) -> list[str]:
    combinations = []
    for i in itertools.product(letters, repeat=CODE_LENGTH):
        combinations.append(''.join(map(str, i)))
    return combinations


def check_combination(combination: str) -> int:
    response = requests.get(BASE_URL + combination)
    print(combination + ' - ' + str(response.status_code))
    if response.status_code == 200:
        FOUND.append(combination)
        with (open('found.txt', 'a')) as f:
            f.write(combination + '\n')
    return response.status_code


def main():
    combinations = generate_combinations(LETTERS)
    threads = []

    for combination in combinations:
        thread = threading.Thread(
            target=check_combination, args=(combination,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        print(f'Found {len(FOUND)} codes: {FOUND}')
    return


if __name__ == '__main__':
    main()
