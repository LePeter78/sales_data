import reader
import transform
import writer
import queries

def menu_app(data):
    choice = -1
    while not choice == 0:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
        print("Choose an option:")
        print()
        print("1: load csv file")
        print("2: view total revenue")
        print("3: view revenue of each category")
        print("4: view top customer")
        print("5: view top product")
        print()
        print("0: exit")
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        choice = int(input())

        if data == [] and not choice == 1:
            print("No data loaded!")
            continue
    
        match choice:
            case 1:
                while True:
                    path = read_file_path("reading raw data")
                    try:
                        data = reader.read_csv(path)
                    except:
                        print("Invalid path!")
                        continue
                    else:
                        break

                data = transform.transform_data(data)

                path = read_file_path("storing data")
                writer.write_data(data, path)
            case 2:
                queries.total_sales(data)
            case 3:
                queries.sales_by_category(data)
            case 4:
                queries.top_customer(data)
            case 5:
                queries.top_product(data)
            case _:
                if not choice == 0: print("invalid number")

def read_file_path(message):
    path = input(f"Select file path for {message}: ")
    return path