git remote -v (for cheking upstream and origin)


git branch  (in my master)

git pull  upstream newdesign_joao_english   (taking pull of rated:master) 

git checkout -b login (go to login branch,     if not there -b will create)


git add .

git commit -m"wip"

git push origin login  (after work )



*********************************************************
*********************************************
git remote -v


git branch --track newdesign upstream/newdesign_joao_english   

git checkout newdesign (newdesign is my copy of newdesign_joao_english )


***********************************************************
************use this***************************************

git pull upstream newdesign_joao_english

git checkout -b login_store_pwd

git branch

**************************************************************
****************************************************************




for staging:
/home/priyank/google_appengine/appcfg.py update /home/priyank/ratedapartments/server


for local: 
cd google_appengine
./dev_appserver.py  /home/priyank/ratedapartments/server/app.yaml

**************************************************************
**************************************************************
debugging:

from inspect import currentframe, getframeinfo
frameinfo = getframeinfo(currentframe())
print frameinfo.filename, frameinfo.lineno









**********************************************************************
**********************************************************************
Only consider this part   ,, written on: 06/04/2019

**********************************************************************
*************delete branch********************************************
https://koukia.ca/delete-a-local-and-a-remote-git-branch-61df0b10d323






******************************************************************.*****
************see branches************************************************

git branch      ::   shows all local brances and also shows your current local branch
git branch -a   ::   local+remote
git branch -r   ::   remote

**************************************************************************




*********************************************************************
**********************************************************************

For adding new feature

Guys, our final branch is "just_before_master", it will contain all changes

steps to add a feature::



step 1.: create a new local branch

On terminal type-

$git checkout -b branch_for_new_feature

Note- for clarity you can delete other local branches

$git branch -d <local branch name>



step 2.:: get code of "just_before_master" in your local

$git pull origin just_before_master



step 3.:: perform changes you want and then add,commit,push this branch to remote

$git add .

$git commit -m"mssg"

$git push origin branch_for_new_feature

Now this branch will appear in github site



step 4.:: Goto github.com, you will see that "branch_for_new_feature" is there
  
open pull request to merge "branch_for_new_feature" into "just_before_master"

"just_before_master"  <<----   "branch_for_new_feature"

successfully merged, now you will get option to delete  "branch_for_new_feature"




step 5.::if you type on terminal

$git remote -r

it will still show "branch_for_new_feature" in list of remote branches but actully it does not exist at remote, to update the list, type


$git remote prune origin 


!!!!!DONE, thanks!!!!!



****************************************************************************************	*
***********************************************************************************

to replace(not merge) code in oldbranch with code in newbranch

git push origin +newBranch:oldBranch


(old brach will be deleted and new branch will come )
