# What's this

During the creation/build of the project, a notes on all the issues faced.

# Issues

#### Issue 1.

Installed Python 3.6 on mac, and then installed feedparser module, when trying to parse the URL end up with the error

```
[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:749)
```

To fix the issue, had to install the certificates through the command

```
/Applications/Python\ 3.6/Install\ Certificates.command
```

Source: https://github.com/tensorflow/tensorflow/issues/10779

#### Issue 2.

When trying to access the Django REST API from the vue JS it ends up with the error

```
Failed to load http://127.0.0.1:8000/security/: No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin 'http://localhost:8080' is therefore not allowed access.
```

To solve it had to install the module : django-cors-headers



