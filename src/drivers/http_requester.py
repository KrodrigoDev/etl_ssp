from typing import Dict, Union

import requests


class HttpRequester:

    def __init__(self) -> None:
        self.__url = "https://seguranca.al.gov.br/?page_id=13494"

    def request_from_page(self) -> Dict[str, Union[int, str]]:
        response = requests.get(self.__url)

        return {"status_code": response.status_code, "html": response.text}
