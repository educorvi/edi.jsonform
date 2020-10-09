# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView
import json
from requests.auth import HTTPBasicAuth
import requests


class Jsonview(BrowserView):
    def __call__(self):
#        self.context.gen_json()


        import pdb; pdb.set_trace()
        url = "http://localhost:8080/@types/Bestellung"

        content = requests.get(url, headers={'Accept': 'application/json'}, auth=('admin', 'admin'))
        if content.status_code == 200:
            parsed = json.loads(content.text)
            print(json.dumps(parsed, indent=4, sort_keys=True))
            #import pdb;pdb.set_trace()
            #results = content.json()
            #import pdb;pdb.set_trace()
            #print(results)



        template = '''<li class="heading" i18n:translate="">
          Sample View
        </li>'''
        return template
