# -*- coding: utf-8 -*-

from Products.Five.browser import BrowserView


class Jsonview(BrowserView):
    def __call__(self):
        self.context.gen_json()
        template = '''<li class="heading" i18n:translate="">
          Sample View
        </li>'''
        return template
