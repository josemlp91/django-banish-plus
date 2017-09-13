Django Banish Plus
====
**Django Banish Plus** is a Django *middleware* app to banish *user agents by IP address* or *User Agent Header*.
It also supports basic abuse prevention by automatically banning users if they **exceed a certain number of requests per minute**, which is likely some form of attack or attempted *denial of service*.

Django Banish Plus stores all ***banishments*** in memory to avoid database lookups on every request. 
It requires memcached, especially for the IP abuse monitoring feature.

Django Banish Plus is based on [Django Banish](http://github.com/yourabi/django-banish) package by [Yousef Ourabi][1].

Features
----------

1. Banish requests, by **IP** or **user agent header** included blacklist.
2. Avoid banish request by whitelist.
3. Banish request from TOR network, using TOR IPS database.
4. The banish action is configurable, (403 response, redirect or custom template).


Installation
------------

### Requirements:

* Python 2.7
* Django 1.11
* **Memcache** or **Redis** cache system.
* Celery

### Python Packages.
- celery: 4.1.0
- redis: 2.10.6
- django-redis-cache: 1.7.1

### Clone with Git:
> $ git clone git@git.intelligenia.com:21617/josemiguel/django-banish-private.git
    
    
### Pip install
> pip install git+ssh://git@git.intelligenia.com:21617/josemiguel/django-banish-private.git

    
### Install and config cache system, to save all banish ips list.

- [Link to config **mencached cache system** in Django enviroment](https://djangosteps.wordpress.com/2013/07/03/setup-memcache-for-django-in-a-development-environment/)
- [Link to config **redis cache system** in Django enviroment](https://realpython.com/blog/python/caching-in-django-with-redis/)

### Install and config celery asynchronous task manager, to refresh tor ips list database.

- [Link to config **redis asynchronous task manager** in Django enviroment](http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html)

Setup
------
Install django-banish. Make sure it is on your PYTHONPATH or in your django project directory.

In your django project settings.py you must set the following options:

1. Add ``'banish.middleware.BanishMiddleware'`` to ``MIDDLEWARE_CLASSES``

2. Add ``'banish'`` to ``INSTALLED_APPS``

3. Run ``manage.py migrate`` to apply database changes and create new tables.

4. Add ``BANISH_ENABLED = True`` to enable Django-Banish (handy if you lock yourself out, you can just set this to False)
    
5. ``ADD BANISH_EMPTY_UA = True|False`` to specify wether requests without a USER_AGENT header will be banned.

6. Optionally set ``BANISH_ABUSE_THRESHOLD`` (default is 75) to the threshold of requests per minute

7. Optionally set ``BANISH_MESSAGE`` (default is "You are banned.") to change default message for banned user.

8. Optionally set ``BANISH_URL_REDIRECT`` to set url to redirect if request is banish.

9.  Optionally set ``BANISH_TEMPLATRE`` to render a custom template if request is banish.

10. Optionally set ``BANISH_RESTRICT_FILTER`` = True|False (default False), to specific url patch where banish is applied.

11. ``BANISH_URI_FILTER`` is patch where banish is applied if  BANISH_RESTRICT_FILTER = True (example ``BANISH_URI_FILTER = '\api'`` only protect \api)

12. Set ``BANISH_ONLY_WHITELIST = True|False``to allow only request from whitelist.

13. Set ``BANISH_TOR_IPS = True|False`` to banish TOR request.

14. Set ``TOR_IPS_DATABASE`` with tor ips database, (example, ``TOR_IPS_DATABASE = "http://torstatus.blutmagie.de/ip_list_exit.php/Tor_ip_list_EXIT.csv"``)

15. Set ``TOR_CACHE_KEY`` with cache key. (example ``TOR_CACHE_KEY = "tor-ip-exit-list"``)


License
------
Django Banish Plus is released under the [Apache Software License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at [http://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

See the License for the specific language governing permissions and limitations under the License.

Authors
-------
 * [José Miguel LP (intelligenia)][2]
 * [Yousef Ourabi][1]

[1]: http://github.com/yourabi
[2]: https://github.com/josemlp91/
