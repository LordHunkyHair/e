def main():
    for number in range(1,100):
        mod = 1
        for mod in range(2,number+1):
            if number % mod > 0:
                continue
            if number % mod == 0 and number != mod:
                break
            else:
                    print(number)
main()