import logging
from typing import Any, Dict, Optional
import requests
from utils.config_reader import ConfigReader

class APIHelper:
    def __init__(self,
        base_url: None,
        timeout: float = 10,
        headers: Optional[Dict[str, str]] = None,):
        self.base_url_api =  base_url
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(headers or {"Content-Type": "application/json"})
    
    def request(self, method, endpoint, params=None, json_data=None, headers=None, timeout=None):
        endpoint = endpoint.lstrip('/')
        url = self.base_url_api + "/" + endpoint
        response = self.session.request(
            method=method,
            url=url,
            params=params,
            json=json_data,
            headers=headers,
            timeout=timeout
        )
        return response
    
    def get(self, endpoint, params=None, headers=None, timeout=None):
        response = self.request("GET", endpoint, params=params)
        return response
    
    def close_session(self):
        self.session.close()

    #close_session = close

    
    

    


    

    
