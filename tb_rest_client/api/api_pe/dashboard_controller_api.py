# coding: utf-8
#      Copyright 2020. ThingsBoard
#  #
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#  #
#          http://www.apache.org/licenses/LICENSE-2.0
#  #
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api.api_ce import DashboardControllerApi


class DashboardControllerApi(DashboardControllerApi):
    """NOTE: This class is auto generated by the swagger code generator program.    
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        super().__init__(api_client)

    def get_dashboards_by_entity_group_id_using_get(self, entity_group_id, page_size, page, **kwargs):  # noqa: E501
        """getDashboardsByEntityGroupId  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_dashboards_by_entity_group_id_using_get(entity_group_id, page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_group_id: entityGroupId (required)
        :param int page_size: Page size (required)
        :param int page: Page (required)
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :return: PageDataDashboardInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dashboards_by_entity_group_id_using_get_with_http_info(entity_group_id, page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dashboards_by_entity_group_id_using_get_with_http_info(entity_group_id, page_size, page, **kwargs)  # noqa: E501
            return data

    def get_dashboards_by_entity_group_id_using_get_with_http_info(self, entity_group_id, page_size, page, **kwargs):  # noqa: E501
        """getDashboardsByEntityGroupId  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_dashboards_by_entity_group_id_using_get_with_http_info(entity_group_id, page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_group_id: entityGroupId (required)
        :param int page_size: Page size (required)
        :param int page: Page (required)
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :return: PageDataDashboardInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_group_id', 'page_size', 'page', 'text_search', 'sort_property', 'sort_order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_group_id' is set
        if ('entity_group_id' not in params or
                params['entity_group_id'] is None):
            raise ValueError("Missing the required parameter `entity_group_id` when calling `get_dashboards_by_entity_group_id_using_get`")  # noqa: E501
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_dashboards_by_entity_group_id_using_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_dashboards_by_entity_group_id_using_get`")  # noqa: E501

        if 'page_size' in params and params['page_size'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_dashboards_by_entity_group_id_using_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'page' in params and params['page'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `get_dashboards_by_entity_group_id_using_get`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'entity_group_id' in params:
            path_params['entityGroupId'] = params['entity_group_id']  # noqa: E501

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
        if 'sort_property' in params:
            query_params.append(('sortProperty', params['sort_property']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/entityGroup/{entityGroupId}/dashboards{?pageSize,page,textSearch,sortProperty,sortOrder}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDataDashboardInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dashboards_by_ids_using_get(self, dashboard_ids, **kwargs):  # noqa: E501
        """getDashboardsByIds  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_dashboards_by_ids_using_get(dashboard_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dashboard_ids: dashboardIds (required)
        :return: list[DashboardInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dashboards_by_ids_using_get_with_http_info(dashboard_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dashboards_by_ids_using_get_with_http_info(dashboard_ids, **kwargs)  # noqa: E501
            return data

    def get_dashboards_by_ids_using_get_with_http_info(self, dashboard_ids, **kwargs):  # noqa: E501
        """getDashboardsByIds  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_dashboards_by_ids_using_get_with_http_info(dashboard_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str dashboard_ids: dashboardIds (required)
        :return: list[DashboardInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard_ids' is set
        if ('dashboard_ids' not in params or
                params['dashboard_ids'] is None):
            raise ValueError("Missing the required parameter `dashboard_ids` when calling `get_dashboards_by_ids_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'dashboard_ids' in params:
            query_params.append(('dashboardIds', params['dashboard_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/dashboards{?dashboardIds}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DashboardInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_group_dashboards_using_get(self, entity_group_id, page_size, page, **kwargs):  # noqa: E501
        """getGroupDashboards  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_group_dashboards_using_get(entity_group_id, page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_group_id: entityGroupId (required)
        :param str page_size: pageSize (required)
        :param str page: page (required)
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :return: PageDataDashboardInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_group_dashboards_using_get_with_http_info(entity_group_id, page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_group_dashboards_using_get_with_http_info(entity_group_id, page_size, page, **kwargs)  # noqa: E501
            return data

    def get_group_dashboards_using_get_with_http_info(self, entity_group_id, page_size, page, **kwargs):  # noqa: E501
        """getGroupDashboards  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_group_dashboards_using_get_with_http_info(entity_group_id, page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_group_id: entityGroupId (required)
        :param str page_size: pageSize (required)
        :param str page: page (required)
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :return: PageDataDashboardInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_group_id', 'page_size', 'page', 'text_search', 'sort_property', 'sort_order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_group_id' is set
        if ('entity_group_id' not in params or
                params['entity_group_id'] is None):
            raise ValueError("Missing the required parameter `entity_group_id` when calling `get_group_dashboards_using_get`")  # noqa: E501
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_group_dashboards_using_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_group_dashboards_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_group_id' in params:
            path_params['entityGroupId'] = params['entity_group_id']  # noqa: E501

        query_params = []
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
        if 'sort_property' in params:
            query_params.append(('sortProperty', params['sort_property']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/entityGroup/{entityGroupId}/dashboards{?textSearch,sortProperty,sortOrder,pageSize,page}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDataDashboardInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tenant_dashboards_using_get(self, page_size, page, **kwargs):  # noqa: E501
        """getTenantDashboards  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_tenant_dashboards_using_get(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_size: pageSize (required)
        :param str page: page (required)
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :return: PageDataDashboardInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tenant_dashboards_using_get_with_http_info(page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tenant_dashboards_using_get_with_http_info(page_size, page, **kwargs)  # noqa: E501
            return data

    def get_tenant_dashboards_using_get_with_http_info(self, page_size, page, **kwargs):  # noqa: E501
        """getTenantDashboards  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_tenant_dashboards_using_get_with_http_info(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_size: pageSize (required)
        :param str page: page (required)
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :return: PageDataDashboardInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page', 'text_search', 'sort_property', 'sort_order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_tenant_dashboards_using_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_tenant_dashboards_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
        if 'sort_property' in params:
            query_params.append(('sortProperty', params['sort_property']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/tenant/dashboards{?textSearch,sortProperty,sortOrder,pageSize,page}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDataDashboardInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tenant_dashboards_using_get1(self, tenant_id, page_size, page, **kwargs):  # noqa: E501
        """getTenantDashboards  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_tenant_dashboards_using_get1(tenant_id, page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: tenantId (required)
        :param str page_size: pageSize (required)
        :param str page: page (required)
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :return: PageDataDashboardInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tenant_dashboards_using_get1_with_http_info(tenant_id, page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tenant_dashboards_using_get1_with_http_info(tenant_id, page_size, page, **kwargs)  # noqa: E501
            return data

    def get_tenant_dashboards_using_get1_with_http_info(self, tenant_id, page_size, page, **kwargs):  # noqa: E501
        """getTenantDashboards  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_tenant_dashboards_using_get1_with_http_info(tenant_id, page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tenant_id: tenantId (required)
        :param str page_size: pageSize (required)
        :param str page: page (required)
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :return: PageDataDashboardInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tenant_id', 'page_size', 'page', 'text_search', 'sort_property', 'sort_order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params or
                params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `get_tenant_dashboards_using_get1`")  # noqa: E501
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_tenant_dashboards_using_get1`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_tenant_dashboards_using_get1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in params:
            path_params['tenantId'] = params['tenant_id']  # noqa: E501

        query_params = []
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
        if 'sort_property' in params:
            query_params.append(('sortProperty', params['sort_property']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/tenant/{tenantId}/dashboards{?textSearch,sortProperty,sortOrder,pageSize,page}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDataDashboardInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_dashboards_using_get(self, page_size, page, **kwargs):  # noqa: E501
        """getUserDashboards  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_user_dashboards_using_get(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_size: pageSize (required)
        :param str page: page (required)
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :param str operation: operation
        :param str user_id: userId
        :return: PageDataDashboardInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_user_dashboards_using_get_with_http_info(page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_user_dashboards_using_get_with_http_info(page_size, page, **kwargs)  # noqa: E501
            return data

    def get_user_dashboards_using_get_with_http_info(self, page_size, page, **kwargs):  # noqa: E501
        """getUserDashboards  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.get_user_dashboards_using_get_with_http_info(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str page_size: pageSize (required)
        :param str page: page (required)
        :param str text_search: textSearch
        :param str sort_property: sortProperty
        :param str sort_order: sortOrder
        :param str operation: operation
        :param str user_id: userId
        :return: PageDataDashboardInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page', 'text_search', 'sort_property', 'sort_order', 'operation', 'user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_user_dashboards_using_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_user_dashboards_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
        if 'sort_property' in params:
            query_params.append(('sortProperty', params['sort_property']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501
        if 'operation' in params:
            query_params.append(('operation', params['operation']))  # noqa: E501
        if 'user_id' in params:
            query_params.append(('userId', params['user_id']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/user/dashboards{?textSearch,sortProperty,sortOrder,operation,userId,pageSize,page}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDataDashboardInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_dashboard_using_post(self, dashboard, **kwargs):  # noqa: E501
        """saveDashboard  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.save_dashboard_using_post(dashboard, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Dashboard dashboard: dashboard (required)
        :param str entity_group_id: entityGroupId
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_dashboard_using_post_with_http_info(dashboard, **kwargs)  # noqa: E501
        else:
            (data) = self.save_dashboard_using_post_with_http_info(dashboard, **kwargs)  # noqa: E501
            return data

    def save_dashboard_using_post_with_http_info(self, dashboard, **kwargs):  # noqa: E501
        """saveDashboard  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api_pe.save_dashboard_using_post_with_http_info(dashboard, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Dashboard dashboard: dashboard (required)
        :param str entity_group_id: entityGroupId
        :return: Dashboard
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard', 'entity_group_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard' is set
        if ('dashboard' not in params or
                params['dashboard'] is None):
            raise ValueError("Missing the required parameter `dashboard` when calling `save_dashboard_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'entity_group_id' in params:
            query_params.append(('entityGroupId', params['entity_group_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'dashboard' in params:
            body_params = params['dashboard']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/dashboard{?entityGroupId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Dashboard',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
