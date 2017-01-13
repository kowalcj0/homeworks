# -*- coding: utf-8 -*-
"""Scenario step implementations."""

import logging
from pprint import pformat

import requests
import validators


def stack_exchange_is_reachable(context):
    """Check if Stack Exchange API is reachable.

    :param context: Behave context object.
    :raises requests.ConnectionError: when API is not reachable
    """
    try:
        requests.get(context.platform_url, timeout=context.request_timeout)
    except requests.ConnectionError:
        raise requests.ConnectionError('Unable to connect to the test URL {} -'
                ' please ensure that Stack Exchange API is reachable'
                .format(context.platform_url))


def get_activity_feed(context, term):
    """Get activity feed for a specific term.

    Will save the response to the context.response.

    :param context: Behave context object.
    :param term: search term
    :raises ValueError: if term is not provided
    """
    if not term:
        raise ValueError('You have to provide a search term!')
    url = '{}{}'.format(context.test_url, term)
    response = requests.get(url, timeout=context.request_timeout)
    context.response = response
    logging.debug('Request URL: %s', response.request.url)
    logging.debug('Request headers:\n%s', pformat(response.request.headers))
    logging.debug('Response headers:\n%s', pformat(response.headers))
    logging.debug('Response content:\n%s', pformat(response.json()))


def response_contains_array_named(context, array_name):
    """Check whether response contain an array of items of a given name.

    :param context: Behave context object.
    :param array_name: name of the array that should be present in the response
    """
    assert context.response
    response = context.response.json()
    assert array_name in response
    assert isinstance(response[array_name], list)


def response_contains_meta_data(context):
    """Check whether response contains all expected meta fields.

    :param context: Behave context object.
    """
    meta_fields = ['has_more', 'quota_max', 'quota_remaining']
    assert context.response
    response = context.response.json()
    all(field in response for field in meta_fields)
    logging.debug(
        'Response contains all expected meta fields: %s',
        ', '.join(meta_fields))


def items_should_contain_array_of_tags(context):
    """Ensure that every item in the response contains an array of tags.

    :param context: Behave context object.
    """
    items = context.response.json()['items']
    for item in items:
        assert 'tags' in item
        assert isinstance(item['tags'], list)
        assert len(item['tags']) > 0


def items_should_contain_owner_object(context):
    """Ensure that every item in the response contains a valid Owner object.

    :param context: Behave context object.
    """
    items = context.response.json()['items']
    existing_owner_fields = [
        'accept_rate', 'display_name', 'link', 'profile_image', 'reputation',
        'user_id', 'user_type'
    ]
    non_existing_owner_fields = ['display_name', 'user_type']

    for item in items:
        assert 'owner' in item
        assert isinstance(item['owner'], dict)
        owner = item['owner']
        if owner['user_type'] == 'does_not_exist':
            all(field in owner for field in non_existing_owner_fields)
            logging.debug(
                ('Item %d contains an non-existing Owner object for user "%s" '
                 'with all required fields: %s'), item['question_id'], 
                 owner['display_name'], ', '.join(non_existing_owner_fields))
        else:
            all(field in owner for field in existing_owner_fields)
            logging.debug(
                ('Item %d contains an existing Owner object for user ID "%d" '
                 'with all required fields: %s'), item['question_id'], 
                 owner['user_id'], ', '.join(existing_owner_fields))


def items_should_contain_required_values(context):
    """Ensure that every item in the response has all required fields.

    :param context: Behave context object.
    """
    items = context.response.json()['items']
    item_fields = [
        'answer_count', 'creation_date', 'is_answered', 'last_activity_date',
        'last_edit_date', 'link', 'question_id', 'score', 'title', 'view_count'
    ]
    for item in items:
        all(field in item for field in item_fields)
        logging.debug(
            'Item object ID "%d" contains all required fields: %s',
            item['question_id'], ', '.join(item_fields))


def every_existing_owner_should_have_valid_profile_link(context):
    """Ensure that every existing owner has a valid profile link.

    :param context: Behave context object.
    """
    items = context.response.json()['items']
    for item in items:
        owner = item['owner']
        if owner['user_type'] == 'does_not_exist':
            continue
        link = owner['link']
        assert validators.url(link), (
            'Owner %s (%d) in item %d has an invalid profile link: %s'.format(
                owner['display_name'], owner['user_id'], link))
        logging.debug(
            'Owner %s (%d) has a valid profile link: %s',
            owner['display_name'], owner['user_id'], link) 


def every_non_existing_owner_should_not_have_profile_link(context):
    """Ensure that every non-existing owner does not have a profile link.

    :param context: Behave context object.
    """
    items = context.response.json()['items']
    for item in items:
        owner = item['owner']
        if not owner['user_type'] == 'does_not_exist':
            continue
        assert 'link' not in owner
        logging.debug(
            'Not existing Owner %s does not have a valid profile link',
            owner['display_name']) 


def every_existing_owner_should_have_valid_profile_image_link(context):
    """Ensure that every existing owner has a valid profile image link.

    :param context: Behave context object.
    """
    items = context.response.json()['items']
    for item in items:
        owner = item['owner']
        if owner['user_type'] == 'does_not_exist':
            continue
        link = owner['profile_image']
        assert validators.url(link), (
            'Owner %s (%d) in item %d has an invalid profile image link: %s'
            .format(owner['display_name'], owner['user_id'], link))
        logging.debug(
            'Owner %s (%d) has a valid profile image link: %s',
            owner['display_name'], owner['user_id'], link) 


def every_non_existing_owner_should_not_have_profile_image_link(context):
    """Ensure that every non-existing owner does not have a profile image link.

    :param context: Behave context object.
    """
    items = context.response.json()['items']
    for item in items:
        owner = item['owner']
        if not owner['user_type'] == 'does_not_exist':
            continue
        assert 'profile_image' not in owner
        logging.debug(
            'Not existing Owner %s does not have a valid profile image link',
            owner['display_name']) 


def save_tags(context):
    """Save all the tags from the response to a list and remove the duplicates.

    :param context: Behave context object.
    """
    items = context.response.json()['items']
    tags = set()
    for item in items:
        for tag in item['tags']:
            tags.add(tag)
    context.tags = list(tags)
    logging.debug('Saved all tags in context.tags:\n%s', pformat(sorted(context.tags)))


def tags_list_should_have_no_duplicates(context):
    """Ensure that we have a list of tags without duplicates.

    :param context: Behave context object.
    """
    assert context.tags
    # converting a list to a set will remove all the duplicates
    # then we need to:
    # * convert it back to a list
    # * sort both lists
    # and finally compare both lists
    unique_tags = list(set(context.tags))
    assert sorted(context.tags) == sorted(unique_tags)
    logging.debug(
        'Saved list of all tags does not contain duplicates:\n%s',
        pformat(sorted(context.tags)))


def copy_response(context):
    """Save a copy of the response JSON in context.response_copy

    :param context: Behave context object.
    """
    context.response_copy = context.response.json()
    logging.debug('Successfully copied the response')


def remove_field_from_every_item_in_response_copy(context, name):
    """Remove selected field from all items created by existing owners.

    :param context: Behave context object.
    :param name: name of the field to be deleted.
    """
    items = context.response_copy['items']
    for item in items:
        print(item)
        if item['owner']['user_type'] == 'does_not_exist':
            continue
        if name in item:
            del(item[name])
            logging.debug(
                'Successfully removed field "%s" from item: %s', name,
                item['question_id']) 
        else:
            logging.debug(
                'Item %s does not contain field "%s', name, item) 
    logging.debug(
        'Response copy after removing "%s" field:\n%s', name,
        pformat(context.response_copy))


def replace_field_value_in_every_item_in_response_copy(context, name, value):
    """Replace value of selected field in all items with provided value.

    It will skip items created by non-existing owners. 

    :param context: Behave context object.
    :param name: name of the field.
    :param value: new value of the field.
    """
    items = context.response_copy['items']
    for item in items:
        print(item)
        if item['owner']['user_type'] == 'does_not_exist':
            continue
        if name in item:
            item[name] = value
            logging.debug(
                'Successfully replaced value of field "%s" in item: %s with %s',
                name, item['question_id'], value) 
        else:
            logging.debug(
                'Item %s does not contain field "%s', name, item) 
    logging.debug(
        'Response copy after replacing values of all "%s" fields with %s:\n%s',
        name, value, pformat(context.response_copy))


def compare_original_response_with_copy(context):
    """Compare original JSON with its modified copy.

    :param context: Behave context object.
    """
    original = context.response.json()
    copy = context.response_copy

    def compare_top_level_values():
        # get the list of fields that are JSON values not arrays
        keys = [val for val in original.iterkeys() if not isinstance(original[val], (dict, list, set))]
        assert keys, ('Expected at least 1 field key to compare but got none!')
        logging.debug('List of top tier field keys to compare: %s', keys)
        for key in keys:
            assert original[key] == copy[key]
        logging.debug(
            'All top level fields in the response copy have the same values as'
            ' in the original response. Here is a list of compared fields:\n%s',
            ', '.join(keys))

    def compare_items():
        original_items = original['items']
        copy_items = copy['items']
        skip = ['title', 'last_activity_date']
        for original_item in original_items:
            # get all item field keys
            keys = [val for val in original_item.iterkeys()]
            # remove the keys that need to be skipped
            keys = [x for x in keys if x not in skip]
            for copy_item in copy_items:
                # find matching items
                if original_item['question_id'] == copy_item['question_id']:
                    # compare original an copied items
                    for key in keys:
                        assert original_item[key] == copy_item[key]
                    logging.debug(
                        'All fields in the copied item ID: %s'
                        ' have the same values as in in the original items',
                        copy_item['question_id'])

    compare_top_level_values()
    compare_items()
