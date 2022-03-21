# Platzi - Git and Github Course - 3/20/2022

Git = 'Git is the Control Version system, it work as time line that let us come back to specif moments in the project';

plain_text = 'it is just simple text, do not represent any other characters';

# the process or stages of the work
git_stages ='are the stages of the work, working directory, stage zone, git repository';

# the first of all we start a repository in a directory, we use 'git init <file>'
git_init = 'this start a repository';
repository = 'is the data base where every change gonna be stay';

#to configure git <git config>
git_config = 'show all the settings of git';

#to view where the setting are saved 'git config --list --show-origin

# we need to identify in Git, for that we gonna configure
# we get into the globa cofigure 'git config --global'
#'git config --global user.name', change our name
#'git config --global user.email, change our email 

# but our repository don't know that it file is there, we must to add 'Stage Zone' using 'git add <file>'
stage_zone = 'is the temporal zone where our files gonna prepare before to upload to the repository, the files in this stage are saved in the cache memory';
cache_memory = ' is a hardware or software component that stores data so that future request for that data can be faster'

git_add = 'add the files to the Stage Zone';

#to add everysingle file in the directory, we use 'git add . '

# to add the files in Stage Zone to the Repository, we use 'git commit -m 'message';
git_commit = 'this upload the files in Stage Zone to the repository, is important add a message to explain or describe';

# to view the state of our repository, we use 'git status'
git_status = 'is used to display the state of the repository and stage are, it allows see the tracked, tracked files and changes ';

#it can show to us: 
# modificated/M (red) : that mean that the files was modificated, but not is in stage zone
# untracked/?? (red) : this show that file isn't tracked
# newfile/A (green) : was added a file to Stage zone
#modificated/M (green) : that mean that the files was modificated, and it is in stage zone

# to have a simpler view the state, we add the '-S' to the end

tracked_files = ' tracked files are files that git know about';
utracked_files = 'Untracked files are everything else in our directory that are not in Stage Zone';

# to see the specific change in the code, we use 'git show'
git_show = 'it show the specifics updates in the code(the lines, author, when,etc';

# to every commit we use, 'git log', to view a specific changes 'git log <file>'
git_log = 'this show a list of all commits made to a repository, this displaying the history of a repository'
# information of this command
# commint 'a code' is the ID code of the commit, and then ( 'stage of the branch' -> 'branch')
# author
# date
# and messeage
# if we add '--stat', we can view the specific changes

# to remove files 'git rm <file>' is used
git_rm = 'to remove files';

#but this gonna depends of the stage of our files
# if the file stay in stage zone 'git rm -cached <file>', but we can add again if the file is our directory

branch = 'is work in paralelo in a different time line';
 
 # to come back to a anterior version, we use 'git reset <code-id> --<type>'
git_reset = 'this gonna undo the changes to specific version';

 # the type is if this gonna be 'hard','soft' or 'soft'
 # 'hard' is undo all changes to the specific version
 #'soft' undo the changes to 'Stage Zone'
 # and 'mixed' undo, bring the changes to our working directory 

 
# to comparate changes in git we use diff 'git diff <git diff 'code-id-earler' 'code-id-older'
git_diff = 'we can view a comparate the anterior state with one more recently';

# to masa:






