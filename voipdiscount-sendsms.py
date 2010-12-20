#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
#
# $Id$
#
# $License$
#

from BeautifulSoup import BeautifulStoneSoup
import urllib, urllib2, sys

username    = r'username'
password    = r'password'
sender      = r'sender'

url         = 'https://myaccount.voipdiscount.com/clx/sendsms.php?%s'

max_tries   = 5

try:
    params      = {
        'username':     username,
        'password':     password,
        'from':         sender,
        'to':           sys.argv[1],
        'text':         sys.argv[2],
    }
except Exception, e:
    print "Error:", e
    sys.exit(1)

try:
    length = len(params['text'])
    if length > 160:
        print 'Message too long: %d characters.' % length
        sys.exit(1)

    sys.stdout.write('Trying to send an sms message to %(to)s (size: %(length)d):' % {'to': params['to'], 'length': length, })
    sys.stdout.flush()

    for current_try in xrange(max_tries):
        page = urllib2.urlopen(url % urllib.urlencode(params))
        soup = BeautifulStoneSoup(page)
        resultstring = soup.find('resultstring')

        if resultstring.contents[0] != 'success':
            sys.stdout.write(' .')
            sys.stdout.flush()
        else:
            print ' done.'
            sys.exit(0)

    print ' error.'
except Exception, e:
    print "Error:", e

# EOF
