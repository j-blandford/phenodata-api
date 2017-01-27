import requests, json

class PhenoData:
    def __init__(self, auth_token):
        self.auth_token = auth_token
        self.headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        self.base_url = 'http://hepmdb.soton.ac.uk/phenodata/api/public'

    def getAll(self):
        r = requests.get(self.base_url+"/papers?auth_token="+self.auth_token, headers=self.headers)
        return r.json()

    def get(self, p_id):
        r = requests.get(self.base_url+"/papers/"+p_id+"?auth_token="+self.auth_token, headers=self.headers)
        return r.json()
    
    def upload(self, bibtex_url, label, description, data_file, figure_file = None):
        payload = {
            'bibtex': bibtex_url,
            'label': label,
            'description': description,
            'upload': '@'+data_file,
        }

        if figure_file != None:
            payload['figure'] = '@'+figure_file

        r = requests.post(self.base_url+"/papers?auth_token="+self.auth_token, data=payload, headers=self.headers)
        return r.json()


pd = PhenoData("")

print(pd.getAll())