Thermos
=======

This is a script I use to quickly deploy toy flask apps to an unprovisioned unbuntu server.

Sets up a basic nginx in front of gunicorn with supervisor managing.

Do not use for production sites.

Usage
=====

```bash
python mkinstall.py <name-of-app> <url-to-git-repo>
```

Name of app can be whatever you want. It doesn't correspond to your Flask app name or anything.

Creates a bash script to copy to your server and run.

Conventions
===========

This assumes you've named your app file app.py and you don't have a complicated setup.
