from model import Student

def main():
    s1 = Student("Иванов И.И.", "ИКБО-23-23", 95, 90)
    s2 = Student("Петрова П.П.", "ИКБО-23-23", 70, 80)
    s3 = Student("Сидоров С.С.", "ИКБО-23-23", 50, 55)

    print(s1)
    print("-" * 40)
    print(s2)
    print("-" * 40)
    print(s3)

if __name__ == "__main__":
    main()