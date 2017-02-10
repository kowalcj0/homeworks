# -*- coding: utf-8 -*-
"""Scenario step implementations."""

import csv
import logging
from contextlib import closing
from pprint import pformat

import requests


def springer_link_is_reachable(context):
    """Check if springer link endpoint is reachable.

    :param context: Behave context object.
    :raises requests.ConnectionError: when the URL is not reachable
    """
    try:
        requests.get(context.platform_url, timeout=context.request_timeout)
        logging.debug("Springer Link is reachable".format(context.platform_url))
    except requests.ConnectionError:
        raise requests.ConnectionError('Unable to connect to the test URL {} -'
                ' please ensure that Springer Link is reachable'
                .format(context.platform_url))


def csv_search(context, keywords, content_type):
    """Search using specific keywords and return results as CSV.

    Will save the response to the context.result

    :param context: Behave context object.
    :param term: search keywords
    :param content_type: expected result content-type eg. Journal, Book etc.
    :return: a list of dictonaries with search results
    """
    ct = '&facet-content-type="{}"'.format(content_type) if content_type else ''
    url = '{}{}{}'.format(context.test_url, keywords, ct)
    response = requests.get(url, timeout=context.request_timeout, stream=True)
    context.response = response
    logging.debug('Request URL: %s', response.request.url)
    logging.debug('Request headers:\n%s', pformat(response.request.headers))
    logging.debug('Response headers:\n%s', pformat(response.headers))

    with closing(response) as r:
        reader = csv.reader(r.iter_lines(), delimiter=',', quotechar='"')
	header = next(reader)
	res = [dict(zip(header, map(str, row))) for row in reader]

    context.result = res
    logging.debug("First 5 search results:\n{}".format(pformat(res[:5])))
    return res


def check_content_type(context, content_type):
    """Will check the content type of the search results.

    If content_type is None, then it will check whether results contain more
    than one type of content-type.

    :param: content_type: None or a predefined content-type, eg. Book, etc.
    """
    if content_type:
        resp_contains_only_one_content_type(context.result, content_type)
    else:
        resp_contains_various_content_type(context.result)


def resp_contains_various_content_type(result):
    """Check whether search results contain documents of various types."""
    types = set()
    for res in result:
        types.add(res['Content Type'])
    assert len(types) > 1, ('Expected that the search results will contain '
                            'more than 1 content-type but got only 1: {}'
                            .format(types))


def resp_contains_only_one_content_type(result, content_type):
    """Check whether search results contain documents of only one type."""
    assert content_type
    failed = []
    for res in result:
        if res['Content Type'] != content_type:
            failed.append(res)
    assert not failed, ('Expected that the search results will only contain '
                        '"{}s" but also got: {}'.format(
                            content_type, ', '.join(failed)))
