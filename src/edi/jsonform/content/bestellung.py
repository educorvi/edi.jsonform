# from plone.autoform import directives
from plone.dexterity.content import Item
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from plone.namedfile.field import NamedBlobFile

from edi.jsonform import _


class IBestellung(model.Schema):
    """ Marker interface and Dexterity Python Schema for Bestellung
    """
    # If you want, you can load a xml model created TTW here
    # and customize it in Python:
    
    meinedateien = schema.List(title=u"Dateien", value_type = NamedBlobFile(title = u"Meine Datei"))
    vorname = schema.TextLine(title=_(u"Vorname"), required=True)
    nachname = schema.TextLine(title=_(u"Nachname"), required=True)
    artikelnummer = schema.Int(title=_(u"Artikelnummer"), required=True)
    # country = schema.Choice(title = _(u"Country")

@implementer(IBestellung)
class Bestellung(Item):
    def gen_json(self):
        schemadict={}
        fields = schema.getFieldsInOrder(IBestellung)
        import pdb; pdb.set_trace()
        for i in fields:
            schemadict[i[0]] = {}

    """
    def gen_json(self):
        fields = zope.schema.getFieldsInOrder(IBestellung)
        import pdb; pdb.set_trace()
    """
