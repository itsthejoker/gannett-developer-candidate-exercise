import cherrypy
import requests

from mako.template import Template

profile_site = "https://peaceful-springs-7920.herokuapp.com/profile/"
articles_site = "https://peaceful-springs-7920.herokuapp.com/content/{}/"

# in seconds, how long to keep the cookie for. Currently 1 year.
cookie_lifespan = 60 * 60 * 24 * 365
cookie_name = 'SiteApp::profileId'

default_text_color = '#000000'


class SiteApp(object):

    def load_cookie(self):
        ''' Abstracted out for testing purposes. Loads an existing cookie and
        returns the profileId. '''
        possible_profileId = cherrypy.request.cookie[cookie_name].value
        cherrypy.log("Retrieved profileId of {} from cookie".format(
            possible_profileId))
        return possible_profileId

    def get_profile_id(self):
        ''' Abstracted out for testing purposes. The call below will result in
        a json response ({'profileId': X}) where x is a number. We make the
        call and return the result. '''
        return requests.get(profile_site).json()['profileId']

    def create_cookie(self, profile_number):
        ''' Abstracted out for testing purposes. Uses the profileId to set
        a cookie with that information on the local machine. '''

        cookie = cherrypy.response.cookie
        cookie[cookie_name] = profile_number
        cookie[cookie_name]['path'] = '/'
        cookie[cookie_name]['max-age'] = cookie_lifespan

        cherrypy.log("Received profileId of {} from site".format(
            profile_number))

    def get_content(self, profile, content=None):
        ''' Abstracted out for testing purposes. If provided with content,
        use that. Otherwise, ping the articles site for information relating
        to this profileId. '''

        if content:
            return content
        else:
            return requests.get(articles_site.format(profile)).json()

    @cherrypy.expose
    def index(self):
        try:
            # have we been here before?
            profileId = self.load_cookie()

        except KeyError:
            # guess not.
            profileId = self.get_profile_id()
            self.create_cookie(profileId)

        articles = self.get_content(profileId)

        # store the value of theme so that we don't have to keep converting
        article_theme = articles['theme']
        if article_theme == 'well':
            text_color = '#8B4513'
        elif article_theme == 'rare':
            text_color = '#DC143C'
        else:
            text_color = default_text_color

        index_template = Template(filename='./index.html')

        return index_template.render(
            title="Gannett Developer Candidate Exercise",
            articles=articles,
            text_color=text_color)


if __name__ == '__main__':
    cherrypy.quickstart(SiteApp(), '/')
