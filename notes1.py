# Notes Learning git and github



Git = 'Git is the Control Version system, it work as time line that let us come back to specif moments in the project';

plain_text = 'it is just simple text, do not represent any other characters';

# the process or stages of the work
git_stages ='are the stages of the work, working directory, staging zone, git repository';

# the first of all we start a repository in a directory, we use 'git init'
git_init = 'this start a repository';
repository = 'is the data base where every change gonna be stay';

#to configure git <git config>
git_config = 'show all the settings of git';

#to view where the setting are saved 'git config --list --show-origin

# we need to identify in Git, for that we gonna configure
# we get into the global cofigure 'git config --global'
#'git config --global user.name', change our name
#'git config --global user.email, change our email 

# but our repository don't know that it file is there, we must to add to 'Staging Zone' using 'git add <file>'
staging_zone = 'is the temporal zone where our files gonna prepare before to upload to the repository, the files in this stage are saved in the cache memory';
cache_memory = ' is a hardware or software component that stores data so that future request for that data can be faster'

git_add = 'add the files to the Staging Zone';

#to add everysingle file in the directory, we use 'git add . '

# to add the files in Staging Zone to the Repository, we use 'git commit -m 'message';
git_commit = 'this upload the files in Staging Zone to the repository, is important add a message to explain or describe';

# and send the files to HEAD of the master

# we can add to 'Staging Zone' and send to the repository, i mean
# 'git add' + 'git commit' = 'git commint -am <messeage>'
# this just work with files added to 'Staging Area' previuslly

HEAD ="Is the final update in the branch";

master = " Is the main branch of our project, is VERY IMPORTANT change to main name to work with GITHUB";
#  below show how to change the name in 'github section'

# to view the state of our repository, we use 'git status'
git_status = 'is used to display the state of the repository and stage are, it allows see the tracked, tracked files and changes ';

#it can show to us: 
# modificated/M (red) : that mean that the files was modificated, but is not in staging zone
# untracked/?? (red) : this show that file isn't tracked
# newfile added/A (green) : was added a file to Staging zone
#modificated/M (green) : that mean that the files was modificated, and it is in stage zone

# to have a simpler view to the state, we add the '-s' to the end

tracked_files = ' tracked files are files that git know about';
untracked_files = 'Untracked files are everything else in our directory that are not in Staging Zone';

# to see the specific change in the code, we use 'git show'
git_show = 'it show the specifics updates in the code(the lines, author, when,etc';

# to view every commit we use, 'git log', to view a specific file changes is used 'git log <file>'
git_log = 'this show a list of all commits made to a repository, this display the history of a repository'
# information displyed by this commnad :
# 'commint <code>' is the ID code of the commit, and then ( 'stage of the branch' -> 'branch')
# author
# date
# and messeage
# if we add '--stat', we can view the specific changes

# to remove files 'git rm <file>' is used
git_rm = 'to remove files, without deleting their history data, we can use again using git checkout';

# with "git rm --cached <file>" remove the files in staging area, but they are in hard disk yet
#but with "git rm --force <file>" delete in staging area and in the hard disk

#but this gonna depends of the stage of our files
# if the file stay in staging zone 'git rm -cached <file>', but we can add again if the file is our directory

branch = 'is a working time line ';

# we can create new branches
# we can have a specific branches every situation
# is very important have order in our branches
# there is standars to name the branches 
# the command 'git flow' display a list of these
 
git_flow = "Display a list of Standard branches name";


 # to come back to a anterior version, we use 'git reset <code-id> --<type>'
git_reset = 'this gonna undo the changes to specific version';

 # the type is if this gonna be 'hard','soft' or 'soft'
 # 'hard' is undo all changes to the specific version
 #'soft' undo the changes to 'Stage Zone'
 # and 'mixed' undo, bring the changes to our working directory 
 # 'git reset HEAD' : come back the files in Stage Zone to our directory 

# for example we can use --soft, if we have something in commit and we want to remove it 
# and have something in Staging zone and replaced it

# or remove in Staging zone such commit with --hard
 
# to comparate changes in git we use diff 
# to comapare specifics files is used git diff <git diff 'code-id-earler' 'code-id-older'>
git_diff = 'we can view a comparate the anterior state with one more recently';

# to change the version without delete other, we use 'git checkout <code-id-version> <file-name>'
git_checkout = 'we this we can change of version file or change the branch';

# to come back to master version we use git 'checkout master <file-name>'

#################################################################################################

# SECOND STAGE IN THE COURSE

# Platzi - Git and Github Course - 3/20/2022

#git log --oneline - Te muestra el id commit y el título del commit.
#git log --decorate- Te muestra donde se encuentra el head point en el log.
#git log --stat - Explica el número de líneas que se cambiaron brevemente.
#git log -p- Explica el número de líneas que se cambiaron y te muestra que se cambió en el contenido.
#git shortlog - Indica que commits ha realizado un usuario, mostrando el usuario y el titulo de sus commits.
#git log --graph --oneline --decorate y
#git log --pretty=format:"%cn hizo un commit %h el dia %cd" - Muestra mensajes personalizados de los commits.
#git log -3 - Limitamos el número de commits.
#git log --after=“2018-1-2” ,
#git log --after=“today” y
#git log --after=“2018-1-2” --before=“today” - Commits para localizar por fechas.
#git log --author=“Name Author” - Commits realizados por autor que cumplan exactamente con el nombre.
#git log --grep=“INVIE” - Busca los commits que cumplan tal cual está escrito entre las comillas.
#git log --grep=“INVIE” –i- Busca los commits que cumplan sin importar mayúsculas o minúsculas.
#git log – index.html- Busca los commits en un archivo en específico.
#git log -S “Por contenido”- Buscar los commits con el contenido dentro del archivo.
#git log > log.txt - guardar los logs en un archivo txt

# Branches

# to have a parallel working directory we must create a branch

#explain working flow git

#############################################################################################################

git_stages;
# i start i my local directory  and start my working flow git using 'git init'

git_init;

# two areas more 0are created, staging zone and repository

staging_zone;
repository;

# the first stage is 'unstaged zone' or my local directory, here i work
# the files are untracked

untracked_files;

# then i finish a work i send to the 'staging zone'  using 'git add'
#and here the start to be tracked
tracked_files;
# this a temporal zone stored in the cache memory
cache_memory;
#if reset my pc, the files her going to be delete to
#here the files are grouping and prepared to send to the repository

# when i want commit out change we send to our repository  using 'git commit'

git_commit;

# if i am working with teammates we need a remote repository


remote_repository = ' is a repository, but can share the work online';

# to get the data from a remote repository we clone the repository, using 'git clone <url>'

git_clone = "Clone the online repository in our local directory";

# and we can follow working as we was doing before (git add, git commit)
# but to send my commit in the head of the master to the remote repository
# we use 'git push'

git_push = "send my commit in the head of the master to the remote repository";

HEAD;
master;

# to get a update from remote repository to my repository, use <git fetch>

git_fetch = "get a update from remote repository to the local repository";

# then to paste to my local directory, we use <git merge>

git_merge = " to merge the data in the local repository with the local directory ";

# but to do fetch and merge in one sigle command, we use <git pull>

git_pull = "combine git fetch and git merge ";

# to create a new branch we use 'git branch <name>' or create and move on with 'git checkout -b <name>'

git_branch = 'Create a new branch';

# to move on to one branch we use 'git checkout <name>'
#we can move all in master to other with 'git branch -m <name-to-destine-branch>'

# to view a list of our branches we use 'git checkout --list' or just use 'git branch'

# to view the commits in oir branch 'git log --graph --decorate'
# to merge to branches
#we must to stay in branch where we want continous
#and the use 'git merge <name of the branch gonna merge with the actual branch>'

#git merge is a commited from a branch to other one

# it important be careful about 'merge conflict'
# if there is gonna apear with <<<<<< and >>>> separete with =======
# the first part is our local branch and the second the income branch changes

#when a merge cobfilct happen, git wait that you resolve and commit the changes or cancel it

# we just choose and modificated what code we want and commit

# we can cancel the merge with 'git merge --abort'

# we can check the merge, and cancel it or confirm with a commit


#######################################################################################################

# WORKING WITH REMOTE REPOSITORIES

GITHUB = 'The Code Social Network, Is website manager of Git repositories';

README = 'Is a text file that contain the information of the repository, This is where you can write a long description for your project';

raw = 'show us the text plan of README.md file';

blame = 'display the list of authors of every update';

history = "display the history of updates of our repository, it's like git log, is a historial of commits";


# how to add  to our remote repository the changes in the local directory

# how to link with Github



# first integrate the remote changes before to do a push
# we must to be careful with the name of our branch
# in git the name is 'master'
#in github is 'main'


#Step 1 - Move the ‘master’ branch to ‘main’
# we must to migrate the branch from master to main
# the next commands which creates a branch called ‘main’ using the history from ‘master’.
#  Using the argument -m will transfer all of the commit history
#  on the ‘master’ branch to your new ‘main’ branch so nothing gets lost.
# 'git branch -m master main'
# first we must link it


#Step 2 - Push ‘main’ to remote repo
#Remember that git is version control software on your local machine
#  and GitHub is the remote server that stores your code. 
# For this reason, you’ll have to push your new ‘main’ branch up to GitHub 
# and tell the local branch to start tracking the remote branch with the same name.
# 'git push -u origin main'
# -u = --set-upstream

# Step 3 - Point HEAD to ‘main’ branch
# At this stage if ‘master’ was your default branch you cannot remove it without first changing HEAD
# the pointer to the current branch reference. 
# This following command will point it to ‘main’.
# 'git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main'


#Delete ‘master’ branch on the remote repo
# 'git push origin --delete master'





# select 'clone or download' button

# and we can select http or ssh

# if we select http:

# copy the url

# go to our local directory from the shell

# we need to indicate to git that we gonna add a remote origin of our files in the local directory
# we use 'git remote add origin <url>'
# to view the origin we use 'git remote'

git_remote = "show us the repository's url ";

# but to be more explicit we add '-v', that mean 'verbal'

# and then send the files 'git push(to send) origin(to the url) <branch>(branch to send)



delta = "changes done";

# if we have histories unrelated
# we use 'git pull origin <branch> --allow-unrelated-histories'


##################################################################
# this can confuse at the beging
# thing that i do

#change from master to main
# important

# 1 add remote repository

# copy url
# git remote add origin <url>


# and we need to do pull to fuse changes in the remote with local
# 'git pull origin <branch>'

# we have unralated histories, we must to use
# 'git pull origin <branch> --allow-unrelated-histories'

#################################################################
# change from master to main

# Step 1 
# create main branch locally, taking the history from master
# 'git branch -m master main'
# git branch (-m | -M) [<oldbranch>] <newbranch>
# -m = merge

# Step 2 
# push the new local main branch to the remote repo (GitHub) 
# 'git push -u origin main'
# -u =--set-upstream
#
# Step 3
# switch the current HEAD to the main branch
# 'git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main'

# Step 4
# change the default branch on GitHub to main
# https://docs.github.com/en/github/administering-a-repository/setting-the-default-branch

# Step 5
# delete the master branch on the remote
# ' git push origin --delete master'


######################################################################

# and then send our commits 'git push(to send) origin(to the url) <branch>(branch to send)
# to to bring changes 'git pull origin <branch>
# to send changes 'git push origin <branch>'

#####################################


# how public & private keys work 

# a symmetrical encrypition is a passoword, you type it to access to the information inside of a document
# but if we want to share a file we need to share the password, and that can to use to attack us

# public & private keys also known as asynnetric one-way encrypition or encryption cipher
# we two kinds of keys

# public key is like a mail box
# private key is like a the key to open the mail box

# we can share our public key to recive data
# and with our private key we view to 

# SSH
# The Secure Shell Protocol is a cryptographic network protocol for operating network services 
# securely over an unsecured network
ssh = "Secure Shell, is protocol to connect two computer remotly without passphrase using encrytion keys";


# SSH or Secure Shell is a network communication protocol that enables two computers to communicate

# create a SSH key

# step 1
# is recomend stay in the home directory (~)
# we use 'ssh-keygen -t rsa -b 4096 -C <email-in-github>
# ssh-keygen(like generation key)
#  -t( specify the algorihtm) 
# rsa(is the more popular alfgorithm)
# - b (specify how much complex is the key) 
# 4096 (is the key's complexity from a mathematical view )
# -C (specify email)

# step 2
# we need to add the public key to Github
# first we must to add the key to the environment

environment = 'is the state of a computer determined by a combination of software, basic hardware, and which programs are running'

# the process is different to add the key to the environment

# in windows & linux

# we need to verify the program to connect keys is working
# for that we use 'eval $(ssh-agent -s)'
# this gonna print something like 'Agent pid <id>'

# then of verify if the program is runnig we must to add to the environment
# we need to use 'ssh-add <ubication of the privaty key>' 


# to find the ubication of a file we use 'find <route from gonna find>/ -name *.<extention>'
# we can add to the route 
# ~ = home
# . = actual directory
# we can specify the type with -type
#d = directory
#f = files

# in mac
# for that we use 'eval "$(ssh-agent -s)"'
# we need to modify a file called 'config' in the '.ssh' directory
#if the files don't stay there's we must to create to, and write

#Host *
# <tab> AddKeysToAgent yes
# <tab> UseKeychain yes
# <tab> IdentityFiles ~/.ssh.id_rsa

#we must to add to the environment
# ssh-add -K <ubication
# -K = keychain

keychain = 'is app in macOS to store and share data(users, passwords) in icloud';

# connection to Github through SSH

# we go to our profile in Github and find SSH keys
# and add and paste the public key

# then we need to change to SSH
#go to 'clone or download' option select SSh

# go to our local directory and change the https url for SSh url
# we use 'git remote set-url origin <url-SSh>'

# every time when we link with remote repository must to fuse with 'pull'
# 'git pull origin <branch>'

# origin is the name of our reposiry, but can have other name  


##############################################################

# Alias and tags

# we can create a alias using