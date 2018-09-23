def main():
    numbers = [2,4,6,8,10]

    sum = get_total(numbers)

    print("The total is" , sum)

def get_total(value_list):
    total = 0

    for num in value_list:
        total += num
    return total
main()
