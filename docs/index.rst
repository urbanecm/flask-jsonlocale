Flask-JSONLocale
============================================

**Flask-JSONLocale** is a localization library taking locale data from JSON files called after language name. There is `self-explanatory example <https://github.com/urbanecm/flask-jsonlocale/tree/master/example>`_.

Configuration
^^^^^^^^^^^^^^^^

There are two configuration options:
* MESSAGES_DIR: path (relative to app.py's location) to messages directory. Defaults to messages. 
* DEFAULT_LANGUAGE: for language used defaults to en

Basic usage
^^^^^^^^^^^^^^^^^^
You need to inicialize the app by doing

.. code-block::

     from flask_jsonlocale import Locales
     locales = Locales(app)

This locales objects serves as an access point to your localization and allwos you to perform all operations. 

Locale's object method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The library allows you to change user's language. For doing it, you should create some change language interface and when the language should be switched, you should do this:

.. code-block::

    >>> locales.set_locale('en')
    
This store user's new language into session (under "language"). Please do not touch it manually, althrough it is technically possible. You can also fall-back to default language determination by doing this:

.. code-block::

    >>> locales.set_locale()


If you want to change your language only temporarily, you can use GET parameter 'uselang', which should to it. It is also possible to be shown just message codes, instead of localization, by using "qqx" as your language code. This should be never returned by get_locales (see below), but it is possible to pass it to set_locale(). 

When you need to get user's current language (for example to know what to check in your change language interface), you can do this:

.. code-block::

    >>> locales.get_locale()
    'en'

It is also possible to get list of supported language codes by doing:

.. code-block::

    >>> locales.get_locales()
    ['en', 'cs', 'de']

If you want to get translated message by message code, you can use this:

.. code-block::

    >>> locales.get_message('welcome')
    'Vítejte'

This will return the message in current user's language. There's optional parameter language to enforce to get message in that language. 

.. code-block::

    >>> locales.get_message('welcome', langauge='en')
    'Welcome'

Storing messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Messages are stored in directory specified by MESSAGES_DIR configuration variable. In that directory, one JSON file per language should be present. You can add message documentation to qqq.json. 

The format is as follows:

.. code-block::
{
   "welcome": "Welcome",
   "login": "Login"
}


.. code-block::
{
   "welcome": "Vítejte",
   "login": "Přihlásit se"
}

Pull requests are welcomed. 
