#!/usr/bin/python
import fitbit
fb = fitbit.Fitbit()
CK = open("CK","r")
CS = open("CS","r")
fb.CONSUMER_KEY = CK.read()
fb.CONSUMER_SECRET = CS.read()
auth_url,auth_token = fb.GetRequestToken()
print auth_url

