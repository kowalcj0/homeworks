# -*- coding: utf-8 -*-
"""Behave configuration file."""

import os
import logging

import requests
import pprint


def before_scenario(context, scenario):
    logging.debug('Scenario: {}'.format(scenario.name))
    # clear the stored response object before every scenario
    context.response = None


def before_step(context, step):
    logging.debug('Step: {} {}'.format(step.step_type, str(repr(step.name))))


def before_all(context):
    # API URL under test
    context.platform_url = 'http://link.springer.com/'
    context.test_url = '{}{}'.format(context.platform_url, 'search/csv?query=')

    # requests configuration
    context.request_timeout = 20

    # get the root logger
    rootLogger = logging.getLogger()

    # configure the formatter
    fmt = ('%(asctime)s-%(filename)s[line:%(lineno)d]-%(name)s-%(levelname)s: '
           '%(message)s')
    logFormatter = logging.Formatter(fmt)

    # configure the file logger
    logFile = "./reports/behave.log"
    fileHandler = logging.FileHandler(logFile)
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    # configure the console logger
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    consoleHandler.setLevel(logging.ERROR)
    rootLogger.addHandler(consoleHandler)

    # Check if the Springer Link is reachable
    try:
        requests.get(context.platform_url, timeout=context.request_timeout)
    except requests.ConnectionError:
        raise Exception(
            ('Unable to connect to the test URL {} - please ensure that '
             'Springer Link Website is reachable'.format(context.platform_url)))


def after_step(context, step):
    if step.status == "failed":
        msg = 'Step "{} {}" has failed. Reason: "{}".'.format(
            step.step_type, step.name, step.exception)
        logging.debug(msg)
