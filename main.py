import random
PATH: str = "KORDAMINE.txt"
def get_random_numbers(number_of_qu: int)->list[int]:
    random.seed()
    list_q: list[int] = []
    if number_of_qu == 45:
        return list(range(1, 46))
    for i in range(number_of_qu):
        random_number = random.randint(1,46)
        list_q.append(random_number)
    list_q.sort()
    return list_q

def get_questions(questions: list[int]):
    count: int = 0
    i: int = 0
    with open(PATH, "rt", encoding = "UTF-8") as f:
        for line in f:
            if "*" in line:
                count +=1
                if count in questions:
                    print(f"{count})", line)
                    input("")
                    print("Lahendus:")
            if "*" not in line and count in questions:
                print(line, end='')

def input_number()->int:
    while True:
        try:
            number: int = int(input("Sisesta küsimuste arv(max = 45): "))
            if number <= 0 or number >45:
                raise ValueError
        except ValueError:
            print("Ei ole kehtiv number, proovi uuesti: ")
        else:
            break
    return number

if __name__ == "__main__":
    number_of_q:int = input_number()
    get_questions(get_random_numbers(number_of_q))
