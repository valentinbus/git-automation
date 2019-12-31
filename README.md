## Automation for git 

### Git Token
 - Go in your settings/developper settings and generate a personal access token
 - `export GITHUB_ACCESS_TOKEN=your_token`
 
### Init Project
 - `cd git-automation`
 - `pip install -r requirements.txt`
 - `source .gitinit.sh` or add this command in your .bashrc or .zshrc
 - then you can run `.gitinit.sh name_of_your_project`

### Process
With this project you can create a repository on your github, create local folder init and push a first initial commit with README.md with only one command
