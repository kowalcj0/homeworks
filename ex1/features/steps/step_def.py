# -*- coding: utf-8 -*-
"""Scenario step definitions."""

from behave import given
from behave import when
from behave import then

from step_impl import every_existing_owner_should_have_valid_profile_image_link
from step_impl import every_existing_owner_should_have_valid_profile_link
from step_impl import every_non_existing_owner_should_not_have_profile_link
from step_impl import every_non_existing_owner_should_not_have_profile_image_link
from step_impl import get_activity_feed
from step_impl import items_should_contain_array_of_tags
from step_impl import items_should_contain_owner_object
from step_impl import items_should_contain_required_values
from step_impl import response_contains_array_named
from step_impl import response_contains_meta_data
from step_impl import stack_exchange_is_reachable


@given('that Stack Exchange API is reachable')
def step_stack_exchange_is_reachable(context):
    stack_exchange_is_reachable(context)


@when('we get the activity feed for the term "{term}"')
def step_get_activity_feed(context, term):
    get_activity_feed(context, term)


@then('the response should contain an array of items called "{array_name}"')
def step_response_contains_array_named(context, array_name):
    response_contains_array_named(context, array_name)


@then('response should contain meta data')
def step_response_contains_meta_data(context):
    response_contains_meta_data(context)


@then('every item should contain an array of tags')
def step_items_should_contain_array_of_tags(context):
    items_should_contain_array_of_tags(context)


@then('every item should contain an owner object')
def step_items_should_contain_owner_object(context):
    items_should_contain_owner_object(context)


@then('every item should contain a list of json values')
def step_items_should_contain_required_values(context):
    items_should_contain_required_values(context)


@then('every existing owner should have a valid profile link')
def step_every_existing_owner_should_have_valid_profile_link(context):
    every_existing_owner_should_have_valid_profile_link(context)


@then('every non-existing owner should not have a profile link')
def step_every_non_existing_owner_should_not_have_profile_link(context):
    every_non_existing_owner_should_not_have_profile_link(context)


@then('every existing owner should have a valid profile image link')
def step_every_existing_owner_should_have_valid_profile_image_link(context):
    every_existing_owner_should_have_valid_profile_image_link(context)


@then('every non-existing owner should not have a valid profile image link')
def step_every_non_existing_owner_should_not_have_valid_profile_image_link(context):
    every_non_existing_owner_should_not_have_profile_image_link(context)
