# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.6.6, generator: @autorest/python@5.12.0)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

VERSION = "unknown"

class ContainerRegistryConfiguration(Configuration):
    """Configuration for ContainerRegistry.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param url: Registry login URL.
    :type url: str
    :keyword api_version: Api Version. The default value is "2021-07-01". Note that overriding this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        url: str,
        **kwargs: Any
    ) -> None:
        super(ContainerRegistryConfiguration, self).__init__(**kwargs)
        api_version = kwargs.pop('api_version', "2021-07-01")  # type: str

        if url is None:
            raise ValueError("Parameter 'url' must not be None.")

        self.url = url
        self.api_version = api_version
        kwargs.setdefault('sdk_moniker', 'containerregistry/{}'.format(VERSION))
        self._configure(**kwargs)

    def _configure(
        self,
        **kwargs: Any
    ) -> None:
        self.user_agent_policy = kwargs.get('user_agent_policy') or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get('headers_policy') or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get('proxy_policy') or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get('logging_policy') or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get('http_logging_policy') or policies.HttpLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get('retry_policy') or policies.AsyncRetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get('custom_hook_policy') or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get('redirect_policy') or policies.AsyncRedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get('authentication_policy')
