TO SPEED UP PRESENTATION
----------------------------------------------------------------------------------
## SQL
CREATE TABLE injection (username varchar(128), password varchar(128), amount int);
SELECT * FROM injection;

# SQLi
## Insecure
http://127.0.0.1:8000/insecure/signup/
{
    "username":"nitish",
    "password":"123",
}
{
    "username":"anurag",
    "password":"456",
}
{
"username":"nitish",
"password":"unknown' or '1'='1"
}

## Secure
{
    "username":"apurba",
    "password":"789"
}
{
    "username": "milind",
    "password": "007"
}
{
    "username":"apurba",
    "password":"unknown' or '1'='1"
}

# HPP
## TEST
https://www.google.com/search?q=instgram&q=elon
http://127.0.0.1:8000/name/anurag/
http://127.0.0.1:8000/name/milind/
http://127.0.0.1:8000/name/someone/

## Insecure
http://127.0.0.1:8000/insecure/login/addmoney/username=nitish/password=123/amount=100/
http://127.0.0.1:8000/insecure/login/transfer/username=milind/amount=50/receiver=nitish/

## Secure
http://127.0.0.1:8000/secure/login/token/username=milind/password=007/amount=25/
http://127.0.0.1:8000/secure/login/add/username=milind/password=007/amount=25/token=
http://127.0.0.1:8000/secure/login/transfer/username=milind/amount=25/receiver=apurba/token=




### CONTRIBUTION
# MILIND[COE19B034] - HPP, CODE, WIRESHARK
# APURBA[CED19I053] - SQLi, CODE, WIRESHARK
# NITISH[CED19I058] - SQLi, CODE, WIRESHARK
# ANURAG[MSM19B021] - HPP CODE, WIRESHARK





