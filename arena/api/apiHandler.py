import requests

class APIHandler:
    """
    A class to handle API requests.

    Attributes:
        baseUrl (str): The base URL for the API.
        headers (dict): Optional headers for the API requests.
    """

    def __init__(self, baseUrl, headers=None):
        """
        Initializes the APIHandler with a base URL and optional headers.

        Args:
            baseUrl (str): The base URL for the API.
            headers (dict, optional): Headers for the API requests.
        """
        self.baseUrl = baseUrl
        self.headers = headers if headers else {}

    def runAPI(self, apiConfig):
        """
        Executes an API request based on the provided configuration.

        Args:
            apiConfig (dict): Configuration for the API request.

        Returns:
            tuple: A tuple containing a success flag and the response data or error message.
        """
        method = apiConfig.get("method", "GET").upper()
        endpoint = apiConfig.get("endpoint", "")
        url = f"{self.baseUrl}{endpoint}"
        headers = {**self.headers, **apiConfig.get("headers", {})}
        queryParams = apiConfig.get("queryParams", {})
        data = apiConfig.get("data", {})

        try:
            response = requests.request(method, url, headers=headers, params=queryParams, json=data)
            response.raise_for_status()
            return True, response.json()
        except requests.exceptions.RequestException as e:
            return False, str(e)

    def runAPIWithCallbacks(self, apiConfig, onSuccess=None, onError=None):
        """
        Executes an API request and handles success and error callbacks.

        Args:
            apiConfig (dict): Configuration for the API request.
            onSuccess (callable, optional): Callback function for successful requests.
            onError (callable, optional): Callback function for failed requests.

        Returns:
            tuple: A tuple containing a success flag and the response data or error message.
        """
        success, result = self.runAPI(apiConfig)
        if success:
            if onSuccess:
                onSuccess(result)
            else:
                return success, result
        else:
            if onError:
                onError(result)
            else:
                return success, result