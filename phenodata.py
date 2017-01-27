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
        }

        files = {
            'upload': open(data_file, 'rb')
        }

        if figure_file != None:
            files['figure'] = open(figure_file, 'rb')

        r = requests.post(self.base_url+"/papers?auth_token="+self.auth_token, data=payload, files=files, headers=self.headers)
        return r.json()


pd = PhenoData("")

print(pd.getAll())