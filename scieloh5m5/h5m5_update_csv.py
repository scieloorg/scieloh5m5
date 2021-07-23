import os
import csv
import argparse
import logging
from datetime import datetime
import shutil


def get_data(file_path):
    with open(file_path, 'r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            for issn in row['ISSN'].split(','):
                yield {
                    'issn': issn.upper(),
                    'year': datetime.now().isoformat()[:4],
                    'title': row['Title'],
                    'h5': row['H5-index'],
                    'm5': row['H5-median'],
                    'url': row['URL']}


def get_rows(input_file_paths):
    for file_path in input_file_paths:
        for row in get_data(file_path):
            yield ",".join(list(row.values()))


def write_journal_url(output_folder_path, input_folder_path):
    # csv provided by Google Scholar
    input_file_paths = [
        os.path.join(input_folder_path, filename)
        for filename in os.listdir(input_folder_path)
    ]
    # output dir
    output_folder_path = os.path.join(
        output_folder_path, 'github.com', 'scieloorg')
    if not os.path.isdir(output_folder_path):
        os.makedirs(output_folder_path)

    # Web/htdocs/google_metrics/journals_url.csv
    web_path = os.path.join(
        output_folder_path, 'Web', 'htdocs', 'google_metrics')
    if not os.path.isdir(web_path):
        os.makedirs(web_path)

    # journals_url.csv
    journals_url_file_path = os.path.join(web_path, "journals_url.csv")

    # scieloh5m5/scieloh5m5/data/google_metrics_h5m5.csv
    scieloh5m5_path = os.path.join(
        output_folder_path, 'scieloh5m5', 'scieloh5m5', 'data')
    if not os.path.isdir(scieloh5m5_path):
        os.makedirs(scieloh5m5_path)

    # google_metrics_h5m5.csv
    scieloh5m5_file_path = os.path.join(
        scieloh5m5_path, "google_metrics_h5m5.csv")

    sorted_rows = sorted(get_rows(input_file_paths))
    content = "\n".join(sorted_rows) + "\n"
    with open(scieloh5m5_file_path, 'w') as outfile:
        outfile.write(content)

    with open(journals_url_file_path, 'w') as outfile:
        outfile.write('issn,year,title,h5,m5,url\n')
        outfile.write(content)


def main():

    parser = argparse.ArgumentParser(description='H5M5 update csv cli utility')
    parser.add_argument(
        '--input_folder_path',
        default='input',
        help='folder which contains CSV files provided by Google Scholar')
    parser.add_argument(
        '--output_folder_path',
        default='output',
        help='output CSV file path')

    parser.add_argument('--loglevel', default='WARNING')
    args = parser.parse_args()

    logging.basicConfig(level=getattr(logging, args.loglevel.upper()))
    try:
        f = os.listdir(args.input_folder_path)
        if not f:
            raise ValueError(
                f"{args.input_folder_path} is invalid because it is an empty folder")
        if not args.output_folder_path:
            raise ValueError(f"{args.output_folder_path} is not a file path")
    except TypeError:
        print(f"{args.input_folder_path} is not a folder")
    except ValueError as e:
        print(e)
    else:
        write_journal_url(args.output_folder_path, args.input_folder_path)
        print(f"Created: {args.input_folder_path}")


if __name__ == '__main__':
    main()
