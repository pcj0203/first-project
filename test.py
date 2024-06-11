def gugudan(dan):
    print(f"{dan}단을 출력합니다:")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan*i}")

if __name__ == "__main__":
    while True:
        try:
            dan = int(input("구구단을 출력할 단을 입력하세요 (1부터 9까지의 정수): "))
            if dan < 1 or dan > 9:
                raise ValueError("1부터 9 사이의 정수를 입력해주세요.")
            gugudan(dan)
            break
        except ValueError as ve:
            print(ve)
