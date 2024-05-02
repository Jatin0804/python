# Git Commands

- mkdir learn = to create a folder
- ls = to show all files
- touch chapter1.txt = to create the file
- code chapter1.txt = to write in the file

###
- git init = to initialize the git 
- ls -a = to show all files and folders
- git status = to show all currently working files in git 
- git add chapter1.txt = to add this file into the working staging area
- git status
- git commit -m "This is the message" = to write the message and commit the file
- git touch chapter2.txt = to create file
- git touch README.md 
- code README.md
- git add . = to add all files in the directory

###
- git diff chapter2.txt = to check the difference between the current file and the last commit
- git checkout chapter2.txt = all the changes after the commit are rolled back
- git log = to check all the commits and actions performed

###
- git remote add origin https://github.com/Jatin0804/python.git = to add the folder to remote github
- git branch -M main = to change the branch to main
- git push -u origin main = to upload the local repository to remote and update the main branch

###
- touch secrets.txt
- touch .gitignore
- git add .
- git status
- git rm --cached -r . = rm is for remove
-r for recursive
. for all files
- git status
- code .gitignore
- git add .
- git commit -m "Added .gitignore"

###
- git branch new-plot = to create a new branch other than main
- git branch =  to check all the branches available
- git checkout new-plot = to switch to any other branch (new-plot)
- git add .
- git status
- git commit -m "Changes in Branch"
- git checkout main
- touch chapter4.txt
- code chapter4.txt
- git add .
- git commit -m "Changes in main "