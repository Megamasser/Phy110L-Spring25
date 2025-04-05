# Phy110L-Spring25
 
## 110L Assignments

This repository contains code and information for submitting and grading assignments in the Phy 110L Lab Class at UC Davis in Spring Quarter 2025.

## Guide for Submitting Assignments

This quarter, we will be using GitHub to submit assignments. GitHub is a collaborative coding platform that is used throughout academia and industry alike. It based on `git`, which is a tool for tracking changes made to your code and allowing you to go back to old versions if needed.

This guide assumes you already understand the basics of git and GitHub. It will not discuss how to actually put your code on github. For an introduction to how to use `git` and Github, see [this video](https://www.youtube.com/watch?v=8Dd7KRpKeaE).

Git was originally designed to be used from the command line. If you like, you can use [GitHub Desktop](https://desktop.github.com) to manage your repositories. It's not as powerful as the command line, but all the basic features you'll need for most coding projects are available. It's designed to be easy to use when you're getting started. I used it when I was first learning git, and I found it very helpful.

If you have any questions. Please feel free to reach out to me on Canvas or come to my office hours.

These instructions will be the same for all the assignments in this course.

**1. Create a Private Repository**

Github repositories can be public or private. As you may expect, public repositories can be seen by anyone, while your private repositories can only be seen by you and anyone else you grant access.

You will be submitting your code for this class by posting it in a private GitHub repository and sharing it with me. I recommend you create the repository *before* you start writing your solutions, and commit as you go. You can name the repo whatever you want, but I'd recommend something that makes it clear what the repo is for. 

If you're creating your repository directly on GitHub.com, there is a Public/Private repository option below the "description" field. If you're creating a repository using the GitHub Desktop client, there is a "keep this code private" checkbox when click the "Publish repository" button for the first time. 

**2. Add your Solutions, and some other stuff**

Make sure to add solutions for all the assignments to the repository. Additionally, you should add file named "pyproject.toml" with the following contents:

```toml
[project]
assignment-name = "My Assignment Name Here"
author = "Your Name Here"
dependencies = [
	"numpy",
	"scipy",
	"some-other-library"
]
```
This is a standard file you will find in almost all python projects. It contains important information about the project, including the name of any 3rd-party libraries that your code depends on. I will use it to make sure I have all the right libraries installed when I grade you code, and to track whose code I am work with.

The "dependencies" list should contain any external libraries that your code needs to run. This includes libraries like "numpy" or "scipy," but *not* modules that are in the python standard library, like "pathlib" or "math". If you're not sure, you can find a list of python standard library modules on [this page](https://docs.python.org/3/library/index.html)


**3. Add me as a collaborator on your repository**

Since your library is private, you will need to add me as a collaborator so that I can access it. For instructions on how to do this, see [this article](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository#)

My username on GitHub is [Megamasser](https://github.com/Megamasser)

**4. Submit your repository URL on Canvas**

GitHub does send me an email when you add me as a collaborator, but emails are hard to work with (from a code perspective).  From the repository home page on GitHub, click the <img src='button.png' width='75'> button and copy the link provided there. It should end with ".git". You can find your repository home page from your profile on GitHub, or by clicking the "View on GitHub" button in the "Repository" menu in GitHub Desktop.

Find the assignment on Canvas, and submit the url to the assignment.

## Assignment Format

You may submit your code as python scripts (.py files) or as Jupyter notebooks (.ipynb files). 

If you submit as python scripts, you should have one script for each problem. The scripts should be clearly named so it is easy for me to tell which is which.
If you submit as a jupyter notebook, be sure to submit the .ipynb file itself. Jupyter has an "export" feature which will create a python script, but it does not export the code in a standard format, which causes problems when I try to run it.

If the assignment asks a non-code question, you should include it in your notebook or script as a comment.

If you're writing your code as scripts, consider putting re-used code in a separate file and importing it. For example:

```python

# file library.py

class Charge:
	# some code here that defines the Charge class



# file problem1.py

from library import Charge

# some code here that uses your Charge class

```
This should work out of the box, as long as both files are in the same folder

## Grading Criteria

Your code will be graded on several criteria. These include, roughly in order of importance:

1. Does the code run?
2. Does the code do what the assignment asks?
3. Is the code well-organized and easy to read?
4. Does it run in a reasonable amount of time?

For points 3 and 4, I will never take off points without explicitly stating what needs improvement. In some cases, I will mark it but not take off points. If I see the same mistake in a later assignment though, I may choose to take off points.

I will give you feedback on your code by submitting issues to your repository. These will be divided into several categories:

- **Note**: This is for things that will not affect your grade on the assignment (or any later assignments) but that I think is worth sharing.
- **needs-fix**: This is for things that I did not take off points for, but may result in points being taken off in future assignments.
- **Problem**: This is for things I took off points for. These can be things that were previously marked as "needs-fix" or new issues. 
- **Critical**: This includes things like "your code doesn't run" or "one of the problems is missing." In the first case, I will do my best to try to track down the issue and point it out to you. But I do not promise to find bugs in your code.  

Last Update: April 5, 2025

