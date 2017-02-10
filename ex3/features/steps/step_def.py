# -*- coding: utf-8 -*-
"""Scenario step definitions."""

from behave import given
from behave import when
from behave import then

from step_impl import springer_link_is_reachable
from step_impl import csv_search
from step_impl import check_content_type


@given('that Springer Link is reachable')
def step_springer_link_is_reachable(context):
    springer_link_is_reachable(context)


@when('an unauthenticated user searches for any content type with "{keywords}"')
def step_csv_search(context, keywords):
    csv_search(context, keywords, content_type=None)


@when('an unauthenticated user searches for "{content_type}" with "{keywords}"')
def step_csv_search(context, keywords, content_type):
    csv_search(context, keywords, content_type)


@then('the results should contain all kinds of content types')
def step_check_content_type(context):
    check_content_type(context, content_type=None)


@then('the results should only contain "{content_type}" content-type')
def step_check_content_type(context, content_type):
    check_content_type(context, content_type)
