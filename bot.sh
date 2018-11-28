#!/bin/sh

pyhton=`which phyton`
cat=`which cat`

script=`$phyton quickstart.py`
echo $script >> msg.txt

#Send message to telegram API (change your chatid and token)
msg=`$cat msg.txt`
token="632930553:AAGpRuN7d_0bDMu3yxH2D3Sw-ofuROkVbmg"
chatid="393577627"
curl -s -F chat_id="$chatid" -F text="$msg" https://api.telegram.org/bot$token/sendMessage > /dev/null


