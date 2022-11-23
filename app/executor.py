from typing import Dict
import requests, sys

ARGENTINA_ID: int = 9

class RequestExecutor:
    def __init__(self, token: str, url: str) -> None:
        self.token = token
        self.url = url
    
    def _get_teams_url(self) -> str:
        return self.url + 'team'

    def _get_team_url(self, team_id: int) -> str:
        return self._get_teams_url() + f'/{team_id}'

    def _get_headers(self) -> Dict[str,str]:
        return {
                'Authorization': f'Bearer {self.token}',
                'Content-Type': 'application/json'
        }

    def get_arg_group(self) -> None:
        r = requests.get(self._get_team_url(ARGENTINA_ID), headers=self._get_headers())
        return r.json()['data'][0]['groups']
