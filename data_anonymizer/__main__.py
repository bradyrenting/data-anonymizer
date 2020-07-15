import sys
import os.path
import argparse
import data_anonymizer as data
from .ConfigReader import config
from .Gui import gui


def add_arguments(parser):
    parser.add_argument('-c', '--config', dest='configfile',
                        help="Configuration file")
    parser.add_argument('-i', '--input', dest='inputfile',
                        help="SQL dump from database")
    parser.add_argument('-o', '--output', dest='outputfile',
                        help="Anonymized SQL dump")
    parser.add_argument('-g', '--gui', dest='gui', action='store_true',
                        help="Start GUI")
    parser.add_argument('--host', dest='host')
    parser.add_argument('--user', dest='username')
    parser.add_argument('--pass', dest='password')
    parser.add_argument('--db', dest='database')

    return parser.parse_args()


def validate_file(infile, configfile):
    if not os.path.isfile(infile):
        print(str(infile) + " is not a valid file")
        sys.exit()
    if not os.path.isfile(configfile):
        print(str(configfile) + " is not a valid file")
        sys.exit()


def anonymize(configfile):
    config_reader = config(open(configfile, 'r'))
    host = config_reader.storage()['host']
    username = config_reader.storage()['username']
    password = config_reader.storage()['password']
    database = config_reader.storage()['database']

    anonymizer = data.Anonymize(host=host, username=username,
                                password=password, database=database,
                                configfile=configfile, infile=infile,
                                outfile=outfile)
    anonymizer.populate_database()
    anonymizer.anonymize_database()
    anonymizer.export_database()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='python -m data_anonymizer')
    args = add_arguments(parser)

    if args.gui:
        storage = [args.host, args.username, args.password, args.database, args.inputfile]

        if args.configfile:
            configReader = config(open(args.configfile, 'r'))
            storage = configReader.storage()
            validate = [args.inputfile]

            if all(v is None for v in validate):
                parser.error("Not all arguments defined")
                sys.exit()

            gui(storage['host'], storage['username'], storage['password'], storage['database'],
                args.inputfile, args.configfile)
        else:
            if all(v is None for v in storage):
                parser.error("Not all arguments defined")
                sys.exit()

            gui(args.host, args.username, args.password, args.database, args.inputfile, args.configfile)
    elif args.configfile:

        if args.inputfile is None or args.outputfile is None:
            parser.error("Not all arguments defined")
            sys.exit()

        configfile = args.configfile
        infile = args.inputfile
        outfile = args.outputfile

        validate_file(infile, configfile)
        anonymize(configfile)
    else:
        parser.error("Select either config file (-c/--config) or GUI (-g/--gui)")
        sys.exit()
