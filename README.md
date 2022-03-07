# bmi_test
## Credentials

username: admin
password: admin123

##  Get Risks API


POST: http://127.0.0.1:8000/get-risk
Body format:
{
    "app": "Welltory",
    "params": [
        "Sex",
        "Mood and mental performance self-esteem"
    ]
}


- First param app is the app name that is requesting for the risk.
- Second param will be the array of params