# IMAP = Internet Message Access Protocol

import imapclient

gmailadd = input("Enter your Gmail ID: ")
gmailpwd = input("Enter your Gmail ID password: ")
reciptent = input("Enter reciptent Gmail ID: ")
imp = imapclient.IMAPClient('imap.gmail.com')
imp.login(gmailadd, gmailpwd)
