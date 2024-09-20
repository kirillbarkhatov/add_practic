def get_sqr_list_div_by_3():
    return [i**2 for i in range(1, 11) if i**2 % 3 == 0]


if __name__ == "__main__":
    print(get_sqr_list_div_by_3())
