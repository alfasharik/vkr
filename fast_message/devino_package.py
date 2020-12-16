import requests


class DevinoClient:

    def __init__(self):
        self.get_session_url = 'https://integrationapi.net/rest/user/sessionid'
        self.send_sms_url = 'https://integrationapi.net/rest/Sms/Send'
        self.send_viber_url = 'https://integrationapi.net/rest/Viber/Send'
        self.get_sms_status_url = 'https://integrationapi.net/rest/Sms/State'

    def get_session(self, login, password):
        params = {'login': login, 'password': password}
        response = requests.get(self.get_session_url, params=params)

        return response

    def send_sms(self, session_id, source, dest, data, validity):
        params = {
            'SessionId': session_id, 'SourceAddress': source,
            'DestinationAddress': dest, 'Data': data, 'Validity': validity
        }
        response = requests.post(self.send_sms_url, params=params)

        return response

    def send_viber(self, session_id, source, dest, data, validity):
        params = {
            'SessionId': session_id, 'SourceAddress': source,
            'DestinationAddress': dest, 'Data': data, 'Validity': validity
        }
        response = requests.post(self.send_viber_url, params=params)

        return response

    def get_sms_status(self, session_id, message_id):
        params = {'sessionID': session_id, 'messageID': message_id}
        response = requests.get(self.get_sms_status_url, params=params)

        return response