def adding_list_nums(list: list[int]):
    total = 0
    for num in list:
        total+=num
    return total
    
def main():
    print(adding_list_nums([1,2,3,4,5,6])) # 21
    
if __name__ == '__main__':
    main()