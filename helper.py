import json
import logging
import os.path

import allure
from allure_commons.types import AttachmentType
from requests import session, Session, Response
from curlify import to_curl


def load_json_schema(file_name: str):
    path_schema = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'schemas', file_name)
    with open(path_schema) as schema_json:
        return json.loads(schema_json.read())


class CustomSession(Session):
    def __init__(self, base_url):
        self.base_url = base_url
        super().__init__()


    def request(self,method, url, *args, **kwargs) -> Response:
        response = super(CustomSession, self).request(method=method, url=self.base_url +  url, *args, **kwargs)
        msg = to_curl(response.request)
        logging.info(msg)
        with allure.step(f'{method} {url}'):
            allure.attach(body=f'status_code={response.status_code}\n{msg}', name='Request curl', attachment_type=AttachmentType.TEXT, extension='txt')

            try:
                response_body = response.json()
            except json.JSONDecodeError:
                response_body = response.text

            allure.attach(body=json.dumps(response_body, indent=2), name="Response body", attachment_type=AttachmentType.JSON)

        return response

reg_session = CustomSession('https://reqres.in')