def times(number_list):
    sum_value = 1
    for number in number_list:
        sum_value *= number
    return sum_value

def main():
    numbers = input("곱할 숫자들을 공백으로 구분하여 입력하세요: ")
    if numbers.strip() == "":
        print("입력값이 비어 있습니다.")
        return
    number_list = map(float, numbers.split())
    result = times(number_list)
    print(result, "입니다")
if __name__ == "__main__":
    main()