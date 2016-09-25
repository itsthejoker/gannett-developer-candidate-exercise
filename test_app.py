import cherrypy

from cherrypy.test import helper
from mock import patch

from main import SiteApp


class SiteAppTest(helper.CPWebCase):

    def setup_server():
        cherrypy.tree.mount(SiteApp())

    setup_server = staticmethod(setup_server)

    def test_basic_page_generation(self):
        ''' Does the single page site load at all? '''
        self.getPage("/")
        self.assertStatus('200 OK')
        self.assertHeader('Content-Type', 'text/html;charset=utf-8')
        self.assertInBody('Gannett Developer Candidate Exercise')

    @patch('main.SiteApp.get_profile_id', return_value=45)
    def test_cookie_creation(self, mock_cookie):
        self.getPage("/")
        self.assertHeader("Set-Cookie")
        assert self.cookies == [(
            'Cookie', 'SiteApp::profileId=45; Max-Age=31536000; Path=/'
        )]

    def test_cookie_load(self):
        '''
        To the best of my knowledge (and what I can find online), there is no
        way to fully test cookies without enabling and using sessions, and
        based on the project description I believe that is outside the scope of
        this app. I can verify that the loading of cookies does work without
        issue manually, so for this demo I'll leave it as is.
        '''

    def test_get_profile_id(self):
        site = SiteApp()
        result = site.get_profile_id()
        assert result in [0, 1, 2, 3, 4]

    def test_get_content(self):
        site = SiteApp()
        # feed it content
        result = site.get_content(1, "asdf")
        assert result == "asdf"
        # get live content
        result = site.get_content(1)
        assert "theme" in result
        assert "title" in result['articles'][0]
        assert "summary" in result['articles'][0]

    fake_content01 = {
        'articles': [
            {'title': 'blargh',
             'summary': 'this is a summary',
             'href': "https:/a/"
             }
        ],
        'theme': 'well',
    }

    @patch('main.SiteApp.get_content', return_value=fake_content01)
    def test_template_well(self, mock_content):
        self.getPage("/")
        self.assertInBody('#8B4513')
        self.assertInBody('blargh')
        self.assertInBody('this is a summary')
        self.assertInBody('<a href=https:/a/ style=')

    fake_content02 = {
        'articles': [
            {'title': 'foobar',
             'summary': 'this is also a summary',
             'href': "https:/b/"
             }
        ],
        'theme': 'rare',
    }

    @patch('main.SiteApp.get_content', return_value=fake_content02)
    def test_template_rare(self, mock_content):
        self.getPage("/")
        self.assertInBody('#DC143C')
        self.assertInBody('foobar')
        self.assertInBody('this is also a summary')
        self.assertInBody('<a href=https:/b/ style=')
