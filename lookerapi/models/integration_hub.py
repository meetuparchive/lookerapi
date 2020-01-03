# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning) 

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IntegrationHub(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, url=None, label=None, official=None, fetch_error_message=None, authorization_token=None, has_authorization_token=None, legal_agreement_signed=None, legal_agreement_required=None, legal_agreement_text=None, can=None):
        """
        IntegrationHub - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'url': 'str',
            'label': 'str',
            'official': 'bool',
            'fetch_error_message': 'str',
            'authorization_token': 'str',
            'has_authorization_token': 'bool',
            'legal_agreement_signed': 'bool',
            'legal_agreement_required': 'bool',
            'legal_agreement_text': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'id': 'id',
            'url': 'url',
            'label': 'label',
            'official': 'official',
            'fetch_error_message': 'fetch_error_message',
            'authorization_token': 'authorization_token',
            'has_authorization_token': 'has_authorization_token',
            'legal_agreement_signed': 'legal_agreement_signed',
            'legal_agreement_required': 'legal_agreement_required',
            'legal_agreement_text': 'legal_agreement_text',
            'can': 'can'
        }

        self._id = id
        self._url = url
        self._label = label
        self._official = official
        self._fetch_error_message = fetch_error_message
        self._authorization_token = authorization_token
        self._has_authorization_token = has_authorization_token
        self._legal_agreement_signed = legal_agreement_signed
        self._legal_agreement_required = legal_agreement_required
        self._legal_agreement_text = legal_agreement_text
        self._can = can

    @property
    def id(self):
        """
        Gets the id of this IntegrationHub.
        ID of the hub.

        :return: The id of this IntegrationHub.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IntegrationHub.
        ID of the hub.

        :param id: The id of this IntegrationHub.
        :type: int
        """

        self._id = id

    @property
    def url(self):
        """
        Gets the url of this IntegrationHub.
        URL of the hub.

        :return: The url of this IntegrationHub.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this IntegrationHub.
        URL of the hub.

        :param url: The url of this IntegrationHub.
        :type: str
        """

        self._url = url

    @property
    def label(self):
        """
        Gets the label of this IntegrationHub.
        Label of the hub.

        :return: The label of this IntegrationHub.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this IntegrationHub.
        Label of the hub.

        :param label: The label of this IntegrationHub.
        :type: str
        """

        self._label = label

    @property
    def official(self):
        """
        Gets the official of this IntegrationHub.
        Whether this hub is a first-party integration hub operated by Looker.

        :return: The official of this IntegrationHub.
        :rtype: bool
        """
        return self._official

    @official.setter
    def official(self, official):
        """
        Sets the official of this IntegrationHub.
        Whether this hub is a first-party integration hub operated by Looker.

        :param official: The official of this IntegrationHub.
        :type: bool
        """

        self._official = official

    @property
    def fetch_error_message(self):
        """
        Gets the fetch_error_message of this IntegrationHub.
        An error message, present if the integration hub metadata could not be fetched. If this is present, the integration hub is unusable.

        :return: The fetch_error_message of this IntegrationHub.
        :rtype: str
        """
        return self._fetch_error_message

    @fetch_error_message.setter
    def fetch_error_message(self, fetch_error_message):
        """
        Sets the fetch_error_message of this IntegrationHub.
        An error message, present if the integration hub metadata could not be fetched. If this is present, the integration hub is unusable.

        :param fetch_error_message: The fetch_error_message of this IntegrationHub.
        :type: str
        """

        self._fetch_error_message = fetch_error_message

    @property
    def authorization_token(self):
        """
        Gets the authorization_token of this IntegrationHub.
        (Write-Only) An authorization key that will be sent to the integration hub on every request.

        :return: The authorization_token of this IntegrationHub.
        :rtype: str
        """
        return self._authorization_token

    @authorization_token.setter
    def authorization_token(self, authorization_token):
        """
        Sets the authorization_token of this IntegrationHub.
        (Write-Only) An authorization key that will be sent to the integration hub on every request.

        :param authorization_token: The authorization_token of this IntegrationHub.
        :type: str
        """

        self._authorization_token = authorization_token

    @property
    def has_authorization_token(self):
        """
        Gets the has_authorization_token of this IntegrationHub.
        Whether the authorization_token is set for the hub.

        :return: The has_authorization_token of this IntegrationHub.
        :rtype: bool
        """
        return self._has_authorization_token

    @has_authorization_token.setter
    def has_authorization_token(self, has_authorization_token):
        """
        Sets the has_authorization_token of this IntegrationHub.
        Whether the authorization_token is set for the hub.

        :param has_authorization_token: The has_authorization_token of this IntegrationHub.
        :type: bool
        """

        self._has_authorization_token = has_authorization_token

    @property
    def legal_agreement_signed(self):
        """
        Gets the legal_agreement_signed of this IntegrationHub.
        Whether the legal agreement message has been signed by the user. This only matters if legal_agreement_required is true.

        :return: The legal_agreement_signed of this IntegrationHub.
        :rtype: bool
        """
        return self._legal_agreement_signed

    @legal_agreement_signed.setter
    def legal_agreement_signed(self, legal_agreement_signed):
        """
        Sets the legal_agreement_signed of this IntegrationHub.
        Whether the legal agreement message has been signed by the user. This only matters if legal_agreement_required is true.

        :param legal_agreement_signed: The legal_agreement_signed of this IntegrationHub.
        :type: bool
        """

        self._legal_agreement_signed = legal_agreement_signed

    @property
    def legal_agreement_required(self):
        """
        Gets the legal_agreement_required of this IntegrationHub.
        Whether the legal terms for the integration hub are required before use.

        :return: The legal_agreement_required of this IntegrationHub.
        :rtype: bool
        """
        return self._legal_agreement_required

    @legal_agreement_required.setter
    def legal_agreement_required(self, legal_agreement_required):
        """
        Sets the legal_agreement_required of this IntegrationHub.
        Whether the legal terms for the integration hub are required before use.

        :param legal_agreement_required: The legal_agreement_required of this IntegrationHub.
        :type: bool
        """

        self._legal_agreement_required = legal_agreement_required

    @property
    def legal_agreement_text(self):
        """
        Gets the legal_agreement_text of this IntegrationHub.
        The legal agreement text for this integration hub.

        :return: The legal_agreement_text of this IntegrationHub.
        :rtype: str
        """
        return self._legal_agreement_text

    @legal_agreement_text.setter
    def legal_agreement_text(self, legal_agreement_text):
        """
        Sets the legal_agreement_text of this IntegrationHub.
        The legal agreement text for this integration hub.

        :param legal_agreement_text: The legal_agreement_text of this IntegrationHub.
        :type: str
        """

        self._legal_agreement_text = legal_agreement_text

    @property
    def can(self):
        """
        Gets the can of this IntegrationHub.
        Operations the current user is able to perform on this object

        :return: The can of this IntegrationHub.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this IntegrationHub.
        Operations the current user is able to perform on this object

        :param can: The can of this IntegrationHub.
        :type: dict(str, bool)
        """

        self._can = can

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, IntegrationHub):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
