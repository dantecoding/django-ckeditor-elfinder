from django.conf import settings
import os
ELFINDER_ROOT = u'%s'%os.path.abspath(settings.MEDIA_ROOT)
ELFINDER_URL = u'../../media/'
ELFINDER_THUMB = os.path.join(ELFINDER_ROOT, 'tmb')
ELFINDER_THUMB_URL = u'%s%s/'%(ELFINDER_URL, 'tmb')