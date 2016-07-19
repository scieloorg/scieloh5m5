# coding: utf-8
import os
import codecs
import csv
import logging

logger = logging.getLogger(__name__)

_CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
JOURNALS = {}


with codecs.open(_CURRENT_DIR + '/data/google_metrics_h5m5.csv', 'r') as metrics:
    spamreader = csv.reader(metrics, delimiter=',', quotechar='"')
    for line in spamreader:
        line = [i.decode('utf-8') for i in line]
        issn = line[0].upper()
        year = line[1]
        h5 = line[3]
        m5 = line[4]
        url = line[5]
        j = JOURNALS.setdefault(issn, {})

        JOURNALS[issn][year] = {
            'h5': h5,
            'm5': m5,
            'url': url
        }


def get(issn, year=None):
    """
        issn: journal issn,
        year: indicator year
    """

    data = JOURNALS.get(issn, None)

    if data and year:
        return data.get(year, None)

    return data
