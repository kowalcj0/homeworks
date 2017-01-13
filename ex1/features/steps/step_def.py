# -*- coding: utf-8 -*-
"""Scenario step definitions."""

from behave import given
from behave import when
from behave import then

from step_impl import compare_original_response_with_copy
from step_impl import copy_response
from step_impl import every_existing_owner_should_have_valid_profile_image_link
from step_impl import every_existing_owner_should_have_valid_profile_link
from step_impl import every_non_existing_owner_should_not_have_profile_image_link
from step_impl import every_non_existing_owner_should_not_have_profile_link
from step_impl import get_activity_feed
from step_impl import items_should_contain_array_of_tags
from step_impl import items_should_contain_owner_object
from step_impl import items_should_contain_required_values
from step_impl import remove_field_from_every_item_in_response_copy
from step_impl import replace_field_value_in_every_item_in_response_copy
from step_impl import response_contains_array_named
from step_impl import response_contains_meta_data
from step_impl import save_tags
from step_impl import stack_exchange_is_reachable
from step_impl import tags_list_should_have_no_duplicates

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


@when('we save the tags from the response to a list and remove the duplicates')
def step_save_tags(context):
    save_tags(context)


@then('we should have a list of tags without duplicates')
def step_tags_list_shoul_have_no_duplicates(context):
    tags_list_should_have_no_duplicates(context)


@when('we create a copy of the response')
def step_copy_response(context):
    copy_response(context)


@when('we replace the value of field "{name}" in every item of the response copy with "{value}"')
def step_replace_field_value_in_every_item_in_response_copy(context, name, value):
    replace_field_value_in_every_item_in_response_copy(context, name, value)


@when('we remove the field "{name}" from every item of the response copy')
def step_remove_field_from_every_item_in_response_copy(context, name):
    remove_field_from_every_item_in_response_copy(context, name)


@then('the original response and the copy should be identical except for title and last_activity_date values')
def step_compare_original_response_with_copy(context):
    compare_original_response_with_copy(context)
