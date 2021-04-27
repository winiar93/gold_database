from optparse import OptionParser

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--fetch_data", dest="fetch_data", action="store_true")
    parser.add_option("-s", "--save_to_db", dest="save_to_db", action="store_true")
    parser.add_option("-d", "--display_data", dest="display_data", action="store_true")
    parser.add_option("-c", "--show_chart", dest="show_chart", action="store_true")

    options, args = parser.parse_args()
    if options.fetch_data:
        print("Fetching data")
    if options.save_to_db:
        print("Saving data to db")
    if options.display_data:
        print("Show data in console.")
    if options.show_chart:
        print("Show chart.")