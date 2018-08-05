# **Logs Analysis**

### Project Description:
  This program uses python and PostgreSQL to read a database, "news."

  There are three tables within this database--_authors, articles,_ and _log_--
  which serve to provide data about a set of articles, their authors, and
  how many times they have been requested.

  There are 3 questions which this program answers:
    **What are the three most popular articles of all time?**
    **Which authors are the most popular?**
    **On which day(s) have more than 1% of requests resulted in errors?**

### Requirements to Run
  -Python
  -Vagrant
  -VirtualBox
  -Database/vagrant folder: https://github.com/udacity/fullstack-nanodegree-vm
    -_fork and clone_
  -Data for the database:   https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
    -will unzip into 'newsdata.sql'

### Steps to Run
1. Make sure Vagrant and VirtualBox are installed
2. Open terminal
3. `cd` into the directory where you have cloned this repository:
    https://github.com/udacity/fullstack-nanodegree-vm
4. `cd` into the `vagrant` sub-directory within the repository
5. Run this command:
    `vagrant up`
6. Then run this command:
    `vagrant ssh`
7. `cd` into `/vagrant`
8. Move the `newsdata.sql` and `FSND-P1.py` files into the vagrant directory of the repository
9. Run the program using this command while in virtual environment: `python FSND-P1.py`


#### **Project from: Udacity Fullstack Developer Nanodegree**
