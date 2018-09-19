from flask import current_app, _app_ctx_stack
from flask import redirect, request, jsonify, make_response, render_template, session, url_for
import os.path
import os
import simplejson as json


class Locales(object):
    def __init__(self, app):
        self.app = app
        self.init_app(app)
    
    def init_app(self, app):
        app.config.setdefault('MESSAGES_DIR', 'messages')
        app.config.setdefault('DEFAULT_LANGUAGE', 'en')
        app.context_processor(self.messages_to_context)

    def get_locale(self):
        return request.args.get('uselang') or session.get('language') or request.accept_languages.best_match(self.get_locales()) or self.app.config.get('DEFAULT_LANGUAGE')
    
    def get_permanent_locale(self):
        return session.get('language') or self.app.config.get('DEFAULT_LANGUAGE')
    
    def set_locale(self, language=None):
        session['language'] = language or self.app.config.get('DEFAULT_LANGUAGE')
    
    def _get_messages(self, language=None):
        if language is None: language = self.get_locale()
        return json.loads(open(os.path.join(self.app.config.get('MESSAGES_DIR'), "%s.json" % language)).read())
    
    def get_message(self, message_code, language=None):
        return self._get_messages(language=language).get(message_code,
            self._get_messages(language=self.app.config.get('DEFAULT_LOCALE')).get(message_code)
        )
    
    def get_locales(self):
        return [x.replace('.json', '') for x in os.listdir(self.app.config.get('MESSAGES_DIR'))]
    
    def messages_to_context(self):
        locales = self._get_messages()
        default_locales = self._get_messages(language=self.app.config.get('DEFAULT_LANGUAGE'))
        for key in default_locales.keys():
            if key not in locales.keys():
                locales[key] = default_locales[key]
        return {'locale': locales}