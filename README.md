# FinalCountdown - README.md

Preview
-------

[https://fcis-finalcountdown.herokuapp.com/](https://fcis-finalcountdown.herokuapp.com/)

  

Backstory
---------

I like hackathons a lot, but I haven't had the chance to join one yet. So I did what any introvert would do in my situation and hosted one. It was a big party for me, myself, and I. It was fun though, about 3 days of work to deliver an MVP, a good breather from a [project](https://github.com/mo3ist/DEDU) I've been working on for the past couple of months.
  

What is FinalCountdown
----------------------

\- A newsletter with a few tweaks:

It sends _custom_ periodic messages to its subscribers. And stops sending after a due date.

Nothing about it is static. There's a Django Model for everything so it can be easily tweaked.

  

**Live demo:**

![](/attachments/preview.GIF)

Technologies
------------

I haven't used anything crazy, just the good ol' **Django** with a couple o' views, **Postgres** as a production database, **Celery & Redis** for sending emails, and **Heroku** for deployment.

  

Here's a diagram that makes things sound complicated and smart:

![](/attachments/diagram.png)

Deployment
----------

I'm poor, so, Heroku free-tier.

  

### How did I run Django and Celery together with a free-tier?

This is by far the most interesting thing in this project.

  

Heroku doesn't let you run more than 1 worker if no money is involved. So I used [_Honcho_](https://github.com/nickstenning/honcho) _("a Python port of_ [_Foreman_](https://ddollar.github.io/foreman)_, a tool for managing Procfile-based applications.")_ as the sole worker, and used it to fork all the processes I need: **Gunicorn**, **Celery**, and **Celery beat**.

*   Note: Heroku still puts a memory limit!