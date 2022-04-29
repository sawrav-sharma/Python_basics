import requests

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

def test_page_response():
    stale_links =  ['http://brochure.getpython.info/', 'http://wiki.python.org/moin/', 'http://python.org/dev/peps/', 
    'http://planetpython.org/', 'http://pyfound.blogspot.com/', 'http://pycon.blogspot.com/', 
    'http://docs.python.org/3/tutorial/introduction',
     'http://pyfound.blogspot.com/2022/03/meta-deepens-its-investment-in-python',
      'http://pyfound.blogspot.com/2022/03/the-pi-thon-2022-psf-spring-fundraiser', 
      'http://www.djangoproject.com/', 'http://www.pylonsproject.org/', 'http://bottlepy.org', 
      'http://tornadoweb.org', 'http://flask.pocoo.org/', 'http://www.web2py.com/', 
      'http://wiki.python.org/moin/', 'http://www.riverbankcomputing.co.uk/software/pyqt/intro', 
      'http://www.wxpython.org/', 'http://www.scipy.org', 'http://pandas.pydata.org/', 'http://ipython.org', 
      'http://buildbot.net/', 'http://trac.edgewall.org/', 'http://roundup.sourceforge.net/', 
      'http://www.ansible.com', 'http://brochure.getpython.info/', 'http://wiki.python.org/moin/', 
      'http://python.org/dev/peps/', 'http://planetpython.org/', 'http://pyfound.blogspot.com/', 
      'http://pycon.blogspot.com/']
    return stale_links

a = test_page_response()
# print(a)

for i in a:
    response = requests.get(i)
    print(i + "Status code : ",response.status_code, response.reason, response.ok)
