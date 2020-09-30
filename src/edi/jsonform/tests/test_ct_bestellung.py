# -*- coding: utf-8 -*-
from edi.jsonform.content.bestellung import IBestellung  # NOQA E501
from edi.jsonform.testing import EDI_JSONFORM_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class BestellungIntegrationTest(unittest.TestCase):

    layer = EDI_JSONFORM_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_bestellung_schema(self):
        fti = queryUtility(IDexterityFTI, name='Bestellung')
        schema = fti.lookupSchema()
        self.assertEqual(IBestellung, schema)

    def test_ct_bestellung_fti(self):
        fti = queryUtility(IDexterityFTI, name='Bestellung')
        self.assertTrue(fti)

    def test_ct_bestellung_factory(self):
        fti = queryUtility(IDexterityFTI, name='Bestellung')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IBestellung.providedBy(obj),
            u'IBestellung not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_bestellung_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Bestellung',
            id='bestellung',
        )

        self.assertTrue(
            IBestellung.providedBy(obj),
            u'IBestellung not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('bestellung', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('bestellung', parent.objectIds())

    def test_ct_bestellung_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Bestellung')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
