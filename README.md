# get_social_notifications
Use Selenium web driver to get social media notifications. Use this so I don't have to check all my social medias for notifications.

## How to Use:

It's...complicated. You need Selenium installed, and a Chrome driver installed. 
Then, the first time it runs you need to sign into those platforms before it works. 
I could implement sign in with the driver but I can't be bothered. Maybe I will if anyone ask for it.

Example usage:
```
$ Python GetSocial.py
Facebook:
        2 notifications found:
                Messenger, 1 unread
                Notifications, 2 unread
LinkedIn:
        2 notifications found
Instagram:
        No unread notifications
```
## Alternatives:

I had a different version of this using BeautifulSoup and Chrome cookies for signin. 
It worked for Facebook but Instagram's endpoints returns some scripts and graph queries instead of HTML so it would need a browser to run, hence I chose Selenium.

## Next steps:

I'll probably try to add push notifications or some wrapper to run this at an interval so that it automatically check for notifications.

## Support:
- Facebook
- Instagram
- LinkedIn


