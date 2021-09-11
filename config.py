import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'postgres://lqocrppdyykukd:2847958efa8663b25cf943cb5f80fb6b57124aed1189cca00cf38754b2eeb296@ec2-54-156-24-159.compute-1.amazonaws.com:5432/d2069d890pgbad'

CUSTOMER_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlpKVnRhX3AyTmktT0t1eGZINndwbyJ9.eyJpc3MiOiJodHRwczovL211ai1tb3NoaW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxM2FkYmRlNjMyNjFhMDA2ODdjMTdhZSIsImF1ZCI6Ik1lYWwtTWFnaWMiLCJpYXQiOjE2MzEyNDc1NDcsImV4cCI6MTYzMTMzMzk0NywiYXpwIjoiME5mZmpHTnJzYThzVVZ0eXRVMEdZRHNNVEc1MTRBSlMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpjdWlzaW5lcyIsImdldDpwcm9kdWN0cyJdfQ.NvOo0wfhGZvSAPfyhAtHT5NiT-yUhUou1a17XNx2-Y_89f8dvZqd5SSGZZQ-GFhQNZnq297J2e9VblffIgfqxZ1Ot8v5i6MqOawDUTcO08BX6WgpaEtvfdP4guKKHn8krGYbYqVWAIwMo4iqlhtBvu8zIg-0fbUyyACOzTvesjf9CNX1-ujq-Nzf2CxjDALi7UhQt5wejOLlPINkEflGzjxJwTBPGynO2Y5-zn9DKfkmDBzDutDoZGPLKRl-wLhOZ0NrdJGI30sAel4gzmWkelCMEasDL8-THiiQ6tIeGcB7aoGf_IHSFnyL-2zO87jhDOVOI1lgKgY_f_tsA4rp8w"
COOKER_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlpKVnRhX3AyTmktT0t1eGZINndwbyJ9.eyJpc3MiOiJodHRwczovL211ai1tb3NoaW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxM2FkYzI4NjM3NjJjMDA3MGMwMDdiYyIsImF1ZCI6Ik1lYWwtTWFnaWMiLCJpYXQiOjE2MzEyNDc2NTEsImV4cCI6MTYzMTMzNDA1MSwiYXpwIjoiME5mZmpHTnJzYThzVVZ0eXRVMEdZRHNNVEc1MTRBSlMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpwcm9kdWN0cyIsImdldDpjdWlzaW5lcyIsImdldDpwcm9kdWN0cyIsInBhdGNoOnByb2R1Y3RzIiwicG9zdDpwcm9kdWN0cyJdfQ.FG3TlSOzaTChhMziZeM4lkHM3m6oQkfIi4gPWX7f_qz-TTOMZ2AuI0fx6jQPJVZT5hxyV7nlk4F5c1dsdXuGAhrMSJ97IFKTsIyhSWLCuX5nkS4G5sQZlyVM8kaCP_ufQHF3InjU9fhXaHoaQsJ2Y_cGMPMxi2ZiSAwDLg5M9xVXSJ-Ct0OnsJF2643udHiu1uxnbuhUAMee5D3C-zClZcqDJWxA3FGMQ3R5SuIdBEZ-aMeHOgi6n4PNittA-1G4lY7KtElIL_OFfgNr63_yINlqAUxBuw_JV9NHA7KNZmyfP5m9vbu2svbSrdiuU0mogwUAuFDw8RWQhT8ARwXpEw"
MANGER_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlpKVnRhX3AyTmktT0t1eGZINndwbyJ9.eyJpc3MiOiJodHRwczovL211ai1tb3NoaW4udXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxM2FkYzVmOGY0NzE0MDA3MGVmNzE4OSIsImF1ZCI6Ik1lYWwtTWFnaWMiLCJpYXQiOjE2MzEyNDc3MDUsImV4cCI6MTYzMTMzNDEwNSwiYXpwIjoiME5mZmpHTnJzYThzVVZ0eXRVMEdZRHNNVEc1MTRBSlMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpjdWlzaW5lcyIsImRlbGV0ZTpwcm9kdWN0cyIsImdldDpjdWlzaW5lcyIsImdldDpwcm9kdWN0cyIsInBhdGNoOmN1aXNpbmVzIiwicGF0Y2g6cHJvZHVjdHMiLCJwb3N0OmN1aXNpbmVzIiwicG9zdDpwcm9kdWN0cyJdfQ.oEYjzJbGvurSz2--AONfMk7FiJjEYHjUrXVflY2csYsFB9r-I8gWMtTJUAczy8t6JX2afyo4NPTeMXzkVaNSgPTndBQKt85G9Vr_VixJ2df5UlJ1Al9OA9c-Asrr_cz8iQKRhYqz_SRFYotto0NC-adGiBZdJ_XFT_f0old2rLiNoIvW_3FeM9YeAvoGoPCUf54Afuzylnjv3kTwfO54E-llG5_EHcZ3zfL8WM1DB0maXCtdxfDHYiVMr-7ol_B_o1HpCNslm-tlMpe7o57b-E2eH94bLslGYHzN4ACr1mkxJpU_nRnoQmhZS-IML4ZnCblEo0Xim7Kv9aMcBfoBqA"

# Last update for token 9/10/2021 7:15 AM, KSA Timeline
