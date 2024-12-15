from .apiHandler import APIHandler

def initializeAPIsFromConfig(apiConfigs):
    """
    Initializes API handlers from the provided configuration.

    Args:
        apiConfigs (dict): A dictionary containing API configurations.

    Returns:
        dict: A dictionary of initialized API handlers.
    """
    apis = {}
    for apiName in apiConfigs:
        config = apiConfigs[apiName]
        headers = None
        if 'headers' in config:
            headers = config["headers"]
        apiHandler = APIHandler(config["baseUrl"], headers)
        apis[apiName] = apiHandler
    return apis           