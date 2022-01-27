# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 TU Wien.
#
# Invenio-Users-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""User groups service configuration."""

from invenio_records_resources.services import RecordServiceConfig, \
    SearchOptions

from ..permissions import UsersPermissionPolicy
from .results import UserGroupItem, UserGroupList


class UserGroupSearchOptions(SearchOptions):
    """Search options."""

    # TODO search params
    params_interpreters_cls = SearchOptions.params_interpreters_cls


class UserGroupsServiceConfig(RecordServiceConfig):
    """Requests service configuration."""

    # TODO common configuration
    permission_policy_cls = UsersPermissionPolicy
    result_item_cls = UserGroupItem
    result_list_cls = UserGroupList
    search = UserGroupSearchOptions

    record_cls = None  # needed for model queries
    schema = None
    index_dumper = None

    # TODO links configuration

    components = [
        # Order of components are important!
    ]
