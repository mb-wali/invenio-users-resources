# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 TU Wien.
#
# Invenio-Users-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""User groups service configuration."""

from invenio_records_resources.services import RecordServiceConfig, \
    SearchOptions, pagination_links

from ...records.api import UserGroupAggregate
from ..common import Link
from ..permissions import UsersPermissionPolicy
from ..schemas import UserGroupSchema
from .results import UserGroupItem, UserGroupList


class UserGroupSearchOptions(SearchOptions):
    """Search options."""

    # TODO search params
    params_interpreters_cls = SearchOptions.params_interpreters_cls


class UserGroupsServiceConfig(RecordServiceConfig):
    """Requests service configuration."""

    # common configuration
    permission_policy_cls = UsersPermissionPolicy
    result_item_cls = UserGroupItem
    result_list_cls = UserGroupList
    search = UserGroupSearchOptions

    # specific configuration
    record_cls = UserGroupAggregate
    schema = UserGroupSchema
    index_dumper = None

    # links configuration
    links_item = {
        "self": Link("{+api}/groups/{id}"),
        "avatar": Link("{+api}/groups/{id}/avatar.svg"),
    }
    links_search = pagination_links("{+api}/groups{?args*}")

    components = [
        # Order of components are important!
    ]