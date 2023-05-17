def main():
    num_name = int(input())
    name_list = []
    for i in range(num_name):
        name = input()
        name_list.append(name)
    
    for name in name_list:
        print('Hello, ' + name + '!')

main()