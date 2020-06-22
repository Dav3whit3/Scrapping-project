import argparse
from p_scrapping import m_scrapp_events


def argument_parser():
    parser = argparse.ArgumentParser(description='specify input file and api key')
    parser.add_argument("-u", "--url", type=str, help='specify url', required=True)
    #parser.add_argument("-p", "--path", type=str, help='specify path to deploy csv', required=True)
    args = parser.parse_args()

    return args


def main(args):
    print("starting the tkus scrap!!!")

    m_scrapp_events.info_to_df(arguments.url)

    print("Tkus scrapp finished! X hackatones inserted in WEB")

if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments)
