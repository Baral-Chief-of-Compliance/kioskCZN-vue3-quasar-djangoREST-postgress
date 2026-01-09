from parser import WorkeParser


def main():
    print("Hello from czn-worker-parser!")

    wp = WorkeParser('','','')
    wp.get_test_data()
    print(wp.get_departments_name())




if __name__ == "__main__":
    main()
