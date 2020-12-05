# stepik_auto_test_python
Course about autotests on python

https://stepik.org/lesson/187065/

11/23/2020 updated:
I've had some troubles with yearly-statistic dashboard. 
My commits were not shown on this dashboard. I found a problem and 
solved it. `git config user.name` and `git config user.email` were wrong
for my git account. Although I use IDE PyCharm by JetBrains and I've been
connected from UI my wrong credentials have been used.


12/5/2020 updated:
To create/update a file with actual packages and plugins you should 
run in terminal: `pip freeze > requirements.txt`
after in the new env run: `pip install -r requirements.txt`

To create env, in the created dir: 
1. `python -m venv "name"`
1. `env_name\Scripts\activate.bat`
