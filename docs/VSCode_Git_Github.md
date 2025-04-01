## Git & GitHub in a Nutshell (VS Code Focus)
### What is Git?
* Git is a version control system that tracks changes to files over time.
* It allows you to collaborate, experiment on different features in separate branches, and revert to old versions if needed.
* Each commit represents a snapshot of your project at a specific time.
### Why Use Git?
* **History & Undo** – You have a timeline of changes and can revert or compare versions.
* **Collaboration** – Multiple people can work on the same code without interfering with each other.
* **Branching** – Develop new features in isolation, then merge them back.
### GitHub Basics
* **GitHub** is an online hosting service for Git repositories.
* It makes collaboration easier with features like pull requests, issue tracking, and social coding.
* You can have **public** (open to everyone) or **private** repos (visible only to you and chosen collaborators).
### Setting Up Git & GitHub in VS Code
1. Install VS Code (if not already).
2. Install Git on your machine (to let VS Code interact with it, even if you prefer not to use the command line).
3. Sign in to GitHub within VS Code:
   * Click on Accounts in the bottom-left corner of VS Code or open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P` on macOS), then search for “GitHub: Sign in”.
   * Follow the on-screen prompts to authenticate with GitHub.
4. Check the Source Control Panel:
   * VS Code has a built-in Source Control panel (the icon with three branching lines in the Activity Bar on the left).
   * You’ll see all Git changes, staged files, commit messages, etc. in this panel.
### Typical GitHub Workflow in VS Code
#### 1. Create or Clone a Repository
Create Repo on GitHub:

1. Go to [github.com](https://github.com) and click New to create a new repository.
2. Provide a name and choose public or private.
3. Optionally add a README, .gitignore, and license.
4. Click Create repository.
5. Copy the repository URL (SSH or HTTPS).

Clone Repo in VS Code:

1. In VS Code, open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`).
2. Search for Git: Clone.
3. Paste in the repository URL.
4. Choose a local folder to clone into.
5. After cloning, VS Code may prompt you to open the cloned folder—click Open.
#### 2. Make Changes
* Open any files in VS Code and edit them.
* VS Code will automatically track changes in the Source Control panel.
#### 3. Stage & Commit Changes
1. Go to the Source Control panel (icon on the left).
2. You will see changed files under Changes.
3. Hover over or right-click the file(s) you want to include in the commit. Click + to stage them. (Alternatively, click + next to **Changes** to stage all.)
4. Enter a commit message in the text box at the top (e.g., “Add new feature”).
5. Click the checkmark icon (✓) or press `Ctrl+Enter` / `Cmd+Enter` to commit.
#### 4. Push Changes
* Click the sync or push icon in the Source Control panel to push your local commits to GitHub.
* If prompted, log in to GitHub within VS Code.
#### 5. Pull Changes
* To get the latest changes from GitHub:
   * Click the sync or pull icon in the Source Control panel.
   * This updates your local files with any new commits from teammates or your remote repo.
### Branching & Merging in VS Code
Create a Branch:
* In the bottom-left corner of VS Code (Status Bar), you can see the current branch (e.g., `main`).
* Click it to open a branch menu, then choose Create New Branch.
* Provide a branch name, e.g., `feature/my-new-feature`.
Switch Branches:
* Same menu: pick another branch to check out.

Make Changes & Commit on the new branch.
Merge (or Create Pull Request):
* If you’re alone on a project, you can merge locally (on the `main` branch, right-click the branch name and choose “Merge from…”).
* If collaborating, push your branch to GitHub, then open a Pull Request on GitHub to review and merge your changes.
### Common Git + VS Code Actions (Cheat Sheet)
Initialize a Local Repo (if you do it locally):

* Open a folder in VS Code, then open Source Control.
* If no Git repo is detected, you’ll see Initialize Repository – click it.

View Changes:

* Click a changed file in Source Control to see a side-by-side diff (before vs. after).

Stage / Unstage Changes:

* Use + or - icons next to files to stage or unstage.

Commit:

* Type a message.
* Press Ctrl+Enter (Windows/Linux) or Cmd+Enter (macOS) or click the checkmark.

Push/Pull/Sync:

* Click the up/down arrows in the Source Control panel or in the bottom status bar to push/pull.

Branch Operations:

* Click on branch name in the bottom-left corner.
* Choose “Create Branch…,” “Switch Branch…,” “Publish Branch,” etc.

### Troubleshooting & Tips
Authentication Issues:

* Make sure you are signed into GitHub in VS Code.
* Use Personal Access Tokens or GitHub CLI if needed (when 2FA is on).

File Conflicts:

* Occur when two people edit the same lines of code differently.
* VS Code will highlight conflicts; manually decide which changes to keep.

Ignore Files:

* Use a .gitignore file to exclude files (e.g., node_modules/, build outputs) from version control.

Keep Commits Descriptive:

* This makes the project history easier to navigate.

Sync Frequently:

* Pull changes often to avoid large, complicated merges.

### Further Resources
Official Git Docs: https://git-scm.com/doc
GitHub Docs: https://docs.github.com/
VS Code + Git: https://code.visualstudio.com/docs/editor/versioncontrol