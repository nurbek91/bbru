# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

from z3c.configurator import ConfigurationPluginBase
from zope.security.proxy import getObject
from zope.lifecycleevent import ObjectCreatedEvent
from zope.intid import IIntIds, IntIds
from zope.site import LocalSiteManager
from zope.event import notify

class InitializeConfigurator(ConfigurationPluginBase):
    """Заселение локальными компонентами в момент создания сайта"""

    def __call__(self, *args):
        site = getObject(self.context)
        try:
            sm = site.getSiteManager()
        except:
            site.setSiteManager(LocalSiteManager(site, False))
            sm = site.getSiteManager()

        if u'intids' not in sm:
            ob = IntIds()
            notify(ObjectCreatedEvent(ob))
            sm[u'intids'] = ob
            sm.registerUtility(ob, IIntIds)

class UpgradeConfigurator(ConfigurationPluginBase):
    """Дальнейшие манипуляции по заселению локальными компонентами,
    апргейд базы данных при обновлениях кода и т.д. """

    dependencies = ('_initialize', 'authentication', 'answers')

    def __call__(self, *args):
        site = getObject(self.context)
        sm = site.getSiteManager()
