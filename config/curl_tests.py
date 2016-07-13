

'''
curl -X POST -d "username=dmedhaug&password=gtr00p06" http://127.0.0.1:8000/api/auth/token/

Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImRtZWRoYXVnIiwiZW1haWwiOiJkam1lZGhhdWdAZ21haWwuY29tIiwiZXhwIjoxNDY4MjcyODM1fQ.CMIsUP4VMkjXwIg3JEjpcjJIfeHLiTHOdGAMJOmu9CM

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImRtZWRoYXVnIiwiZW1haWwiOiJkam1lZGhhdWdAZ21haWwuY29tIiwiZXhwIjoxNDY4MjcyODM1fQ.CMIsUP4VMkjXwIg3JEjpcjJIfeHLiTHOdGAMJOmu9CM
" http://127.0.0.1:8000/api/comments/


curl -X POST -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImRtZWRoYXVnIiwiZW1haWwiOiJkam1lZGhhdWdAZ21haWwuY29tIiwiZXhwIjoxNDY4MjcyODM1fQ.CMIsUP4VMkjXwIg3JEjpcjJIfeHLiTHOdGAMJOmu9CM" -H "Content-Type: application/json" -d '{"content":"some reply to another try"}' 'http://127.0.0.1:8000/api/comments/create/?slug=micahs-post&type=post&parent_id=12'



curl http://127.0.0.1:8000/api/comments/

'''

https://www.eventbriteapi.com/v3/users/me/?token=R3PE2OGPQEXNYJYY6B2G

https://www.eventbriteapi.com/v3/users/me/owned_events/?token=R3PE2OGPQEXNYJYY6B2G