# coding: utf-8
import os
import csv
import logging

logger = logging.getLogger(__name__)

_CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
JOURNALS = {}

CURRENT_METRICS = '2016'

with open(_CURRENT_DIR + '/data/google_metrics_h5m5.csv', 'r') as metrics:
    spamreader = csv.reader(metrics, delimiter=',', quotechar='"')
    for line in spamreader:
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


def get_metrics(issn, year=None):
    """
        issn: journal issn,
        year: indicator year
    """

    data = JOURNALS.get(issn, None)

    if data and year:
        return data.get(year, None)

    return data


def get_current_metrics(issn):
    """
        This method will retrive the current H5M5 metric. It means the last year
        the H5M5 indicators were produced by Google Scholar.
        issn: journal issn
    """
    return get_metrics(issn, CURRENT_METRICS)


def get(issn, year=None):
    from warnings import warn
    warn("method get is deprecated, use get_metrics instead.")

    return get_metrics(issn, year)
