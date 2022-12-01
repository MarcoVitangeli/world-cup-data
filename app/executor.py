from typing import Dict
import requests

class RequestExecutor:
    def __init__(self, email: str, password: str, url: str) -> None:
        self.url = url
        self.token = self._get_token(email, password)
        self.id = None
    
    def _get_teams_url(self) -> str:
        return self.url + 'team'

    def _get_team_url(self, team_id: int) -> str:
        return self._get_teams_url() + f'/{team_id}'

    def _get_headers(self) -> Dict[str,str]:
        return {
                'Authorization': f'Bearer {self.token}',
                'Content-Type': 'application/json'
        }

    def _get_token(self, email: str, pasw: str) -> str:
        r = requests.post(self.url + 'user/login', headers={'Content-Type': 'application/json'}, json={
                'email': email,
                'password': pasw
            })

        if r.json()['status'] != 'success':
            raise RuntimeError('Error login to API')

        return r.json()['data']['token'] 

    def _get_standings_url(self) -> str:
        return self.url + 'standings'

    def get_id_by_name(self, name: str) -> int:
        if self.id != None:
            return self.id

        r = requests.get(self._get_teams_url(), headers=self._get_headers())
        teams = r.json()['data']

        for team in teams:
            if team['name_en'].lower() == name.lower():
                self.id = team['id']
                return team['id']

        raise ValueError('Invalid team entered')

    def get_group_by_id(self, id: int) -> str:
        r = requests.get(self._get_team_url(id), headers=self._get_headers())
        return r.json()['data'][0]['groups']
    
    def get_pts_by_id(self, teamId: int) -> int:
        r = requests.get(self._get_standings_url(), headers=self._get_headers())
        data = r.json()['data']
        for group in data:
            for team in group['teams']:
                if  team['team_id'] == teamId:
                    return int(team['pts'])

        raise ValueError('Invalid team id')

