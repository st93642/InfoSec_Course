"""
Static video library containing all InfoSec course videos.
This module contains hardcoded video data from GitHub releases.
"""

from typing import Dict, List, Any


class VideoLibrary:
    """Static video library with all course videos organized by release."""

    # Static video data - organized by release tag
    VIDEOS: Dict[str, List[Dict[str, Any]]] = {
        "13.0.0": [
                {
                        "name": "13.1.1.Intro.to.the.Course.mp4",
                        "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.1.Intro.to.the.Course.mp4",
                        "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.1.Intro.to.the.Course.txt",
                        "size": 45172845,
                        "description": "13 1 1 Intro to the Course"
                },
                {
                        "name": "13.1.10.Working.with.Git.in.Command.Line.mp4",
                        "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.10.Working.with.Git.in.Command.Line.mp4",
                        "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.10.Working.with.Git.in.Command.Line.txt",
                        "size": 99101684,
                        "description": "13 1 10 Working with Git in Command Line"
                },
                {
                        "name": "13.1.11.File.Lifecycle.in.Repository.mp4",
                        "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.11.File.Lifecycle.in.Repository.mp4",
                        "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.11.File.Lifecycle.in.Repository.txt",
                        "size": 129133970,
                        "description": "13 1 11 File Lifecycle in Repository"
                },
                {
                        "name": "13.1.12.Ignoring.Changes.mp4",
                        "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.12.Ignoring.Changes.mp4",
                        "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.12.Ignoring.Changes.txt",
                        "size": 184468296,
                        "description": "13 1 12 Ignoring Changes"
                },
                {

                    "name": "13.1.14.Working.with.Git.in.Development.Environments.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.14.Working.with.Git.in.Development.Environments.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.14.Working.with.Git.in.Development.Environments.txt",

                    "size": 139176844,

                    "description": "13 1 14 Working with Git in Development Environments"

                },
                {

                    "name": "13.1.15.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.15.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.15.Summary.txt",

                    "size": 25920208,

                    "description": "13 1 15 Summary"

                },
                {

                    "name": "13.1.2.1.Intro.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.1.Intro.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.1.Intro.txt",

                    "size": 25180554,

                    "description": "13 1 2 1 Intro"

                },
                {

                    "name": "13.1.2.10.Resolving.Conflicts.When.Updating.Repository.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.10.Resolving.Conflicts.When.Updating.Repository.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.10.Resolving.Conflicts.When.Updating.Repository.txt",

                    "size": 103060908,

                    "description": "13 1 2 10 Resolving Conflicts When Updating Repository"

                },
                {

                    "name": "13.1.2.12.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.12.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.12.Summary.txt",

                    "size": 16942183,

                    "description": "13 1 2 12 Summary"

                },
                {

                    "name": "13.1.2.2.Remote.and.Local.Repositories.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.2.Remote.and.Local.Repositories.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.2.Remote.and.Local.Repositories.txt",

                    "size": 82943602,

                    "description": "13 1 2 2 Remote and Local Repositories"

                },
                {

                    "name": "13.1.2.3.GitHub.and.GitLab.Overview.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.3.GitHub.and.GitLab.Overview.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.3.GitHub.and.GitLab.Overview.txt",

                    "size": 169034832,

                    "description": "13 1 2 3 GitHub and GitLab Overview"

                },
                {

                    "name": "13.1.2.4.GitHub.Registration.and.Remote.Repository.Creation.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.4.GitHub.Registration.and.Remote.Repository.Creation.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.4.GitHub.Registration.and.Remote.Repository.Creation.txt",

                    "size": 40684689,

                    "description": "13 1 2 4 GitHub Registration and Remote Repository Creation"

                },
                {

                    "name": "13.1.2.6.Connecting.to.Remote.Repository.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.6.Connecting.to.Remote.Repository.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.6.Connecting.to.Remote.Repository.txt",

                    "size": 183093299,

                    "description": "13 1 2 6 Connecting to Remote Repository"

                },
                {

                    "name": "13.1.2.7.Making.Changes.and.Sending.Them.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.7.Making.Changes.and.Sending.Them.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.7.Making.Changes.and.Sending.Them.txt",

                    "size": 56366046,

                    "description": "13 1 2 7 Making Changes and Sending Them"

                },
                {

                    "name": "13.1.2.9.Updating.Local.Repository.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.9.Updating.Local.Repository.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.9.Updating.Local.Repository.txt",

                    "size": 105016709,

                    "description": "13 1 2 9 Updating Local Repository"

                },
                {

                    "name": "13.1.2.Five.Useful.Tips.for.Working.with.the.Course.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.Five.Useful.Tips.for.Working.with.the.Course.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.2.Five.Useful.Tips.for.Working.with.the.Course.txt",

                    "size": 119301401,

                    "description": "13 1 2 Five Useful Tips for Working with the Course"

                },
                {

                    "name": "13.1.3.1.Intro.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.1.Intro.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.1.Intro.txt",

                    "size": 34848898,

                    "description": "13 1 3 1 Intro"

                },
                {

                    "name": "13.1.3.10.Pull.Request.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.10.Pull.Request.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.10.Pull.Request.txt",

                    "size": 161158697,

                    "description": "13 1 3 10 Pull Request"

                },
                {

                    "name": "13.1.3.11.Branching.Models.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.11.Branching.Models.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.11.Branching.Models.txt",

                    "size": 116338871,

                    "description": "13 1 3 11 Branching Models"

                },
                {

                    "name": "13.1.3.12.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.12.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.12.Summary.txt",

                    "size": 23680770,

                    "description": "13 1 3 12 Summary"

                },
                {

                    "name": "13.1.3.2.Branches.Creation.and.Work.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.2.Branches.Creation.and.Work.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.2.Branches.Creation.and.Work.txt",

                    "size": 149351213,

                    "description": "13 1 3 2 Branches Creation and Work"

                },
                {

                    "name": "13.1.3.3.Working.with.Remote.Branches.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.3.Working.with.Remote.Branches.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.3.Working.with.Remote.Branches.txt",

                    "size": 151663542,

                    "description": "13 1 3 3 Working with Remote Branches"

                },
                {

                    "name": "13.1.3.5.Stashing.Changes.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.5.Stashing.Changes.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.5.Stashing.Changes.txt",

                    "size": 127325625,

                    "description": "13 1 3 5 Stashing Changes"

                },
                {

                    "name": "13.1.3.7.Merging.Branches.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.7.Merging.Branches.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.7.Merging.Branches.txt",

                    "size": 105209490,

                    "description": "13 1 3 7 Merging Branches"

                },
                {

                    "name": "13.1.3.8.Resolving.Conflicts.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.8.Resolving.Conflicts.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.8.Resolving.Conflicts.txt",

                    "size": 80876039,

                    "description": "13 1 3 8 Resolving Conflicts"

                },
                {

                    "name": "13.1.3.Introduction.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.Introduction.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.3.Introduction.txt",

                    "size": 29521711,

                    "description": "13 1 3 Introduction"

                },
                {

                    "name": "13.1.4.1.Introduction.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.4.1.Introduction.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.4.1.Introduction.txt",

                    "size": 19322239,

                    "description": "13 1 4 1 Introduction"

                },
                {

                    "name": "13.1.4.10.Reverting.Merges.Renaming.Deleting.Branches.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.4.10.Reverting.Merges.Renaming.Deleting.Branches.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.4.10.Reverting.Merges.Renaming.Deleting.Branches.txt",

                    "size": 200335519,

                    "description": "13 1 4 10 Reverting Merges Renaming Deleting Branches"

                },
                {

                    "name": "13.1.4.11.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.4.11.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.4.11.Summary.txt",

                    "size": 15121410,

                    "description": "13 1 4 11 Summary"

                },
                {

                    "name": "13.1.4.2.Viewing.Changes.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.4.2.Viewing.Changes.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.4.2.Viewing.Changes.txt",

                    "size": 346885421,

                    "description": "13 1 4 2 Viewing Changes"

                },
                {

                    "name": "13.1.4.4.Deleting.Uncommitted.Changes.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.4.4.Deleting.Uncommitted.Changes.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.4.4.Deleting.Uncommitted.Changes.txt",

                    "size": 231918485,

                    "description": "13 1 4 4 Deleting Uncommitted Changes"

                },
                {

                    "name": "13.1.4.6.Reverting.Committed.Changes.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.4.6.Reverting.Committed.Changes.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.4.6.Reverting.Committed.Changes.txt",

                    "size": 231918485,

                    "description": "13 1 4 6 Reverting Committed Changes"

                },
                {

                    "name": "13.1.4.8.Resetting.Commits.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.4.8.Resetting.Commits.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.4.8.Resetting.Commits.txt",

                    "size": 169902853,

                    "description": "13 1 4 8 Resetting Commits"

                },
                {

                    "name": "13.1.4.Why.Version.Control.System.Is.Needed.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.4.Why.Version.Control.System.Is.Needed.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.4.Why.Version.Control.System.Is.Needed.txt",

                    "size": 199964213,

                    "description": "13 1 4 Why Version Control System Is Needed"

                },
                {

                    "name": "13.1.5.1.Working.in.Command.Line.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.5.1.Working.in.Command.Line.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.5.1.Working.in.Command.Line.txt",

                    "size": 192956906,

                    "description": "13 1 5 1 Working in Command Line"

                },
                {

                    "name": "13.1.5.3.Working.in.GitHub.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.5.3.Working.in.GitHub.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.5.3.Working.in.GitHub.txt",

                    "size": 150613743,

                    "description": "13 1 5 3 Working in GitHub"

                },
                {

                    "name": "13.1.5.4.Working.in.GitLab.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.5.4.Working.in.GitLab.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.5.4.Working.in.GitLab.txt",

                    "size": 119011806,

                    "description": "13 1 5 4 Working in GitLab"

                },
                {

                    "name": "13.1.5.5.Working.in.JetBrains.IDE.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.5.5.Working.in.JetBrains.IDE.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.5.5.Working.in.JetBrains.IDE.txt",

                    "size": 58740515,

                    "description": "13 1 5 5 Working in JetBrains IDE"

                },
                {

                    "name": "13.1.5.6.Working.in.VS.Code.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.5.6.Working.in.VS.Code.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.5.6.Working.in.VS.Code.txt",

                    "size": 96023969,

                    "description": "13 1 5 6 Working in VS Code"

                },
                {

                    "name": "13.1.5.7.Other.Clients.and.Tools.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.5.7.Other.Clients.and.Tools.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.5.7.Other.Clients.and.Tools.txt",

                    "size": 71307612,

                    "description": "13 1 5 7 Other Clients and Tools"

                },
                {

                    "name": "13.1.5.8.Git.Working.Rules.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.5.8.Git.Working.Rules.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.5.8.Git.Working.Rules.txt",

                    "size": 147221761,

                    "description": "13 1 5 8 Git Working Rules"

                },
                {

                    "name": "13.1.5.9.Common.Problems.and.Solutions.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.5.9.Common.Problems.and.Solutions.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.5.9.Common.Problems.and.Solutions.txt",

                    "size": 265883534,

                    "description": "13 1 5 9 Common Problems and Solutions"

                },
                {

                    "name": "13.1.5.What.Git.Workflow.Looks.Like.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.5.What.Git.Workflow.Looks.Like.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.5.What.Git.Workflow.Looks.Like.txt",

                    "size": 84103611,

                    "description": "13 1 5 What Git Workflow Looks Like"

                },
                {

                    "name": "13.1.6.Installing.Git.on.Windows.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.6.Installing.Git.on.Windows.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.6.Installing.Git.on.Windows.txt",

                    "size": 70949552,

                    "description": "13 1 6 Installing Git on Windows"

                },
                {

                    "name": "13.1.8.Installing.Git.on.MacOS.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.8.Installing.Git.on.MacOS.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.8.Installing.Git.on.MacOS.txt",

                    "size": 65456723,

                    "description": "13 1 8 Installing Git on MacOS"

                },
                {

                    "name": "13.1.9.Installing.Git.on.Linux.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.9.Installing.Git.on.Linux.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.1.9.Installing.Git.on.Linux.txt",

                    "size": 83488675,

                    "description": "13 1 9 Installing Git on Linux"

                },
                {

                    "name": "13.2.1.2.Installing.Python.and.PyCharm.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.1.2.Installing.Python.and.PyCharm.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.1.2.Installing.Python.and.PyCharm.txt",

                    "size": 305136515,

                    "description": "13 2 1 2 Installing Python and PyCharm"

                },
                {

                    "name": "13.2.1.3.Command.Line.and.Interpreter.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.1.3.Command.Line.and.Interpreter.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.1.3.Command.Line.and.Interpreter.txt",

                    "size": 201826636,

                    "description": "13 2 1 3 Command Line and Interpreter"

                },
                {

                    "name": "13.2.1.4.Working.in.PyCharm.Debugging.Programs.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.1.4.Working.in.PyCharm.Debugging.Programs.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.1.4.Working.in.PyCharm.Debugging.Programs.txt",

                    "size": 137647555,

                    "description": "13 2 1 4 Working in PyCharm Debugging Programs"

                },
                {

                    "name": "13.2.1.5.Conditional.Breakpoints.and.Interactive.Mode.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.1.5.Conditional.Breakpoints.and.Interactive.Mode.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.1.5.Conditional.Breakpoints.and.Interactive.Mode.txt",

                    "size": 133111536,

                    "description": "13 2 1 5 Conditional Breakpoints and Interactive Mode"

                },
                {

                    "name": "13.2.1.6.Working.with.Git.and.GitLab.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.1.6.Working.with.Git.and.GitLab.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.1.6.Working.with.Git.and.GitLab.txt",

                    "size": 249325072,

                    "description": "13 2 1 6 Working with Git and GitLab"

                },
                {

                    "name": "13.2.1.7.Merge.Proposals.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.1.7.Merge.Proposals.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.1.7.Merge.Proposals.txt",

                    "size": 163943734,

                    "description": "13 2 1 7 Merge Proposals"

                },
                {

                    "name": "13.2.10.1.Homework.Review.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.10.1.Homework.Review.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.10.1.Homework.Review.txt",

                    "size": 289148724,

                    "description": "13 2 10 1 Homework Review"

                },
                {

                    "name": "13.2.10.2.Exception.Handling.Try.Except.Operators.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.10.2.Exception.Handling.Try.Except.Operators.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.10.2.Exception.Handling.Try.Except.Operators.txt",

                    "size": 223891530,

                    "description": "13 2 10 2 Exception Handling Try Except Operators"

                },
                {

                    "name": "13.2.10.3.Exception.Handling.Else.Finally.Operators.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.10.3.Exception.Handling.Else.Finally.Operators.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.10.3.Exception.Handling.Else.Finally.Operators.txt",

                    "size": 107566337,

                    "description": "13 2 10 3 Exception Handling Else Finally Operators"

                },
                {

                    "name": "13.2.10.4.Raising.Exceptions.Raise.Operator.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.10.4.Raising.Exceptions.Raise.Operator.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.10.4.Raising.Exceptions.Raise.Operator.txt",

                    "size": 173020596,

                    "description": "13 2 10 4 Raising Exceptions Raise Operator"

                },
                {

                    "name": "13.2.10.5.Context.Manager.With.Operator.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.10.5.Context.Manager.With.Operator.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.10.5.Context.Manager.With.Operator.txt",

                    "size": 96562287,

                    "description": "13 2 10 5 Context Manager With Operator"

                },
                {

                    "name": "13.2.11.1.Homework.Review.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.11.1.Homework.Review.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.11.1.Homework.Review.txt",

                    "size": 96975561,

                    "description": "13 2 11 1 Homework Review"

                },
                {

                    "name": "13.2.11.2.Classes.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.11.2.Classes.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.11.2.Classes.txt",

                    "size": 72451985,

                    "description": "13 2 11 2 Classes"

                },
                {

                    "name": "13.2.11.3.Class.Methods.Argument.Self.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.11.3.Class.Methods.Argument.Self.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.11.3.Class.Methods.Argument.Self.txt",

                    "size": 151367784,

                    "description": "13 2 11 3 Class Methods Argument Self"

                },
                {

                    "name": "13.2.11.4.Constructor.Init.And.Working.With.Multiple.Classes.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.11.4.Constructor.Init.And.Working.With.Multiple.Classes.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.11.4.Constructor.Init.And.Working.With.Multiple.Classes.txt",

                    "size": 161234836,

                    "description": "13 2 11 4 Constructor Init And Working With Multiple Classes"

                },
                {

                    "name": "13.2.11.5.Defining.Classes.In.Modules.And.Importing.Them.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.11.5.Defining.Classes.In.Modules.And.Importing.Them.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.11.5.Defining.Classes.In.Modules.And.Importing.Them.txt",

                    "size": 51705772,

                    "description": "13 2 11 5 Defining Classes In Modules And Importing Them"

                },
                {

                    "name": "13.2.12.1.Homework.Review.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.12.1.Homework.Review.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.12.1.Homework.Review.txt",

                    "size": 85398408,

                    "description": "13 2 12 1 Homework Review"

                },
                {

                    "name": "13.2.12.2.Encapsulation.And.Data.Hiding.Getters.And.Setters.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.12.2.Encapsulation.And.Data.Hiding.Getters.And.Setters.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.12.2.Encapsulation.And.Data.Hiding.Getters.And.Setters.txt",

                    "size": 80613851,

                    "description": "13 2 12 2 Encapsulation And Data Hiding Getters And Setters"

                },
                {

                    "name": "13.2.12.3.Inheritance.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.12.3.Inheritance.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.12.3.Inheritance.txt",

                    "size": 94268467,

                    "description": "13 2 12 3 Inheritance"

                },
                {

                    "name": "13.2.12.4.Polymorphism.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.12.4.Polymorphism.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.12.4.Polymorphism.txt",

                    "size": 104111507,

                    "description": "13 2 12 4 Polymorphism"

                },
                {

                    "name": "13.2.12.5.Documentation.Class.And.Method.Description.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.12.5.Documentation.Class.And.Method.Description.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.12.5.Documentation.Class.And.Method.Description.txt",

                    "size": 109192828,

                    "description": "13 2 12 5 Documentation Class And Method Description"

                },
                {

                    "name": "13.2.13.1.Homework.Review.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.13.1.Homework.Review.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.13.1.Homework.Review.txt",

                    "size": 94814264,

                    "description": "13 2 13 1 Homework Review"

                },
                {

                    "name": "13.2.13.2.Iterators.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.13.2.Iterators.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.13.2.Iterators.txt",

                    "size": 47425578,

                    "description": "13 2 13 2 Iterators"

                },
                {

                    "name": "13.2.13.3.Iterator.Implementation.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.13.3.Iterator.Implementation.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.13.3.Iterator.Implementation.txt",

                    "size": 75529444,

                    "description": "13 2 13 3 Iterator Implementation"

                },
                {

                    "name": "13.2.13.4.Generators.and.Their.Implementation.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.13.4.Generators.and.Their.Implementation.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.13.4.Generators.and.Their.Implementation.txt",

                    "size": 65837422,

                    "description": "13 2 13 4 Generators and Their Implementation"

                },
                {

                    "name": "13.2.13.5.Type.Annotations.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.13.5.Type.Annotations.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.13.5.Type.Annotations.txt",

                    "size": 80256044,

                    "description": "13 2 13 5 Type Annotations"

                },
                {

                    "name": "13.2.14.1.Homework.Review.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.14.1.Homework.Review.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.14.1.Homework.Review.txt",

                    "size": 112225687,

                    "description": "13 2 14 1 Homework Review"

                },
                {

                    "name": "13.2.14.2.Function.as.Object.Higher-Order.Functions.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.14.2.Function.as.Object.Higher-Order.Functions.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.14.2.Function.as.Object.Higher-Order.Functions.txt",

                    "size": 94304921,

                    "description": "13 2 14 2 Function as Object Higher-Order Functions"

                },
                {

                    "name": "13.2.14.3.Decorators.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.14.3.Decorators.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.14.3.Decorators.txt",

                    "size": 76587761,

                    "description": "13 2 14 3 Decorators"

                },
                {

                    "name": "13.2.14.4.Some.Features.of.Using.Decorators.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.14.4.Some.Features.of.Using.Decorators.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.14.4.Some.Features.of.Using.Decorators.txt",

                    "size": 87090902,

                    "description": "13 2 14 4 Some Features of Using Decorators"

                },
                {

                    "name": "13.2.14.5.functools.Module.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.14.5.functools.Module.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.14.5.functools.Module.txt",

                    "size": 41844111,

                    "description": "13 2 14 5 functools Module"

                },
                {

                    "name": "13.2.15.1.Homework.Review.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.15.1.Homework.Review.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.15.1.Homework.Review.txt",

                    "size": 48448241,

                    "description": "13 2 15 1 Homework Review"

                },
                {

                    "name": "13.2.15.2.Multiple.Inheritance.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.15.2.Multiple.Inheritance.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.15.2.Multiple.Inheritance.txt",

                    "size": 79453863,

                    "description": "13 2 15 2 Multiple Inheritance"

                },
                {

                    "name": "13.2.15.3.Multiple.Inheritance.Mixins.and.Abstract.Classes.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.15.3.Multiple.Inheritance.Mixins.and.Abstract.Classes.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.15.3.Multiple.Inheritance.Mixins.and.Abstract.Classes.txt",

                    "size": 88810224,

                    "description": "13 2 15 3 Multiple Inheritance Mixins and Abstract Classes"

                },
                {

                    "name": "13.2.15.4.Class.as.Context.Manager.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.15.4.Class.as.Context.Manager.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.15.4.Class.as.Context.Manager.txt",

                    "size": 63954137,

                    "description": "13 2 15 4 Class as Context Manager"

                },
                {

                    "name": "13.2.15.5.Class.Methods.Decorators.Setter.and.Property.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.15.5.Class.Methods.Decorators.Setter.and.Property.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.15.5.Class.Methods.Decorators.Setter.and.Property.txt",

                    "size": 56219533,

                    "description": "13 2 15 5 Class Methods Decorators Setter and Property"

                },
                {

                    "name": "13.2.15.6.Class.Methods.Decorator.Classmethod.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.15.6.Class.Methods.Decorator.Classmethod.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.15.6.Class.Methods.Decorator.Classmethod.txt",

                    "size": 44526349,

                    "description": "13 2 15 6 Class Methods Decorator Classmethod"

                },
                {

                    "name": "13.2.16.1.Homework.Review.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.16.1.Homework.Review.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.16.1.Homework.Review.txt",

                    "size": 78199294,

                    "description": "13 2 16 1 Homework Review"

                },
                {

                    "name": "13.2.16.2.Decorator.Context.Manager.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.16.2.Decorator.Context.Manager.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.16.2.Decorator.Context.Manager.txt",

                    "size": 80323214,

                    "description": "13 2 16 2 Decorator Context Manager"

                },
                {

                    "name": "13.2.16.3.Decorators.With.Arguments.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.16.3.Decorators.With.Arguments.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.16.3.Decorators.With.Arguments.txt",

                    "size": 79042380,

                    "description": "13 2 16 3 Decorators With Arguments"

                },
                {

                    "name": "13.2.16.4.Decorators.For.Classes.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.16.4.Decorators.For.Classes.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.16.4.Decorators.For.Classes.txt",

                    "size": 107237858,

                    "description": "13 2 16 4 Decorators For Classes"

                },
                {

                    "name": "13.2.16.5.Decorator.As.Class.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.16.5.Decorator.As.Class.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.16.5.Decorator.As.Class.txt",

                    "size": 48163965,

                    "description": "13 2 16 5 Decorator As Class"

                },
                {

                    "name": "13.2.17.1.Homework.Review.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.17.1.Homework.Review.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.17.1.Homework.Review.txt",

                    "size": 116213700,

                    "description": "13 2 17 1 Homework Review"

                },
                {

                    "name": "13.2.17.2.Namespace.And.Scope.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.17.2.Namespace.And.Scope.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.17.2.Namespace.And.Scope.txt",

                    "size": 84655677,

                    "description": "13 2 17 2 Namespace And Scope"

                },
                {

                    "name": "13.2.17.3.Lambda.Functions.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.17.3.Lambda.Functions.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.17.3.Lambda.Functions.txt",

                    "size": 51065246,

                    "description": "13 2 17 3 Lambda Functions"

                },
                {

                    "name": "13.2.17.4.Map.And.Filter.Functions.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.17.4.Map.And.Filter.Functions.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.17.4.Map.And.Filter.Functions.txt",

                    "size": 81472657,

                    "description": "13 2 17 4 Map And Filter Functions"

                },
                {

                    "name": "13.2.17.5.Special.Variable.Name.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.17.5.Special.Variable.Name.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.17.5.Special.Variable.Name.txt",

                    "size": 56240711,

                    "description": "13 2 17 5 Special Variable Name"

                },
                {

                    "name": "13.2.18.1.Homework.Review.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.18.1.Homework.Review.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.18.1.Homework.Review.txt",

                    "size": 43041053,

                    "description": "13 2 18 1 Homework Review"

                },
                {

                    "name": "13.2.18.2.Regular.Expressions.Re.Module.And.Methods.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.18.2.Regular.Expressions.Re.Module.And.Methods.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.18.2.Regular.Expressions.Re.Module.And.Methods.txt",

                    "size": 71774327,

                    "description": "13 2 18 2 Regular Expressions Re Module And Methods"

                },
                {

                    "name": "13.2.18.3.Regular.Expressions.Patterns.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.18.3.Regular.Expressions.Patterns.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.18.3.Regular.Expressions.Patterns.txt",

                    "size": 98974005,

                    "description": "13 2 18 3 Regular Expressions Patterns"

                },
                {

                    "name": "13.2.18.4.Parsing.Basics.Requests.Module.And.JSON.Format.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.18.4.Parsing.Basics.Requests.Module.And.JSON.Format.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.18.4.Parsing.Basics.Requests.Module.And.JSON.Format.txt",

                    "size": 95239983,

                    "description": "13 2 18 4 Parsing Basics Requests Module And JSON Format"

                },
                {

                    "name": "13.2.18.5.Itertools.Module.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.18.5.Itertools.Module.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.18.5.Itertools.Module.txt",

                    "size": 64012153,

                    "description": "13 2 18 5 Itertools Module"

                },
                {

                    "name": "13.2.2.1.Lists.and.Their.Initialization.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.2.1.Lists.and.Their.Initialization.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.2.1.Lists.and.Their.Initialization.txt",

                    "size": 169864810,

                    "description": "13 2 2 1 Lists and Their Initialization"

                },
                {

                    "name": "13.2.2.2.Indexes.Working.with.List.Elements.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.2.2.Indexes.Working.with.List.Elements.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.2.2.Indexes.Working.with.List.Elements.txt",

                    "size": 149021955,

                    "description": "13 2 2 2 Indexes Working with List Elements"

                },
                {

                    "name": "13.2.2.3.Lists.Working.with.Strings.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.2.3.Lists.Working.with.Strings.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.2.3.Lists.Working.with.Strings.txt",

                    "size": 131010762,

                    "description": "13 2 2 3 Lists Working with Strings"

                },
                {

                    "name": "13.2.2.4.Basic.Capabilities.when.Working.with.Lists.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.2.4.Basic.Capabilities.when.Working.with.Lists.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.2.4.Basic.Capabilities.when.Working.with.Lists.txt",

                    "size": 142748123,

                    "description": "13 2 2 4 Basic Capabilities when Working with Lists"

                },
                {

                    "name": "13.2.3.1.Homework.Review.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.3.1.Homework.Review.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.3.1.Homework.Review.txt",

                    "size": 132114294,

                    "description": "13 2 3 1 Homework Review"

                },
                {

                    "name": "13.2.3.2.Working.with.Lists.Insert.Remove.Index.Methods.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.3.2.Working.with.Lists.Insert.Remove.Index.Methods.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.3.2.Working.with.Lists.Insert.Remove.Index.Methods.txt",

                    "size": 229808008,

                    "description": "13 2 3 2 Working with Lists Insert Remove Index Methods"

                },
                {

                    "name": "13.2.3.3.Working.with.Multiple.Lists.Extend.and.Count.Methods.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.3.3.Working.with.Multiple.Lists.Extend.and.Count.Methods.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.3.3.Working.with.Multiple.Lists.Extend.and.Count.Methods.txt",

                    "size": 115267805,

                    "description": "13 2 3 3 Working with Multiple Lists Extend and Count Methods"

                },
                {

                    "name": "13.2.3.4.Nested.Lists.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.3.4.Nested.Lists.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.3.4.Nested.Lists.txt",

                    "size": 173419369,

                    "description": "13 2 3 4 Nested Lists"

                },
                {

                    "name": "13.2.4.1.Homework.Review.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.4.1.Homework.Review.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.4.1.Homework.Review.txt",

                    "size": 86887113,

                    "description": "13 2 4 1 Homework Review"

                },
                {

                    "name": "13.2.4.2.List.Comprehensions.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.4.2.List.Comprehensions.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.4.2.List.Comprehensions.txt",

                    "size": 59662850,

                    "description": "13 2 4 2 List Comprehensions"

                },
                {

                    "name": "13.2.4.3.List.Comprehensions.with.Conditions.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.4.3.List.Comprehensions.with.Conditions.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.4.3.List.Comprehensions.with.Conditions.txt",

                    "size": 78947342,

                    "description": "13 2 4 3 List Comprehensions with Conditions"

                },
                {

                    "name": "13.2.4.4.List.Slices.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.4.4.List.Slices.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.4.4.List.Slices.txt",

                    "size": 93218138,

                    "description": "13 2 4 4 List Slices"

                },
                {

                    "name": "13.2.4.5.Strings.Indices.and.Slices.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.4.5.Strings.Indices.and.Slices.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.4.5.Strings.Indices.and.Slices.txt",

                    "size": 86501141,

                    "description": "13 2 4 5 Strings Indices and Slices"

                },
                {

                    "name": "13.2.4.6.Outro.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.4.6.Outro.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.4.6.Outro.txt",

                    "size": 8398909,

                    "description": "13 2 4 6 Outro"

                },
                {

                    "name": "13.2.5.1.Homework.Review.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.5.1.Homework.Review.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.5.1.Homework.Review.txt",

                    "size": 119126931,

                    "description": "13 2 5 1 Homework Review"

                },
                {

                    "name": "13.2.5.2.String.Formatting.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.5.2.String.Formatting.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.5.2.String.Formatting.txt",

                    "size": 132945585,

                    "description": "13 2 5 2 String Formatting"

                },
                {

                    "name": "13.2.5.3.String.Methods.Split.Join.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.5.3.String.Methods.Split.Join.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.5.3.String.Methods.Split.Join.txt",

                    "size": 157791496,

                    "description": "13 2 5 3 String Methods Split Join"

                },
                {

                    "name": "13.2.5.4.String.Methods.Startswith.Endswith.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.5.4.String.Methods.Startswith.Endswith.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.5.4.String.Methods.Startswith.Endswith.txt",

                    "size": 140660626,

                    "description": "13 2 5 4 String Methods Startswith Endswith"

                },
                {

                    "name": "13.2.5.5.String.Formatting.Substitutions.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.5.5.String.Formatting.Substitutions.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.5.5.String.Formatting.Substitutions.txt",

                    "size": 84210795,

                    "description": "13 2 5 5 String Formatting Substitutions"

                },
                {

                    "name": "13.2.6.1.Dictionary.Basics.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.6.1.Dictionary.Basics.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.6.1.Dictionary.Basics.txt",

                    "size": 122988534,

                    "description": "13 2 6 1 Dictionary Basics"

                },
                {

                    "name": "13.2.6.2.Dictionary.Methods.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.6.2.Dictionary.Methods.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.6.2.Dictionary.Methods.txt",

                    "size": 112800462,

                    "description": "13 2 6 2 Dictionary Methods"

                },
                {

                    "name": "13.2.6.3.Nested.Dictionaries.Default.Get.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.6.3.Nested.Dictionaries.Default.Get.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.6.3.Nested.Dictionaries.Default.Get.txt",

                    "size": 96689996,

                    "description": "13 2 6 3 Nested Dictionaries Default Get"

                },
                {

                    "name": "13.2.6.4.Sets.Function.Set.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.6.4.Sets.Function.Set.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.6.4.Sets.Function.Set.txt",

                    "size": 66505637,

                    "description": "13 2 6 4 Sets Function Set"

                },
                {

                    "name": "13.2.6.5.Dictionary.Generation.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.6.5.Dictionary.Generation.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.6.5.Dictionary.Generation.txt",

                    "size": 138927344,

                    "description": "13 2 6 5 Dictionary Generation"

                },
                {

                    "name": "13.2.7.1.Homework.Review.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.7.1.Homework.Review.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.7.1.Homework.Review.txt",

                    "size": 52970511,

                    "description": "13 2 7 1 Homework Review"

                },
                {

                    "name": "13.2.7.2.Tuples.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.7.2.Tuples.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.7.2.Tuples.txt",

                    "size": 112469424,

                    "description": "13 2 7 2 Tuples"

                },
                {

                    "name": "13.2.7.3.Enumerate.Function.Iterating.Multiple.Values.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.7.3.Enumerate.Function.Iterating.Multiple.Values.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.7.3.Enumerate.Function.Iterating.Multiple.Values.txt",

                    "size": 83114226,

                    "description": "13 2 7 3 Enumerate Function Iterating Multiple Values"

                },
                {

                    "name": "13.2.7.4.Iterating.Keys.Values.In.Dictionary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.7.4.Iterating.Keys.Values.In.Dictionary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.7.4.Iterating.Keys.Values.In.Dictionary.txt",

                    "size": 73048470,

                    "description": "13 2 7 4 Iterating Keys Values In Dictionary"

                },
                {

                    "name": "13.2.7.5.Composite.Keys.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.7.5.Composite.Keys.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.7.5.Composite.Keys.txt",

                    "size": 60813094,

                    "description": "13 2 7 5 Composite Keys"

                },
                {

                    "name": "13.2.7.6.Zip.Function.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.7.6.Zip.Function.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.7.6.Zip.Function.txt",

                    "size": 109250796,

                    "description": "13 2 7 6 Zip Function"

                },
                {

                    "name": "13.2.7.7.Outro.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.7.7.Outro.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.7.7.Outro.txt",

                    "size": 7668014,

                    "description": "13 2 7 7 Outro"

                },
                {

                    "name": "13.2.8.1.Homework.Review.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.8.1.Homework.Review.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.8.1.Homework.Review.txt",

                    "size": 57326526,

                    "description": "13 2 8 1 Homework Review"

                },
                {

                    "name": "13.2.8.2.Recursion.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.8.2.Recursion.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.8.2.Recursion.txt",

                    "size": 107418197,

                    "description": "13 2 8 2 Recursion"

                },
                {

                    "name": "13.2.8.4.Passing.Mutable.Immutable.Data.to.Function.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.8.4.Passing.Mutable.Immutable.Data.to.Function.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.8.4.Passing.Mutable.Immutable.Data.to.Function.txt",

                    "size": 55597936,

                    "description": "13 2 8 4 Passing Mutable Immutable Data to Function"

                },
                {

                    "name": "13.2.8.6.Named.Arguments.and.Default.Values.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.8.6.Named.Arguments.and.Default.Values.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.8.6.Named.Arguments.and.Default.Values.txt",

                    "size": 104627344,

                    "description": "13 2 8 6 Named Arguments and Default Values"

                },
                {

                    "name": "13.2.8.7.Args.and.Kwargs.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.8.7.Args.and.Kwargs.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.8.7.Args.and.Kwargs.txt",

                    "size": 117666607,

                    "description": "13 2 8 7 Args and Kwargs"

                },
                {

                    "name": "13.2.9.1.Os.Module.Path.Generation.and.Listdir.Method.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.9.1.Os.Module.Path.Generation.and.Listdir.Method.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.9.1.Os.Module.Path.Generation.and.Listdir.Method.txt",

                    "size": 127166622,

                    "description": "13 2 9 1 Os Module Path Generation and Listdir Method"

                },
                {

                    "name": "13.2.9.2.Os.Module.Checks.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.9.2.Os.Module.Checks.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.9.2.Os.Module.Checks.txt",

                    "size": 91779498,

                    "description": "13 2 9 2 Os Module Checks"

                },
                {

                    "name": "13.2.9.3.Basic.File.Operations.Open.Close.Read.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.9.3.Basic.File.Operations.Open.Close.Read.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.9.3.Basic.File.Operations.Open.Close.Read.txt",

                    "size": 96251691,

                    "description": "13 2 9 3 Basic File Operations Open Close Read"

                },
                {

                    "name": "13.2.9.4.Write.Method.Write.Modes.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.9.4.Write.Method.Write.Modes.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.9.4.Write.Method.Write.Modes.txt",

                    "size": 90025100,

                    "description": "13 2 9 4 Write Method Write Modes"

                },
                {

                    "name": "13.2.9.5.Moving.Cursor.in.File.Seek.Method.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.9.5.Moving.Cursor.in.File.Seek.Method.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.2.9.5.Moving.Cursor.in.File.Seek.Method.txt",

                    "size": 52423136,

                    "description": "13 2 9 5 Moving Cursor in File Seek Method"

                },
                {

                    "name": "13.3.1.1.Intro.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.1.1.Intro.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.1.1.Intro.txt",

                    "size": 19834617,

                    "description": "13 3 1 1 Intro"

                },
                {

                    "name": "13.3.1.2.OSI.Model.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.1.2.OSI.Model.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.1.2.OSI.Model.txt",

                    "size": 52856023,

                    "description": "13 3 1 2 OSI Model"

                },
                {

                    "name": "13.3.1.3.OSI.Levels.Analysis.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.1.3.OSI.Levels.Analysis.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.1.3.OSI.Levels.Analysis.txt",

                    "size": 73690547,

                    "description": "13 3 1 3 OSI Levels Analysis"

                },
                {

                    "name": "13.3.1.4.TCP.IP.Protocol.and.Stack.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.1.4.TCP.IP.Protocol.and.Stack.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.1.4.TCP.IP.Protocol.and.Stack.txt",

                    "size": 112205995,

                    "description": "13 3 1 4 TCP IP Protocol and Stack"

                },
                {

                    "name": "13.3.1.5.UDP.Protocol.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.1.5.UDP.Protocol.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.1.5.UDP.Protocol.txt",

                    "size": 33854623,

                    "description": "13 3 1 5 UDP Protocol"

                },
                {

                    "name": "13.3.1.6.Protocols.Comparison.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.1.6.Protocols.Comparison.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.1.6.Protocols.Comparison.txt",

                    "size": 43575875,

                    "description": "13 3 1 6 Protocols Comparison"

                },
                {

                    "name": "13.3.10.1.FireWall.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.10.1.FireWall.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.10.1.FireWall.txt",

                    "size": 78463347,

                    "description": "13 3 10 1 FireWall"

                },
                {

                    "name": "13.3.10.2.FirewallArchitecture.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.10.2.FirewallArchitecture.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.10.2.FirewallArchitecture.txt",

                    "size": 121882912,

                    "description": "13 3 10 2 FirewallArchitecture"

                },
                {

                    "name": "13.3.10.3.FirewallSetup.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.10.3.FirewallSetup.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.10.3.FirewallSetup.txt",

                    "size": 302977576,

                    "description": "13 3 10 3 FirewallSetup"

                },
                {

                    "name": "13.3.2.1.DNS.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.2.1.DNS.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.2.1.DNS.txt",

                    "size": 38216775,

                    "description": "13 3 2 1 DNS"

                },
                {

                    "name": "13.3.2.2.DHCP.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.2.2.DHCP.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.2.2.DHCP.txt",

                    "size": 302258139,

                    "description": "13 3 2 2 DHCP"

                },
                {

                    "name": "13.3.2.3.NAT.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.2.3.NAT.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.2.3.NAT.txt",

                    "size": 341263744,

                    "description": "13 3 2 3 NAT"

                },
                {

                    "name": "13.3.2.4.NTP.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.2.4.NTP.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.2.4.NTP.txt",

                    "size": 132767966,

                    "description": "13 3 2 4 NTP"

                },
                {

                    "name": "13.3.3.1.NetworkDesignBasics.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.3.1.NetworkDesignBasics.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.3.1.NetworkDesignBasics.txt",

                    "size": 77481908,

                    "description": "13 3 3 1 NetworkDesignBasics"

                },
                {

                    "name": "13.3.3.2.RoleDistribution.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.3.2.RoleDistribution.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.3.2.RoleDistribution.txt",

                    "size": 185264280,

                    "description": "13 3 3 2 RoleDistribution"

                },
                {

                    "name": "13.3.3.3.NetworkBuildingConcept.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.3.3.NetworkBuildingConcept.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.3.3.NetworkBuildingConcept.txt",

                    "size": 239652640,

                    "description": "13 3 3 3 NetworkBuildingConcept"

                },
                {

                    "name": "13.3.4.1.NetworkScalingVLAN.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.4.1.NetworkScalingVLAN.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.4.1.NetworkScalingVLAN.txt",

                    "size": 240671875,

                    "description": "13 3 4 1 NetworkScalingVLAN"

                },
                {

                    "name": "13.3.4.2.Layer3Switching.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.4.2.Layer3Switching.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.4.2.Layer3Switching.txt",

                    "size": 90070637,

                    "description": "13 3 4 2 Layer3Switching"

                },
                {

                    "name": "13.3.4.3.LinkAggregation.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.4.3.LinkAggregation.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.4.3.LinkAggregation.txt",

                    "size": 104729685,

                    "description": "13 3 4 3 LinkAggregation"

                },
                {

                    "name": "13.3.4.4.FirstHopRedundancyProtocols.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.4.4.FirstHopRedundancyProtocols.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.4.4.FirstHopRedundancyProtocols.txt",

                    "size": 131758267,

                    "description": "13 3 4 4 FirstHopRedundancyProtocols"

                },
                {

                    "name": "13.3.4.5.ChannelAggregationProtocolsConfiguration.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.4.5.ChannelAggregationProtocolsConfiguration.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.4.5.ChannelAggregationProtocolsConfiguration.txt",

                    "size": 716132238,

                    "description": "13 3 4 5 ChannelAggregationProtocolsConfiguration"

                },
                {

                    "name": "13.3.5.1.DynamicRoutingProtocols.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.5.1.DynamicRoutingProtocols.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.5.1.DynamicRoutingProtocols.txt",

                    "size": 192335636,

                    "description": "13 3 5 1 DynamicRoutingProtocols"

                },
                {

                    "name": "13.3.5.2.OSPFCharacteristics.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.5.2.OSPFCharacteristics.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.5.2.OSPFCharacteristics.txt",

                    "size": 166968631,

                    "description": "13 3 5 2 OSPFCharacteristics"

                },
                {

                    "name": "13.3.5.3.OSPFPacketTypes.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.5.3.OSPFPacketTypes.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.5.3.OSPFPacketTypes.txt",

                    "size": 159262567,

                    "description": "13 3 5 3 OSPFPacketTypes"

                },
                {

                    "name": "13.3.5.4.OSPFv2SingleAreaConfiguration.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.5.4.OSPFv2SingleAreaConfiguration.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.5.4.OSPFv2SingleAreaConfiguration.txt",

                    "size": 415724769,

                    "description": "13 3 5 4 OSPFv2SingleAreaConfiguration"

                },
                {

                    "name": "13.3.6.1.BGPBasic.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.6.1.BGPBasic.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.6.1.BGPBasic.txt",

                    "size": 103843898,

                    "description": "13 3 6 1 BGPBasic"

                },
                {

                    "name": "13.3.6.2.BGPBasicAdvanced.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.6.2.BGPBasicAdvanced.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.6.2.BGPBasicAdvanced.txt",

                    "size": 368782274,

                    "description": "13 3 6 2 BGPBasicAdvanced"

                },
                {

                    "name": "13.3.6.3.BGPAttributes.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.6.3.BGPAttributes.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.6.3.BGPAttributes.txt",

                    "size": 213677801,

                    "description": "13 3 6 3 BGPAttributes"

                },
                {

                    "name": "13.3.6.4.BGPProtocolConfiguration.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.6.4.BGPProtocolConfiguration.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.6.4.BGPProtocolConfiguration.txt",

                    "size": 382896005,

                    "description": "13 3 6 4 BGPProtocolConfiguration"

                },
                {

                    "name": "13.3.7.1.IPv4Protocol.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.7.1.IPv4Protocol.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.7.1.IPv4Protocol.txt",

                    "size": 977584700,

                    "description": "13 3 7 1 IPv4Protocol"

                },
                {

                    "name": "13.3.7.2.IPv6Protocol.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.7.2.IPv6Protocol.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.7.2.IPv6Protocol.txt",

                    "size": 496782004,

                    "description": "13 3 7 2 IPv6Protocol"

                },
                {

                    "name": "13.3.7.3.IPv6NetworkPrefixAcquisition.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.7.3.IPv6NetworkPrefixAcquisition.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.7.3.IPv6NetworkPrefixAcquisition.txt",

                    "size": 367213143,

                    "description": "13 3 7 3 IPv6NetworkPrefixAcquisition"

                },
                {

                    "name": "13.3.7.4.IPv6PracticeConfiguration.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.7.4.IPv6PracticeConfiguration.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.7.4.IPv6PracticeConfiguration.txt",

                    "size": 252664331,

                    "description": "13 3 7 4 IPv6PracticeConfiguration"

                },
                {

                    "name": "13.3.8.1.Introduction.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.8.1.Introduction.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.8.1.Introduction.txt",

                    "size": 36636401,

                    "description": "13 3 8 1 Introduction"

                },
                {

                    "name": "13.3.8.2.GRE.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.8.2.GRE.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.8.2.GRE.txt",

                    "size": 605866544,

                    "description": "13 3 8 2 GRE"

                },
                {

                    "name": "13.3.8.3.IPSecBasic.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.8.3.IPSecBasic.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.8.3.IPSecBasic.txt",

                    "size": 349570040,

                    "description": "13 3 8 3 IPSecBasic"

                },
                {

                    "name": "13.3.8.4.IPSecAdvancedESPAH.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.8.4.IPSecAdvancedESPAH.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.8.4.IPSecAdvancedESPAH.txt",

                    "size": 278793951,

                    "description": "13 3 8 4 IPSecAdvancedESPAH"

                },
                {

                    "name": "13.3.8.5.IPSecAdvancedIKE.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.8.5.IPSecAdvancedIKE.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.8.5.IPSecAdvancedIKE.txt",

                    "size": 336054694,

                    "description": "13 3 8 5 IPSecAdvancedIKE"

                },
                {

                    "name": "13.3.8.6.VPN.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.8.6.VPN.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.8.6.VPN.txt",

                    "size": 114603495,

                    "description": "13 3 8 6 VPN"

                },
                {

                    "name": "13.3.9.1.ACL.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.9.1.ACL.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.9.1.ACL.txt",

                    "size": 73598987,

                    "description": "13 3 9 1 ACL"

                },
                {

                    "name": "13.3.9.2.AAA.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.9.2.AAA.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.9.2.AAA.txt",

                    "size": 69563490,

                    "description": "13 3 9 2 AAA"

                },
                {

                    "name": "13.3.9.3.L2Security.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.9.3.L2Security.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/13.0.0/13.3.9.3.L2Security.txt",

                    "size": 139129406,

                    "description": "13 3 9 3 L2Security"

                }
        ],
        "12.0.0": [
                {

                    "name": "12.1.1.Intro.to.the.Course.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.1.1.Intro.to.the.Course.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.1.1.Intro.to.the.Course.txt",

                    "size": 11685326,

                    "description": "12 1 1 Intro to the Course"

                },
                {

                    "name": "12.1.2.Introduction.to.Application.Security.Analysis.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.1.2.Introduction.to.Application.Security.Analysis.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.1.2.Introduction.to.Application.Security.Analysis.txt",

                    "size": 3773419,

                    "description": "12 1 2 Introduction to Application Security Analysis"

                },
                {

                    "name": "12.1.3.Security.Analysis.Using.White.Box.Method.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.1.3.Security.Analysis.Using.White.Box.Method.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.1.3.Security.Analysis.Using.White.Box.Method.txt",

                    "size": 3116458,

                    "description": "12 1 3 Security Analysis Using White Box Method"

                },
                {

                    "name": "12.1.4.Process.of.Conducting.Security.Analysis.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.1.4.Process.of.Conducting.Security.Analysis.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.1.4.Process.of.Conducting.Security.Analysis.txt",

                    "size": 3900033,

                    "description": "12 1 4 Process of Conducting Security Analysis"

                },
                {

                    "name": "12.1.5.Classification.of.Vulnerabilities.and.Ranking.by.Criticality.Levels.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.1.5.Classification.of.Vulnerabilities.and.Ranking.by.Criticality.Levels.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.1.5.Classification.of.Vulnerabilities.and.Ranking.by.Criticality.Levels.txt",

                    "size": 3826644,

                    "description": "12 1 5 Classification of Vulnerabilities and Ranking by Criticality Levels"

                },
                {

                    "name": "12.1.6.Module.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.1.6.Module.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.1.6.Module.Summary.txt",

                    "size": 10428492,

                    "description": "12 1 6 Module Summary"

                },
                {

                    "name": "12.2.1.Intro.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.2.1.Intro.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.2.1.Intro.txt",

                    "size": 13634456,

                    "description": "12 2 1 Intro"

                },
                {

                    "name": "12.2.2.Concept.and.Types.of.Cross-Site.Scripting.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.2.2.Concept.and.Types.of.Cross-Site.Scripting.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.2.2.Concept.and.Types.of.Cross-Site.Scripting.txt",

                    "size": 6574515,

                    "description": "12 2 2 Concept and Types of Cross-Site Scripting"

                },
                {

                    "name": "12.2.3.Burp.Suite.Setup.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.2.3.Burp.Suite.Setup.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.2.3.Burp.Suite.Setup.txt",

                    "size": 35491113,

                    "description": "12 2 3 Burp Suite Setup"

                },
                {

                    "name": "12.2.4.Finding.XSS.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.2.4.Finding.XSS.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.2.4.Finding.XSS.txt",

                    "size": 108277251,

                    "description": "12 2 4 Finding XSS"

                },
                {

                    "name": "12.2.5.Preventing.XSS.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.2.5.Preventing.XSS.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.2.5.Preventing.XSS.txt",

                    "size": 6091020,

                    "description": "12 2 5 Preventing XSS"

                },
                {

                    "name": "12.2.6.Module.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.2.6.Module.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.2.6.Module.Summary.txt",

                    "size": 36718329,

                    "description": "12 2 6 Module Summary"

                },
                {

                    "name": "12.3.1.Intro.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.3.1.Intro.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.3.1.Intro.txt",

                    "size": 4695245,

                    "description": "12 3 1 Intro"

                },
                {

                    "name": "12.3.2.Web.Application.Structure.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.3.2.Web.Application.Structure.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.3.2.Web.Application.Structure.txt",

                    "size": 3799944,

                    "description": "12 3 2 Web Application Structure"

                },
                {

                    "name": "12.3.3.Types.of.SQL.Injections.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.3.3.Types.of.SQL.Injections.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.3.3.Types.of.SQL.Injections.txt",

                    "size": 61889213,

                    "description": "12 3 3 Types of SQL Injections"

                },
                {

                    "name": "12.3.4.Sqlmap.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.3.4.Sqlmap.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.3.4.Sqlmap.txt",

                    "size": 51211178,

                    "description": "12 3 4 Sqlmap"

                },
                {

                    "name": "12.3.5.Detecting.SQL.Injections.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.3.5.Detecting.SQL.Injections.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.3.5.Detecting.SQL.Injections.txt",

                    "size": 170761519,

                    "description": "12 3 5 Detecting SQL Injections"

                },
                {

                    "name": "12.3.6.Preventing.SQL.Injections.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.3.6.Preventing.SQL.Injections.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.3.6.Preventing.SQL.Injections.txt",

                    "size": 23163171,

                    "description": "12 3 6 Preventing SQL Injections"

                },
                {

                    "name": "12.3.7.Module.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.3.7.Module.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.3.7.Module.Summary.txt",

                    "size": 18828461,

                    "description": "12 3 7 Module Summary"

                },
                {

                    "name": "12.4.1.Intro.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.4.1.Intro.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.4.1.Intro.txt",

                    "size": 28847698,

                    "description": "12 4 1 Intro"

                },
                {

                    "name": "12.4.2.Web.Application.Structure.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.4.2.Web.Application.Structure.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.4.2.Web.Application.Structure.txt",

                    "size": 17149282,

                    "description": "12 4 2 Web Application Structure"

                },
                {

                    "name": "12.4.3.Path.Traversal.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.4.3.Path.Traversal.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.4.3.Path.Traversal.txt",

                    "size": 60510418,

                    "description": "12 4 3 Path Traversal"

                },
                {

                    "name": "12.4.4.IDOR.File.Enumeration.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.4.4.IDOR.File.Enumeration.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.4.4.IDOR.File.Enumeration.txt",

                    "size": 73293007,

                    "description": "12 4 4 IDOR File Enumeration"

                },
                {

                    "name": "12.4.5.IDOR.for.Retrieving.Arbitrary.Data.from.Database.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.4.5.IDOR.for.Retrieving.Arbitrary.Data.from.Database.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.4.5.IDOR.for.Retrieving.Arbitrary.Data.from.Database.txt",

                    "size": 46455721,

                    "description": "12 4 5 IDOR for Retrieving Arbitrary Data from Database"

                },
                {

                    "name": "12.4.6.Module.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.4.6.Module.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.4.6.Module.Summary.txt",

                    "size": 58035388,

                    "description": "12 4 6 Module Summary"

                },
                {

                    "name": "12.5.1.Intro.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.5.1.Intro.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.5.1.Intro.txt",

                    "size": 7140161,

                    "description": "12 5 1 Intro"

                },
                {

                    "name": "12.5.2.User.Session.Management.in.Web.Applications.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.5.2.User.Session.Management.in.Web.Applications.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.5.2.User.Session.Management.in.Web.Applications.txt",

                    "size": 4376506,

                    "description": "12 5 2 User Session Management in Web Applications"

                },
                {

                    "name": "12.5.3.CSRF.Attacks.in.Practice.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.5.3.CSRF.Attacks.in.Practice.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.5.3.CSRF.Attacks.in.Practice.txt",

                    "size": 115258469,

                    "description": "12 5 3 CSRF Attacks in Practice"

                },
                {

                    "name": "12.5.4.Preventing.CSRF.Attacks.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.5.4.Preventing.CSRF.Attacks.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.5.4.Preventing.CSRF.Attacks.txt",

                    "size": 3771641,

                    "description": "12 5 4 Preventing CSRF Attacks"

                },
                {

                    "name": "12.5.5.Module.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.5.5.Module.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.5.5.Module.Summary.txt",

                    "size": 13977579,

                    "description": "12 5 5 Module Summary"

                },
                {

                    "name": "12.6.1.Intro.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.6.1.Intro.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.6.1.Intro.txt",

                    "size": 40184410,

                    "description": "12 6 1 Intro"

                },
                {

                    "name": "12.6.2.Web.Application.Structure.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.6.2.Web.Application.Structure.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.6.2.Web.Application.Structure.txt",

                    "size": 12286713,

                    "description": "12 6 2 Web Application Structure"

                },
                {

                    "name": "12.6.3.Using.XML.Documents.in.Web.Applications.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.6.3.Using.XML.Documents.in.Web.Applications.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.6.3.Using.XML.Documents.in.Web.Applications.txt",

                    "size": 15865352,

                    "description": "12 6 3 Using XML Documents in Web Applications"

                },
                {

                    "name": "12.6.4.Searching.and.Exploiting.XXE.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.6.4.Searching.and.Exploiting.XXE.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.6.4.Searching.and.Exploiting.XXE.txt",

                    "size": 46096939,

                    "description": "12 6 4 Searching and Exploiting XXE"

                },
                {

                    "name": "12.6.5.Preventing.XXE.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.6.5.Preventing.XXE.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.6.5.Preventing.XXE.txt",

                    "size": 17128731,

                    "description": "12 6 5 Preventing XXE"

                },
                {

                    "name": "12.6.6.Analysis.of.Log4j.Vulnerability.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.6.6.Analysis.of.Log4j.Vulnerability.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.6.6.Analysis.of.Log4j.Vulnerability.txt",

                    "size": 135673449,

                    "description": "12 6 6 Analysis of Log4j Vulnerability"

                },
                {

                    "name": "12.6.7.Searching.for.Vulnerabilities.in.Third-Party.Libraries.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.6.7.Searching.for.Vulnerabilities.in.Third-Party.Libraries.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.6.7.Searching.for.Vulnerabilities.in.Third-Party.Libraries.txt",

                    "size": 86847182,

                    "description": "12 6 7 Searching for Vulnerabilities in Third-Party Libraries"

                },
                {

                    "name": "12.6.8.Module.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.6.8.Module.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.6.8.Module.Summary.txt",

                    "size": 34994619,

                    "description": "12 6 8 Module Summary"

                },
                {

                    "name": "12.7.1.Introduction.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.7.1.Introduction.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.7.1.Introduction.txt",

                    "size": 19925437,

                    "description": "12 7 1 Introduction"

                },
                {

                    "name": "12.7.2.SAST.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.7.2.SAST.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.7.2.SAST.txt",

                    "size": 15108385,

                    "description": "12 7 2 SAST"

                },
                {

                    "name": "12.7.3.SonarQube.Setup.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.7.3.SonarQube.Setup.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.7.3.SonarQube.Setup.txt",

                    "size": 63547838,

                    "description": "12 7 3 SonarQube Setup"

                },
                {

                    "name": "12.7.4.Vulnerability.Detection.with.SonarQube.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.7.4.Vulnerability.Detection.with.SonarQube.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.7.4.Vulnerability.Detection.with.SonarQube.txt",

                    "size": 127455173,

                    "description": "12 7 4 Vulnerability Detection with SonarQube"

                },
                {

                    "name": "12.7.5.Module.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.7.5.Module.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.7.5.Module.Summary.txt",

                    "size": 35393720,

                    "description": "12 7 5 Module Summary"

                },
                {

                    "name": "12.8.1.Introduction.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.8.1.Introduction.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.8.1.Introduction.txt",

                    "size": 6830399,

                    "description": "12 8 1 Introduction"

                },
                {

                    "name": "12.8.2.Web.Application.Firewall.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.8.2.Web.Application.Firewall.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.8.2.Web.Application.Firewall.txt",

                    "size": 4132387,

                    "description": "12 8 2 Web Application Firewall"

                },
                {

                    "name": "12.8.3.Vulnerabilities.and.Web.Application.Firewall.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.8.3.Vulnerabilities.and.Web.Application.Firewall.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.8.3.Vulnerabilities.and.Web.Application.Firewall.txt",

                    "size": 4370449,

                    "description": "12 8 3 Vulnerabilities and Web Application Firewall"

                },
                {

                    "name": "12.8.4.WAF.on.Practice.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.8.4.WAF.on.Practice.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.8.4.WAF.on.Practice.txt",

                    "size": 351060323,

                    "description": "12 8 4 WAF on Practice"

                },
                {

                    "name": "12.8.5.Configuring.Content.Security.Policy.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.8.5.Configuring.Content.Security.Policy.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.8.5.Configuring.Content.Security.Policy.txt",

                    "size": 202663002,

                    "description": "12 8 5 Configuring Content Security Policy"

                },
                {

                    "name": "12.8.6.Module.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.8.6.Module.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/12.0.0/12.8.6.Module.Summary.txt",

                    "size": 12451753,

                    "description": "12 8 6 Module Summary"

                }
        ],
        "11.0.0": [
                {

                    "name": "11.1.1.Introduction.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.1.1.Introduction.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.1.1.Introduction.txt",

                    "size": 21704414,

                    "description": "11 1 1 Introduction"

                },
                {

                    "name": "11.1.2.Compliance.in.Organization.Activities.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.1.2.Compliance.in.Organization.Activities.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.1.2.Compliance.in.Organization.Activities.txt",

                    "size": 46521062,

                    "description": "11 1 2 Compliance in Organization Activities"

                },
                {

                    "name": "11.1.3.Hierarchy.of.Normative.Legal.Acts.in.the.Field.of.Information.Security.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.1.3.Hierarchy.of.Normative.Legal.Acts.in.the.Field.of.Information.Security.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.1.3.Hierarchy.of.Normative.Legal.Acts.in.the.Field.of.Information.Security.txt",

                    "size": 9691275,

                    "description": "11 1 3 Hierarchy of Normative Legal Acts in the Field of Information Security"

                },
                {

                    "name": "11.1.4.Standards.and.International.Acts.on.Information.Security.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.1.4.Standards.and.International.Acts.on.Information.Security.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.1.4.Standards.and.International.Acts.on.Information.Security.txt",

                    "size": 5869611,

                    "description": "11 1 4 Standards and International Acts on Information Security"

                },
                {

                    "name": "11.1.5.Liability.for.Violation.of.Information.Security.Requirements.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.1.5.Liability.for.Violation.of.Information.Security.Requirements.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.1.5.Liability.for.Violation.of.Information.Security.Requirements.txt",

                    "size": 5957897,

                    "description": "11 1 5 Liability for Violation of Information Security Requirements"

                },
                {

                    "name": "11.2.1.Classification.of.Organization.Information.Resources.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.2.1.Classification.of.Organization.Information.Resources.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.2.1.Classification.of.Organization.Information.Resources.txt",

                    "size": 4340595,

                    "description": "11 2 1 Classification of Organization Information Resources"

                },
                {

                    "name": "11.2.2.Basic.Concepts.of.Threat.Modeling.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.2.2.Basic.Concepts.of.Threat.Modeling.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.2.2.Basic.Concepts.of.Threat.Modeling.txt",

                    "size": 91694425,

                    "description": "11 2 2 Basic Concepts of Threat Modeling"

                },
                {

                    "name": "11.2.3.Development.of.a.List.of.Threats.to.Organization.Information.Resources.Part.1.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.2.3.Development.of.a.List.of.Threats.to.Organization.Information.Resources.Part.1.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.2.3.Development.of.a.List.of.Threats.to.Organization.Information.Resources.Part.1.txt",

                    "size": 47515469,

                    "description": "11 2 3 Development of a List of Threats to Organization Information Resources Part 1"

                },
                {

                    "name": "11.2.4.Development.of.a.List.of.Threats.to.Organization.Information.Resources.Part.2.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.2.4.Development.of.a.List.of.Threats.to.Organization.Information.Resources.Part.2.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.2.4.Development.of.a.List.of.Threats.to.Organization.Information.Resources.Part.2.txt",

                    "size": 6063965,

                    "description": "11 2 4 Development of a List of Threats to Organization Information Resources Part 2"

                },
                {

                    "name": "11.3.1.Application.of.Controls.in.Ensuring.Compliance.with.Information.Security.Requirements.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.3.1.Application.of.Controls.in.Ensuring.Compliance.with.Information.Security.Requirements.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.3.1.Application.of.Controls.in.Ensuring.Compliance.with.Information.Security.Requirements.txt",

                    "size": 12162283,

                    "description": "11 3 1 Application of Controls in Ensuring Compliance with Information Security Requirements"

                },
                {

                    "name": "11.3.2.Algorithm.for.Compiling.a.List.of.Types.of.Control.for.Information.Security.Requirements.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.3.2.Algorithm.for.Compiling.a.List.of.Types.of.Control.for.Information.Security.Requirements.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.3.2.Algorithm.for.Compiling.a.List.of.Types.of.Control.for.Information.Security.Requirements.txt",

                    "size": 6874871,

                    "description": "11 3 2 Algorithm for Compiling a List of Types of Control for Information Security Requirements"

                },
                {

                    "name": "11.3.3.Compiling.Lists.of.Controls.for.Various.Information.Security.Requirements.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.3.3.Compiling.Lists.of.Controls.for.Various.Information.Security.Requirements.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.3.3.Compiling.Lists.of.Controls.for.Various.Information.Security.Requirements.txt",

                    "size": 153472819,

                    "description": "11 3 3 Compiling Lists of Controls for Various Information Security Requirements"

                },
                {

                    "name": "11.3.4.Module.Conclusions.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.3.4.Module.Conclusions.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.3.4.Module.Conclusions.txt",

                    "size": 3387462,

                    "description": "11 3 4 Module Conclusions"

                },
                {

                    "name": "11.4.1.Methodologies.and.Basic.Models.of.Threats.to.Information.Security.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.4.1.Methodologies.and.Basic.Models.of.Threats.to.Information.Security.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.4.1.Methodologies.and.Basic.Models.of.Threats.to.Information.Security.txt",

                    "size": 89765043,

                    "description": "11 4 1 Methodologies and Basic Models of Threats to Information Security"

                },
                {

                    "name": "11.4.2.Developing.a.General.Model.of.Threats.to.Information.Security.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.4.2.Developing.a.General.Model.of.Threats.to.Information.Security.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.4.2.Developing.a.General.Model.of.Threats.to.Information.Security.txt",

                    "size": 96967628,

                    "description": "11 4 2 Developing a General Model of Threats to Information Security"

                },
                {

                    "name": "11.4.3.Developing.Private.Models.of.Threats.to.Information.Security.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.4.3.Developing.Private.Models.of.Threats.to.Information.Security.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.4.3.Developing.Private.Models.of.Threats.to.Information.Security.txt",

                    "size": 105018654,

                    "description": "11 4 3 Developing Private Models of Threats to Information Security"

                },
                {

                    "name": "11.4.4.Agreement.of.Threat.Models.with.Regulators.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.4.4.Agreement.of.Threat.Models.with.Regulators.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.4.4.Agreement.of.Threat.Models.with.Regulators.txt",

                    "size": 88514783,

                    "description": "11 4 4 Agreement of Threat Models with Regulators"

                },
                {

                    "name": "11.5.1.Hierarchy.of.Organizational.and.Administrative.Documents.on.Information.Security.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.5.1.Hierarchy.of.Organizational.and.Administrative.Documents.on.Information.Security.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.5.1.Hierarchy.of.Organizational.and.Administrative.Documents.on.Information.Security.txt",

                    "size": 11229329,

                    "description": "11 5 1 Hierarchy of Organizational and Administrative Documents on Information Security"

                },
                {

                    "name": "11.5.2.Structure.of.Organizational.and.Administrative.Documents.on.Information.Security.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.5.2.Structure.of.Organizational.and.Administrative.Documents.on.Information.Security.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.5.2.Structure.of.Organizational.and.Administrative.Documents.on.Information.Security.txt",

                    "size": 3329917,

                    "description": "11 5 2 Structure of Organizational and Administrative Documents on Information Security"

                },
                {

                    "name": "11.5.3.Development.of.the.Organization.s.Information.Security.Policy.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.5.3.Development.of.the.Organization.s.Information.Security.Policy.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.5.3.Development.of.the.Organization.s.Information.Security.Policy.txt",

                    "size": 10105952,

                    "description": "11 5 3 Development of the Organization s Information Security Policy"

                },
                {

                    "name": "11.5.4.Development.of.Regulations.and.Instructions.on.Information.Security.for.the.Company.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.5.4.Development.of.Regulations.and.Instructions.on.Information.Security.for.the.Company.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.5.4.Development.of.Regulations.and.Instructions.on.Information.Security.for.the.Company.txt",

                    "size": 8506009,

                    "description": "11 5 4 Development of Regulations and Instructions on Information Security for the Company"

                },
                {

                    "name": "11.6.1.Intro.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.6.1.Intro.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.6.1.Intro.txt",

                    "size": 7555601,

                    "description": "11 6 1 Intro"

                },
                {

                    "name": "11.6.2.Audit.of.Information.Security.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.6.2.Audit.of.Information.Security.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.6.2.Audit.of.Information.Security.txt",

                    "size": 8692935,

                    "description": "11 6 2 Audit of Information Security"

                },
                {

                    "name": "11.6.4.Regulatory.Checks.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.6.4.Regulatory.Checks.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.6.4.Regulatory.Checks.txt",

                    "size": 9386854,

                    "description": "11 6 4 Regulatory Checks"

                },
                {

                    "name": "11.6.5.Attestation.and.Certification.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.6.5.Attestation.and.Certification.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/11.0.0/11.6.5.Attestation.and.Certification.txt",

                    "size": 6777333,

                    "description": "11 6 5 Attestation and Certification"

                }
        ],
        "10.0.0": [
                {

                    "name": "10.1.1.Introduction.to.the.Course.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.1.1.Introduction.to.the.Course.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.1.1.Introduction.to.the.Course.txt",

                    "size": 76021779,

                    "description": "10 1 1 Introduction to the Course"

                },
                {

                    "name": "10.1.2.Module.Introduction.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.1.2.Module.Introduction.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.1.2.Module.Introduction.txt",

                    "size": 43813369,

                    "description": "10 1 2 Module Introduction"

                },
                {

                    "name": "10.1.3.Data.Collection.for.Inventory.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.1.3.Data.Collection.for.Inventory.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.1.3.Data.Collection.for.Inventory.txt",

                    "size": 105857633,

                    "description": "10 1 3 Data Collection for Inventory"

                },
                {

                    "name": "10.1.4.Preparation.for.Monitoring.System.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.1.4.Preparation.for.Monitoring.System.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.1.4.Preparation.for.Monitoring.System.txt",

                    "size": 66243640,

                    "description": "10 1 4 Preparation for Monitoring System"

                },
                {

                    "name": "10.1.5.Module.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.1.5.Module.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.1.5.Module.Summary.txt",

                    "size": 43265837,

                    "description": "10 1 5 Module Summary"

                },
                {

                    "name": "10.2.1.Introduction.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.2.1.Introduction.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.2.1.Introduction.txt",

                    "size": 44542802,

                    "description": "10 2 1 Introduction"

                },
                {

                    "name": "10.2.2.Threat.Modeling.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.2.2.Threat.Modeling.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.2.2.Threat.Modeling.txt",

                    "size": 71894577,

                    "description": "10 2 2 Threat Modeling"

                },
                {

                    "name": "10.2.3.Monitoring.Priorities.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.2.3.Monitoring.Priorities.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.2.3.Monitoring.Priorities.txt",

                    "size": 73009286,

                    "description": "10 2 3 Monitoring Priorities"

                },
                {

                    "name": "10.2.4.Monitoring.System.Planning.2.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.2.4.Monitoring.System.Planning.2.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.2.4.Monitoring.System.Planning.2.txt",

                    "size": 64870298,

                    "description": "10 2 4 Monitoring System Planning 2"

                },
                {

                    "name": "10.2.4.Monitoring.System.Planning.3.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.2.4.Monitoring.System.Planning.3.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.2.4.Monitoring.System.Planning.3.txt",

                    "size": 71475676,

                    "description": "10 2 4 Monitoring System Planning 3"

                },
                {

                    "name": "10.2.4.Monitoring.System.Planning.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.2.4.Monitoring.System.Planning.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.2.4.Monitoring.System.Planning.txt",

                    "size": 126375654,

                    "description": "10 2 4 Monitoring System Planning"

                },
                {

                    "name": "10.2.5.Module.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.2.5.Module.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.2.5.Module.Summary.txt",

                    "size": 49732496,

                    "description": "10 2 5 Module Summary"

                },
                {

                    "name": "10.3.1.Introduction.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.3.1.Introduction.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.3.1.Introduction.txt",

                    "size": 50881219,

                    "description": "10 3 1 Introduction"

                },
                {

                    "name": "10.3.2.Sources.Events.Monitoring.Types.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.3.2.Sources.Events.Monitoring.Types.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.3.2.Sources.Events.Monitoring.Types.txt",

                    "size": 94241110,

                    "description": "10 3 2 Sources Events Monitoring Types"

                },
                {

                    "name": "10.3.3.Monitoring.Technologies.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.3.3.Monitoring.Technologies.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.3.3.Monitoring.Technologies.txt",

                    "size": 192848123,

                    "description": "10 3 3 Monitoring Technologies"

                },
                {

                    "name": "10.3.4.Event.Transport.Network.Changes.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.3.4.Event.Transport.Network.Changes.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.3.4.Event.Transport.Network.Changes.txt",

                    "size": 65996878,

                    "description": "10 3 4 Event Transport Network Changes"

                },
                {

                    "name": "10.3.5.Module.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.3.5.Module.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.3.5.Module.Summary.txt",

                    "size": 16256697,

                    "description": "10 3 5 Module Summary"

                },
                {

                    "name": "10.4.1.Introduction.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.4.1.Introduction.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.4.1.Introduction.txt",

                    "size": 35729223,

                    "description": "10 4 1 Introduction"

                },
                {

                    "name": "10.4.2.Event.Normalization.and.Log.Parsers.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.4.2.Event.Normalization.and.Log.Parsers.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.4.2.Event.Normalization.and.Log.Parsers.txt",

                    "size": 60800685,

                    "description": "10 4 2 Event Normalization and Log Parsers"

                },
                {

                    "name": "10.4.3.Use.Case.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.4.3.Use.Case.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.4.3.Use.Case.txt",

                    "size": 31117472,

                    "description": "10 4 3 Use Case"

                },
                {

                    "name": "10.4.4.Correlation.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.4.4.Correlation.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.4.4.Correlation.txt",

                    "size": 69538690,

                    "description": "10 4 4 Correlation"

                },
                {

                    "name": "10.4.5.Enrichment.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.4.5.Enrichment.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.4.5.Enrichment.txt",

                    "size": 34970113,

                    "description": "10 4 5 Enrichment"

                },
                {

                    "name": "10.4.6.Testing.and.Normal.Levels.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.4.6.Testing.and.Normal.Levels.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.4.6.Testing.and.Normal.Levels.txt",

                    "size": 36643068,

                    "description": "10 4 6 Testing and Normal Levels"

                },
                {

                    "name": "10.4.7.Module.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.4.7.Module.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.4.7.Module.Summary.txt",

                    "size": 10385896,

                    "description": "10 4 7 Module Summary"

                },
                {

                    "name": "10.5.1.Introduction.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.5.1.Introduction.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.5.1.Introduction.txt",

                    "size": 48352765,

                    "description": "10 5 1 Introduction"

                },
                {

                    "name": "10.5.2.Manual.and.Automated.Response.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.5.2.Manual.and.Automated.Response.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.5.2.Manual.and.Automated.Response.txt",

                    "size": 131825845,

                    "description": "10 5 2 Manual and Automated Response"

                },
                {

                    "name": "10.5.3.Incident.Enrichment.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.5.3.Incident.Enrichment.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.5.3.Incident.Enrichment.txt",

                    "size": 145097539,

                    "description": "10 5 3 Incident Enrichment"

                },
                {

                    "name": "10.5.4.Playbook.Structure.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.5.4.Playbook.Structure.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.5.4.Playbook.Structure.txt",

                    "size": 131648715,

                    "description": "10 5 4 Playbook Structure"

                },
                {

                    "name": "10.5.5.Anomalies.and.Undescribed.Incidents.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.5.5.Anomalies.and.Undescribed.Incidents.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.5.5.Anomalies.and.Undescribed.Incidents.txt",

                    "size": 25705917,

                    "description": "10 5 5 Anomalies and Undescribed Incidents"

                },
                {

                    "name": "10.5.6.Playbook.Socialization.and.Exercises.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.5.6.Playbook.Socialization.and.Exercises.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.5.6.Playbook.Socialization.and.Exercises.txt",

                    "size": 262916736,

                    "description": "10 5 6 Playbook Socialization and Exercises"

                },
                {

                    "name": "10.5.7.Module.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.5.7.Module.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.5.7.Module.Summary.txt",

                    "size": 33147461,

                    "description": "10 5 7 Module Summary"

                },
                {

                    "name": "10.6.1.Introduction.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.6.1.Introduction.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.6.1.Introduction.txt",

                    "size": 31189680,

                    "description": "10 6 1 Introduction"

                },
                {

                    "name": "10.6.2.Types.of.Security.Analysis.Additional.Analytical.Information.for.Report.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.6.2.Types.of.Security.Analysis.Additional.Analytical.Information.for.Report.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.6.2.Types.of.Security.Analysis.Additional.Analytical.Information.for.Report.txt",

                    "size": 37340686,

                    "description": "10 6 2 Types of Security Analysis Additional Analytical Information for Report"

                },
                {

                    "name": "10.6.3.Concept.of.Security.Analysis.Report.Customers.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.6.3.Concept.of.Security.Analysis.Report.Customers.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.6.3.Concept.of.Security.Analysis.Report.Customers.txt",

                    "size": 66455997,

                    "description": "10 6 3 Concept of Security Analysis Report Customers"

                },
                {

                    "name": "10.6.4.Report.Formatting.and.Access.Provisioning.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.6.4.Report.Formatting.and.Access.Provisioning.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.6.4.Report.Formatting.and.Access.Provisioning.txt",

                    "size": 47791088,

                    "description": "10 6 4 Report Formatting and Access Provisioning"

                },
                {

                    "name": "10.6.5.Module.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.6.5.Module.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.6.5.Module.Summary.txt",

                    "size": 55419369,

                    "description": "10 6 5 Module Summary"

                },
                {

                    "name": "10.7.1.Introduction.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.7.1.Introduction.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.7.1.Introduction.txt",

                    "size": 46246734,

                    "description": "10 7 1 Introduction"

                },
                {

                    "name": "10.7.3.Preparation.of.the.Investigation.Environment.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.7.3.Preparation.of.the.Investigation.Environment.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.7.3.Preparation.of.the.Investigation.Environment.txt",

                    "size": 148121677,

                    "description": "10 7 3 Preparation of the Investigation Environment"

                },
                {

                    "name": "10.7.4.Determining.the.Time.of.Attack.Onset.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.7.4.Determining.the.Time.of.Attack.Onset.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.7.4.Determining.the.Time.of.Attack.Onset.txt",

                    "size": 124672394,

                    "description": "10 7 4 Determining the Time of Attack Onset"

                },
                {

                    "name": "10.7.5.Determining.Distorted.Added.Deleted.Data.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.7.5.Determining.Distorted.Added.Deleted.Data.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.7.5.Determining.Distorted.Added.Deleted.Data.txt",

                    "size": 76431761,

                    "description": "10 7 5 Determining Distorted Added Deleted Data"

                },
                {

                    "name": "10.7.6.Building.the.Chain.of.Attack.Development.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.7.6.Building.the.Chain.of.Attack.Development.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.7.6.Building.the.Chain.of.Attack.Development.txt",

                    "size": 27319212,

                    "description": "10 7 6 Building the Chain of Attack Development"

                },
                {

                    "name": "10.7.7.Collecting.the.Attack.Attribution.Base.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.7.7.Collecting.the.Attack.Attribution.Base.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.7.7.Collecting.the.Attack.Attribution.Base.txt",

                    "size": 111006165,

                    "description": "10 7 7 Collecting the Attack Attribution Base"

                },
                {

                    "name": "10.7.8.Building.the.Chain.of.Attack.Development.Formatting.Digital.Evidence.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.7.8.Building.the.Chain.of.Attack.Development.Formatting.Digital.Evidence.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.7.8.Building.the.Chain.of.Attack.Development.Formatting.Digital.Evidence.txt",

                    "size": 31181577,

                    "description": "10 7 8 Building the Chain of Attack Development Formatting Digital Evidence"

                },
                {

                    "name": "10.7.9.Module.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.7.9.Module.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.7.9.Module.Summary.txt",

                    "size": 34814103,

                    "description": "10 7 9 Module Summary"

                },
                {

                    "name": "10.8.1.Introduction.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.8.1.Introduction.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.8.1.Introduction.txt",

                    "size": 60917902,

                    "description": "10 8 1 Introduction"

                },
                {

                    "name": "10.8.2.Establishing.the.Causes.of.the.Incident.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.8.2.Establishing.the.Causes.of.the.Incident.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.8.2.Establishing.the.Causes.of.the.Incident.txt",

                    "size": 20861891,

                    "description": "10 8 2 Establishing the Causes of the Incident"

                },
                {

                    "name": "10.8.3.Improving.Security.Measures.and.Preventing.Future.Incidents.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.8.3.Improving.Security.Measures.and.Preventing.Future.Incidents.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.8.3.Improving.Security.Measures.and.Preventing.Future.Incidents.txt",

                    "size": 38036128,

                    "description": "10 8 3 Improving Security Measures and Preventing Future Incidents"

                },
                {

                    "name": "10.8.4.Recovery.After.Incident.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.8.4.Recovery.After.Incident.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.8.4.Recovery.After.Incident.txt",

                    "size": 64440992,

                    "description": "10 8 4 Recovery After Incident"

                },
                {

                    "name": "10.8.5.Analysis.of.Elimination.Results.and.Conclusions.After.Incident.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.8.5.Analysis.of.Elimination.Results.and.Conclusions.After.Incident.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.8.5.Analysis.of.Elimination.Results.and.Conclusions.After.Incident.txt",

                    "size": 35769234,

                    "description": "10 8 5 Analysis of Elimination Results and Conclusions After Incident"

                },
                {

                    "name": "10.8.6.Module.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.8.6.Module.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.8.6.Module.Summary.txt",

                    "size": 39059697,

                    "description": "10 8 6 Module Summary"

                },
                {

                    "name": "10.8.7.Course.Summary.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.8.7.Course.Summary.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/10.0.0/10.8.7.Course.Summary.txt",

                    "size": 49254117,

                    "description": "10 8 7 Course Summary"

                }
        ],
        "9.0.0": [
                {

                    "name": "9.1.1.Introduction.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.1.1.Introduction.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.1.1.Introduction.webm",

                    "size": 114350851,

                    "description": "9 1 1 Introduction"

                },
                {

                    "name": "9.1.2.Solution.Preparation.Task.Formulation.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.1.2.Solution.Preparation.Task.Formulation.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.1.2.Solution.Preparation.Task.Formulation.webm",

                    "size": 45205406,

                    "description": "9 1 2 Solution Preparation Task Formulation"

                },
                {

                    "name": "9.1.3.Security.Solutions.Classification.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.1.3.Security.Solutions.Classification.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.1.3.Security.Solutions.Classification.webm",

                    "size": 28002015,

                    "description": "9 1 3 Security Solutions Classification"

                },
                {

                    "name": "9.1.4.Implementation.Process.Product.Lifecycle.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.1.4.Implementation.Process.Product.Lifecycle.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.1.4.Implementation.Process.Product.Lifecycle.webm",

                    "size": 21592076,

                    "description": "9 1 4 Implementation Process Product Lifecycle"

                },
                {

                    "name": "9.1.5.Implementation.Participants.Responsibilities.Resource.Owners.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.1.5.Implementation.Participants.Responsibilities.Resource.Owners.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.1.5.Implementation.Participants.Responsibilities.Resource.Owners.webm",

                    "size": 22994521,

                    "description": "9 1 5 Implementation Participants Responsibilities Resource Owners"

                },
                {

                    "name": "9.1.6.Module.Summary.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.1.6.Module.Summary.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.1.6.Module.Summary.webm",

                    "size": 29005842,

                    "description": "9 1 6 Module Summary"

                },
                {

                    "name": "9.2.3.Test.Environment.Deployment.Antivirus.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.2.3.Test.Environment.Deployment.Antivirus.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.2.3.Test.Environment.Deployment.Antivirus.webm",

                    "size": 164319613,

                    "description": "9 2 3 Test Environment Deployment Antivirus"

                },
                {

                    "name": "9.2.4.Module.Summary.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.2.4.Module.Summary.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.2.4.Module.Summary.webm",

                    "size": 7413722,

                    "description": "9 2 4 Module Summary"

                },
                {

                    "name": "9.3.1.Introduction.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.3.1.Introduction.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.3.1.Introduction.txt",

                    "size": 19954211,

                    "description": "9 3 1 Introduction"

                },
                {

                    "name": "9.3.2.System.Testing.Technical.Project.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.3.2.System.Testing.Technical.Project.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.3.2.System.Testing.Technical.Project.txt",

                    "size": 70648863,

                    "description": "9 3 2 System Testing Technical Project"

                },
                {

                    "name": "9.3.3.Participant.Roles.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.3.3.Participant.Roles.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.3.3.Participant.Roles.txt",

                    "size": 64726163,

                    "description": "9 3 3 Participant Roles"

                },
                {

                    "name": "9.3.4.Documentation.Support.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.3.4.Documentation.Support.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.3.4.Documentation.Support.txt",

                    "size": 37511112,

                    "description": "9 3 4 Documentation Support"

                },
                {

                    "name": "9.3.5.Endpoint.Security.Testing.Program.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.3.5.Endpoint.Security.Testing.Program.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.3.5.Endpoint.Security.Testing.Program.txt",

                    "size": 40386167,

                    "description": "9 3 5 Endpoint Security Testing Program"

                },
                {

                    "name": "9.3.6.Module.Conclusions.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.3.6.Module.Conclusions.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.3.6.Module.Conclusions.txt",

                    "size": 25397674,

                    "description": "9 3 6 Module Conclusions"

                },
                {

                    "name": "9.4.1.System.Operation.Introduction.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.4.1.System.Operation.Introduction.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.4.1.System.Operation.Introduction.txt",

                    "size": 44694675,

                    "description": "9 4 1 System Operation Introduction"

                },
                {

                    "name": "9.4.2.What.to.Consider.for.System.Adoption.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.4.2.What.to.Consider.for.System.Adoption.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.4.2.What.to.Consider.for.System.Adoption.txt",

                    "size": 43111902,

                    "description": "9 4 2 What to Consider for System Adoption"

                },
                {

                    "name": "9.4.3.Final.Stage.Documentation.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.4.3.Final.Stage.Documentation.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.4.3.Final.Stage.Documentation.txt",

                    "size": 33087243,

                    "description": "9 4 3 Final Stage Documentation"

                },
                {

                    "name": "9.4.5.Why.Pay.Special.Attention.to.System.Handover.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.4.5.Why.Pay.Special.Attention.to.System.Handover.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/9.0.0/9.4.5.Why.Pay.Special.Attention.to.System.Handover.txt",

                    "size": 25664280,

                    "description": "9 4 5 Why Pay Special Attention to System Handover"

                }
        ],
        "8.0.0": [
                {

                    "name": "8.1.1.Access.and.Connection.to.Test.Environment.for.Practical.Work.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.1.1.Access.and.Connection.to.Test.Environment.for.Practical.Work.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.1.1.Access.and.Connection.to.Test.Environment.for.Practical.Work.webm",

                    "size": 38825709,

                    "description": "8 1 1 Access and Connection to Test Environment for Practical Work"

                },
                {

                    "name": "8.10.1.Module.Introduction.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.10.1.Module.Introduction.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.10.1.Module.Introduction.webm",

                    "size": 52727893,

                    "description": "8 10 1 Module Introduction"

                },
                {

                    "name": "8.10.2.What.is.Active.Directory.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.10.2.What.is.Active.Directory.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.10.2.What.is.Active.Directory.webm",

                    "size": 70895742,

                    "description": "8 10 2 What is Active Directory"

                },
                {

                    "name": "8.10.3.Active.Directory.Users.and.Groups.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.10.3.Active.Directory.Users.and.Groups.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.10.3.Active.Directory.Users.and.Groups.webm",

                    "size": 78888631,

                    "description": "8 10 3 Active Directory Users and Groups"

                },
                {

                    "name": "8.10.4.BloodHound.AD.Analysis.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.10.4.BloodHound.AD.Analysis.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.10.4.BloodHound.AD.Analysis.webm",

                    "size": 62400716,

                    "description": "8 10 4 BloodHound AD Analysis"

                },
                {

                    "name": "8.10.5.Windows.Authentication.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.10.5.Windows.Authentication.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.10.5.Windows.Authentication.webm",

                    "size": 40514384,

                    "description": "8 10 5 Windows Authentication"

                },
                {

                    "name": "8.10.6.NTLM.Authentication.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.10.6.NTLM.Authentication.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.10.6.NTLM.Authentication.webm",

                    "size": 89660442,

                    "description": "8 10 6 NTLM Authentication"

                },
                {

                    "name": "8.10.7.Kerberos.Authentication.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.10.7.Kerberos.Authentication.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.10.7.Kerberos.Authentication.webm",

                    "size": 62115936,

                    "description": "8 10 7 Kerberos Authentication"

                },
                {

                    "name": "8.10.8.Module.Summary.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.10.8.Module.Summary.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.10.8.Module.Summary.webm",

                    "size": 22123416,

                    "description": "8 10 8 Module Summary"

                },
                {

                    "name": "8.11.1.Introduction.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.11.1.Introduction.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.11.1.Introduction.webm",

                    "size": 39605420,

                    "description": "8 11 1 Introduction"

                },
                {

                    "name": "8.11.2.Pass.the.Hash.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.11.2.Pass.the.Hash.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.11.2.Pass.the.Hash.webm",

                    "size": 56410388,

                    "description": "8 11 2 Pass the Hash"

                },
                {

                    "name": "8.11.3.NTLM.Relay.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.11.3.NTLM.Relay.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.11.3.NTLM.Relay.webm",

                    "size": 61282754,

                    "description": "8 11 3 NTLM Relay"

                },
                {

                    "name": "8.11.4.NTLM.Hash.Cracking.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.11.4.NTLM.Hash.Cracking.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.11.4.NTLM.Hash.Cracking.webm",

                    "size": 57452892,

                    "description": "8 11 4 NTLM Hash Cracking"

                },
                {

                    "name": "8.11.5.Kerberoasting.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.11.5.Kerberoasting.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.11.5.Kerberoasting.webm",

                    "size": 84316905,

                    "description": "8 11 5 Kerberoasting"

                },
                {

                    "name": "8.11.6.Pass.the.Ticket.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.11.6.Pass.the.Ticket.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.11.6.Pass.the.Ticket.webm",

                    "size": 61869370,

                    "description": "8 11 6 Pass the Ticket"

                },
                {

                    "name": "8.11.7.Module.Summary.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.11.7.Module.Summary.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.11.7.Module.Summary.webm",

                    "size": 39239077,

                    "description": "8 11 7 Module Summary"

                },
                {

                    "name": "8.12.1.Vulnerability.Management.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.12.1.Vulnerability.Management.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.12.1.Vulnerability.Management.webm",

                    "size": 12226809,

                    "description": "8 12 1 Vulnerability Management"

                },
                {

                    "name": "8.12.2.Vulnerability.Metrics.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.12.2.Vulnerability.Metrics.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.12.2.Vulnerability.Metrics.webm",

                    "size": 56166542,

                    "description": "8 12 2 Vulnerability Metrics"

                },
                {

                    "name": "8.12.3.Vulnerability.Search.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.12.3.Vulnerability.Search.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.12.3.Vulnerability.Search.webm",

                    "size": 122858151,

                    "description": "8 12 3 Vulnerability Search"

                },
                {

                    "name": "8.12.4.Scanner.Setup.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.12.4.Scanner.Setup.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.12.4.Scanner.Setup.webm",

                    "size": 99999344,

                    "description": "8 12 4 Scanner Setup"

                },
                {

                    "name": "8.12.5.Scanner.Usage.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.12.5.Scanner.Usage.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.12.5.Scanner.Usage.webm",

                    "size": 135900222,

                    "description": "8 12 5 Scanner Usage"

                },
                {

                    "name": "8.12.6.Exploit.Search-2.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.12.6.Exploit.Search-2.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.12.6.Exploit.Search-2.webm",

                    "size": 34418290,

                    "description": "8 12 6 Exploit Search-2"

                },
                {

                    "name": "8.12.6.Exploit.Search.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.12.6.Exploit.Search.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.12.6.Exploit.Search.webm",

                    "size": 48672856,

                    "description": "8 12 6 Exploit Search"

                },
                {

                    "name": "8.12.7.Module.Summary.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.12.7.Module.Summary.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.12.7.Module.Summary.webm",

                    "size": 10357817,

                    "description": "8 12 7 Module Summary"

                },
                {

                    "name": "8.13.1.Introduction.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.13.1.Introduction.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.13.1.Introduction.webm",

                    "size": 6358178,

                    "description": "8 13 1 Introduction"

                },
                {

                    "name": "8.13.2.Metasploit.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.13.2.Metasploit.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.13.2.Metasploit.webm",

                    "size": 58385756,

                    "description": "8 13 2 Metasploit"

                },
                {

                    "name": "8.13.3.Post-Exploitation.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.13.3.Post-Exploitation.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.13.3.Post-Exploitation.webm",

                    "size": 159369114,

                    "description": "8 13 3 Post-Exploitation"

                },
                {

                    "name": "8.13.4.System-Persistence.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.13.4.System-Persistence.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.13.4.System-Persistence.webm",

                    "size": 179607455,

                    "description": "8 13 4 System-Persistence"

                },
                {

                    "name": "8.13.5.Bug-Bounty-Programs.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.13.5.Bug-Bounty-Programs.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.13.5.Bug-Bounty-Programs.webm",

                    "size": 22159355,

                    "description": "8 13 5 Bug-Bounty-Programs"

                },
                {

                    "name": "8.13.6.Module-Summary.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.13.6.Module-Summary.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.13.6.Module-Summary.webm",

                    "size": 11812651,

                    "description": "8 13 6 Module-Summary"

                },
                {

                    "name": "8.2.1.Intro.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.2.1.Intro.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.2.1.Intro.webm",

                    "size": 22294571,

                    "description": "8 2 1 Intro"

                },
                {

                    "name": "8.2.2.What.is.Ethical.Hacking.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.2.2.What.is.Ethical.Hacking.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.2.2.What.is.Ethical.Hacking.webm",

                    "size": 39341474,

                    "description": "8 2 2 What is Ethical Hacking"

                },
                {

                    "name": "8.2.3.Legal.Aspects.of.Activity.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.2.3.Legal.Aspects.of.Activity.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.2.3.Legal.Aspects.of.Activity.webm",

                    "size": 19425172,

                    "description": "8 2 3 Legal Aspects of Activity"

                },
                {

                    "name": "8.2.4.Main.Directions.of.Activity.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.2.4.Main.Directions.of.Activity.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.2.4.Main.Directions.of.Activity.webm",

                    "size": 30594088,

                    "description": "8 2 4 Main Directions of Activity"

                },
                {

                    "name": "8.2.5.Kill.Chain.Model.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.2.5.Kill.Chain.Model.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.2.5.Kill.Chain.Model.webm",

                    "size": 19753568,

                    "description": "8 2 5 Kill Chain Model"

                },
                {

                    "name": "8.2.6.Overview.of.Public.Distributives.for.Pentest.Part2.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.2.6.Overview.of.Public.Distributives.for.Pentest.Part2.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.2.6.Overview.of.Public.Distributives.for.Pentest.Part2.webm",

                    "size": 35577555,

                    "description": "8 2 6 Overview of Public Distributives for Pentest Part2"

                },
                {

                    "name": "8.2.6.Overview.of.Public.Distributives.for.Pentest.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.2.6.Overview.of.Public.Distributives.for.Pentest.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.2.6.Overview.of.Public.Distributives.for.Pentest.webm",

                    "size": 18080317,

                    "description": "8 2 6 Overview of Public Distributives for Pentest"

                },
                {

                    "name": "8.2.7.Module.Summary.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.2.7.Module.Summary.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.2.7.Module.Summary.webm",

                    "size": 32575074,

                    "description": "8 2 7 Module Summary"

                },
                {

                    "name": "8.3.1.Introduction.to.OSINT.Part.1.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.1.Introduction.to.OSINT.Part.1.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.1.Introduction.to.OSINT.Part.1.webm",

                    "size": 128492331,

                    "description": "8 3 1 Introduction to OSINT Part 1"

                },
                {

                    "name": "8.3.10.Module.Summary.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.10.Module.Summary.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.10.Module.Summary.webm",

                    "size": 34492941,

                    "description": "8 3 10 Module Summary"

                },
                {

                    "name": "8.3.2.What.is.OSINT.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.2.What.is.OSINT.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.2.What.is.OSINT.webm",

                    "size": 135367121,

                    "description": "8 3 2 What is OSINT"

                },
                {

                    "name": "8.3.3.Internet.Levels.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.3.Internet.Levels.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.3.Internet.Levels.webm",

                    "size": 27399425,

                    "description": "8 3 3 Internet Levels"

                },
                {

                    "name": "8.3.4.Websites.and.Social.Networks.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.4.Websites.and.Social.Networks.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.4.Websites.and.Social.Networks.webm",

                    "size": 209272589,

                    "description": "8 3 4 Websites and Social Networks"

                },
                {

                    "name": "8.3.5.Metadata.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.5.Metadata.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.5.Metadata.webm",

                    "size": 53678182,

                    "description": "8 3 5 Metadata"

                },
                {

                    "name": "8.3.6.Honeytokens.and.Countering.OSINT.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.6.Honeytokens.and.Countering.OSINT.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.6.Honeytokens.and.Countering.OSINT.webm",

                    "size": 51356438,

                    "description": "8 3 6 Honeytokens and Countering OSINT"

                },
                {

                    "name": "8.3.7.Search.Engines.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.7.Search.Engines.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.7.Search.Engines.webm",

                    "size": 105768468,

                    "description": "8 3 7 Search Engines"

                },
                {

                    "name": "8.3.8.Email.Search.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.8.Email.Search.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.8.Email.Search.webm",

                    "size": 26398908,

                    "description": "8 3 8 Email Search"

                },
                {

                    "name": "8.3.9.Repositories.and.Search.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.9.Repositories.and.Search.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.3.9.Repositories.and.Search.webm",

                    "size": 29449469,

                    "description": "8 3 9 Repositories and Search"

                },
                {

                    "name": "8.4.1.What.Awaits.You.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.4.1.What.Awaits.You.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.4.1.What.Awaits.You.webm",

                    "size": 9709837,

                    "description": "8 4 1 What Awaits You"

                },
                {

                    "name": "8.4.2.DNS.Record.Investigation.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.4.2.DNS.Record.Investigation.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.4.2.DNS.Record.Investigation.webm",

                    "size": 168556026,

                    "description": "8 4 2 DNS Record Investigation"

                },
                {

                    "name": "8.4.3.Search.Engines.2.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.4.3.Search.Engines.2.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.4.3.Search.Engines.2.webm",

                    "size": 328762943,

                    "description": "8 4 3 Search Engines 2"

                },
                {

                    "name": "8.4.4.OSINT.Tools.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.4.4.OSINT.Tools.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.4.4.OSINT.Tools.webm",

                    "size": 249478763,

                    "description": "8 4 4 OSINT Tools"

                },
                {

                    "name": "8.4.5.Maltego.Setup.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.4.5.Maltego.Setup.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.4.5.Maltego.Setup.webm",

                    "size": 141355303,

                    "description": "8 4 5 Maltego Setup"

                },
                {

                    "name": "8.4.6.Module.Summary.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.4.6.Module.Summary.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.4.6.Module.Summary.webm",

                    "size": 8226069,

                    "description": "8 4 6 Module Summary"

                },
                {

                    "name": "8.5.1.Intro.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.5.1.Intro.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.5.1.Intro.webm",

                    "size": 4239328,

                    "description": "8 5 1 Intro"

                },
                {

                    "name": "8.5.2.Introduction.to.Social.Engineering.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.5.2.Introduction.to.Social.Engineering.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.5.2.Introduction.to.Social.Engineering.webm",

                    "size": 6291586,

                    "description": "8 5 2 Introduction to Social Engineering"

                },
                {

                    "name": "8.6.1.Intro.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.6.1.Intro.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.6.1.Intro.webm",

                    "size": 6269008,

                    "description": "8 6 1 Intro"

                },
                {

                    "name": "8.6.2.Introduction.to.Networks.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.6.2.Introduction.to.Networks.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.6.2.Introduction.to.Networks.webm",

                    "size": 1812136,

                    "description": "8 6 2 Introduction to Networks"

                },
                {

                    "name": "8.6.3.Basic.Protocols.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.6.3.Basic.Protocols.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.6.3.Basic.Protocols.webm",

                    "size": 1279592,

                    "description": "8 6 3 Basic Protocols"

                },
                {

                    "name": "8.6.4.Traffic.Interception.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.6.4.Traffic.Interception.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.6.4.Traffic.Interception.webm",

                    "size": 163050752,

                    "description": "8 6 4 Traffic Interception"

                },
                {

                    "name": "8.6.5.Network.Attacks.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.6.5.Network.Attacks.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.6.5.Network.Attacks.webm",

                    "size": 701851,

                    "description": "8 6 5 Network Attacks"

                },
                {

                    "name": "8.6.6.ARP.Spoofing.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.6.6.ARP.Spoofing.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.6.6.ARP.Spoofing.webm",

                    "size": 68808132,

                    "description": "8 6 6 ARP Spoofing"

                },
                {

                    "name": "8.6.7.Module.Summary.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.6.7.Module.Summary.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.6.7.Module.Summary.webm",

                    "size": 1512815,

                    "description": "8 6 7 Module Summary"

                },
                {

                    "name": "8.7.1.Introduction.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.7.1.Introduction.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.7.1.Introduction.webm",

                    "size": 4001684,

                    "description": "8 7 1 Introduction"

                },
                {

                    "name": "8.7.2.Network.Scanning.Basics.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.7.2.Network.Scanning.Basics.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.7.2.Network.Scanning.Basics.webm",

                    "size": 81249861,

                    "description": "8 7 2 Network Scanning Basics"

                },
                {

                    "name": "8.7.3.Nmap.Scripts.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.7.3.Nmap.Scripts.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.7.3.Nmap.Scripts.webm",

                    "size": 58385327,

                    "description": "8 7 3 Nmap Scripts"

                },
                {

                    "name": "8.7.4.Module.Summary.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.7.4.Module.Summary.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.7.4.Module.Summary.webm",

                    "size": 5623120,

                    "description": "8 7 4 Module Summary"

                },
                {

                    "name": "8.8.1.Introduction.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.8.1.Introduction.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.8.1.Introduction.webm",

                    "size": 50912324,

                    "description": "8 8 1 Introduction"

                },
                {

                    "name": "8.8.2.Modern.Web.Applications.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.8.2.Modern.Web.Applications.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.8.2.Modern.Web.Applications.webm",

                    "size": 12515485,

                    "description": "8 8 2 Modern Web Applications"

                },
                {

                    "name": "8.8.3.Web.Application.Attack.Types.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.8.3.Web.Application.Attack.Types.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.8.3.Web.Application.Attack.Types.webm",

                    "size": 23850679,

                    "description": "8 8 3 Web Application Attack Types"

                },
                {

                    "name": "8.8.4.Web.Vulnerability.Exploitation.Tools.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.8.4.Web.Vulnerability.Exploitation.Tools.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.8.4.Web.Vulnerability.Exploitation.Tools.webm",

                    "size": 131235392,

                    "description": "8 8 4 Web Vulnerability Exploitation Tools"

                },
                {

                    "name": "8.8.5.Module.Summary.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.8.5.Module.Summary.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.8.5.Module.Summary.webm",

                    "size": 44987522,

                    "description": "8 8 5 Module Summary"

                },
                {

                    "name": "8.9.1.Module.Introduction.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.9.1.Module.Introduction.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.9.1.Module.Introduction.webm",

                    "size": 20736082,

                    "description": "8 9 1 Module Introduction"

                },
                {

                    "name": "8.9.2.Brute.Force.Attacks.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.9.2.Brute.Force.Attacks.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.9.2.Brute.Force.Attacks.webm",

                    "size": 12249627,

                    "description": "8 9 2 Brute Force Attacks"

                },
                {

                    "name": "8.9.3.Brute.Force.on.Network.Services.Part1.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.9.3.Brute.Force.on.Network.Services.Part1.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.9.3.Brute.Force.on.Network.Services.Part1.webm",

                    "size": 102152065,

                    "description": "8 9 3 Brute Force on Network Services Part1"

                },
                {

                    "name": "8.9.3.Brute.Force.on.Network.Services.Part2.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.9.3.Brute.Force.on.Network.Services.Part2.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.9.3.Brute.Force.on.Network.Services.Part2.webm",

                    "size": 33217757,

                    "description": "8 9 3 Brute Force on Network Services Part2"

                },
                {

                    "name": "8.9.4.Brute.Force.on.Hash.Functions.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.9.4.Brute.Force.on.Hash.Functions.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.9.4.Brute.Force.on.Hash.Functions.webm",

                    "size": 108530860,

                    "description": "8 9 4 Brute Force on Hash Functions"

                },
                {

                    "name": "8.9.5.Local.Credential.Sources.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.9.5.Local.Credential.Sources.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.9.5.Local.Credential.Sources.webm",

                    "size": 48964071,

                    "description": "8 9 5 Local Credential Sources"

                },
                {

                    "name": "8.9.6.Module.Summary.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.9.6.Module.Summary.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/8.0.0/8.9.6.Module.Summary.webm",

                    "size": 47539111,

                    "description": "8 9 6 Module Summary"

                }
        ],
        "7.0.0": [
                {

                    "name": "7.1.1.Intro.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.1.1.Intro.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.1.1.Intro.webm",

                    "size": 41303916,

                    "description": "7 1 1 Intro"

                },
                {

                    "name": "7.1.2.Types.of.Processes.and.Their.Differences.Part.1.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.1.2.Types.of.Processes.and.Their.Differences.Part.1.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.1.2.Types.of.Processes.and.Their.Differences.Part.1.webm",

                    "size": 227401827,

                    "description": "7 1 2 Types of Processes and Their Differences Part 1"

                },
                {

                    "name": "7.1.2.Types.of.Processes.and.Their.Differences.Part.2.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.1.2.Types.of.Processes.and.Their.Differences.Part.2.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.1.2.Types.of.Processes.and.Their.Differences.Part.2.webm",

                    "size": 325094496,

                    "description": "7 1 2 Types of Processes and Their Differences Part 2"

                },
                {

                    "name": "7.1.3.The.Golden.Standard.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.1.3.The.Golden.Standard.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.1.3.The.Golden.Standard.webm",

                    "size": 210553090,

                    "description": "7 1 3 The Golden Standard"

                },
                {

                    "name": "7.1.4.Prioritization.of.Processes.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.1.4.Prioritization.of.Processes.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.1.4.Prioritization.of.Processes.webm",

                    "size": 563976374,

                    "description": "7 1 4 Prioritization of Processes"

                },
                {

                    "name": "7.2.1.Groups.of.IS.Processes.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.2.1.Groups.of.IS.Processes.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.2.1.Groups.of.IS.Processes.webm",

                    "size": 490728859,

                    "description": "7 2 1 Groups of IS Processes"

                },
                {

                    "name": "7.2.2.Operational.Processes.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.2.2.Operational.Processes.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.2.2.Operational.Processes.webm",

                    "size": 249713098,

                    "description": "7 2 2 Operational Processes"

                },
                {

                    "name": "7.2.3.Antivirus.Protection.Process.Part.1.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.2.3.Antivirus.Protection.Process.Part.1.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.2.3.Antivirus.Protection.Process.Part.1.webm",

                    "size": 165290630,

                    "description": "7 2 3 Antivirus Protection Process Part 1"

                },
                {

                    "name": "7.2.3.Antivirus.Protection.Process.Part.2.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.2.3.Antivirus.Protection.Process.Part.2.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.2.3.Antivirus.Protection.Process.Part.2.webm",

                    "size": 397599830,

                    "description": "7 2 3 Antivirus Protection Process Part 2"

                },
                {

                    "name": "7.3.1.Tactical.Processes.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.3.1.Tactical.Processes.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.3.1.Tactical.Processes.webm",

                    "size": 178058513,

                    "description": "7 3 1 Tactical Processes"

                },
                {

                    "name": "7.3.2.Incident.Management.Process.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.3.2.Incident.Management.Process.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.3.2.Incident.Management.Process.webm",

                    "size": 621285223,

                    "description": "7 3 2 Incident Management Process"

                },
                {

                    "name": "7.3.3.Strategic.Processes.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.3.3.Strategic.Processes.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.3.3.Strategic.Processes.webm",

                    "size": 169179210,

                    "description": "7 3 3 Strategic Processes"

                },
                {

                    "name": "7.3.4.Compliance.Management.Process.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.3.4.Compliance.Management.Process.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.3.4.Compliance.Management.Process.webm",

                    "size": 244422301,

                    "description": "7 3 4 Compliance Management Process"

                },
                {

                    "name": "7.3.5.Differences.and.Features.of.Different.Types.of.Processes.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.3.5.Differences.and.Features.of.Different.Types.of.Processes.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.3.5.Differences.and.Features.of.Different.Types.of.Processes.webm",

                    "size": 229704794,

                    "description": "7 3 5 Differences and Features of Different Types of Processes"

                },
                {

                    "name": "7.4.1.Set.of.Roles.in.Operational.Processes.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.4.1.Set.of.Roles.in.Operational.Processes.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.4.1.Set.of.Roles.in.Operational.Processes.webm",

                    "size": 366973512,

                    "description": "7 4 1 Set of Roles in Operational Processes"

                },
                {

                    "name": "7.4.2.Set.of.Roles.in.Project.Implementation.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.4.2.Set.of.Roles.in.Project.Implementation.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.4.2.Set.of.Roles.in.Project.Implementation.webm",

                    "size": 302524710,

                    "description": "7 4 2 Set of Roles in Project Implementation"

                },
                {

                    "name": "7.4.3.Manager.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.4.3.Manager.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.4.3.Manager.webm",

                    "size": 360295591,

                    "description": "7 4 3 Manager"

                },
                {

                    "name": "7.4.4.Chief.Engineer.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.4.4.Chief.Engineer.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.4.4.Chief.Engineer.webm",

                    "size": 447569209,

                    "description": "7 4 4 Chief Engineer"

                },
                {

                    "name": "7.4.5.Participant.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.4.5.Participant.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.4.5.Participant.webm",

                    "size": 319832305,

                    "description": "7 4 5 Participant"

                },
                {

                    "name": "7.5.1.Company.Types.and.Influencing.Factors.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.5.1.Company.Types.and.Influencing.Factors.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.5.1.Company.Types.and.Influencing.Factors.webm",

                    "size": 393635080,

                    "description": "7 5 1 Company Types and Influencing Factors"

                },
                {

                    "name": "7.5.2.Basic.Specializations.in.Information.Security.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.5.2.Basic.Specializations.in.Information.Security.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.5.2.Basic.Specializations.in.Information.Security.webm",

                    "size": 758760583,

                    "description": "7 5 2 Basic Specializations in Information Security"

                },
                {

                    "name": "7.5.3.Development.of.Specializations.in.Companies.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.5.3.Development.of.Specializations.in.Companies.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.5.3.Development.of.Specializations.in.Companies.webm",

                    "size": 306315869,

                    "description": "7 5 3 Development of Specializations in Companies"

                },
                {

                    "name": "7.5.4.Career.Graph.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.5.4.Career.Graph.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/7.0.0/7.5.4.Career.Graph.webm",

                    "size": 633818846,

                    "description": "7 5 4 Career Graph"

                }
        ],
        "6.0.0": [
                {

                    "name": "6.1.2.Introduction.to.Programming.and.Python.Language.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.1.2.Introduction.to.Programming.and.Python.Language.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.1.2.Introduction.to.Programming.and.Python.Language.webm",

                    "size": 99645831,

                    "description": "6 1 2 Introduction to Programming and Python Language"

                },
                {

                    "name": "6.1.3.First.Program.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.1.3.First.Program.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.1.3.First.Program.webm",

                    "size": 56788246,

                    "description": "6 1 3 First Program"

                },
                {

                    "name": "6.1.4.First.Errors.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.1.4.First.Errors.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.1.4.First.Errors.webm",

                    "size": 32019723,

                    "description": "6 1 4 First Errors"

                },
                {

                    "name": "6.1.5.Features.of.Working.with.Print.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.1.5.Features.of.Working.with.Print.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.1.5.Features.of.Working.with.Print.webm",

                    "size": 38062372,

                    "description": "6 1 5 Features of Working with Print"

                },
                {

                    "name": "6.10.1.Working.with.Nested.Loops.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.10.1.Working.with.Nested.Loops.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.10.1.Working.with.Nested.Loops.webm",

                    "size": 93318321,

                    "description": "6 10 1 Working with Nested Loops"

                },
                {

                    "name": "6.10.2.Using.if.in.Nested.Loops.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.10.2.Using.if.in.Nested.Loops.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.10.2.Using.if.in.Nested.Loops.webm",

                    "size": 59836343,

                    "description": "6 10 2 Using if in Nested Loops"

                },
                {

                    "name": "6.10.3.Working.with.Two.Counters.in.Conditional.Operator.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.10.3.Working.with.Two.Counters.in.Conditional.Operator.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.10.3.Working.with.Two.Counters.in.Conditional.Operator.webm",

                    "size": 72233362,

                    "description": "6 10 3 Working with Two Counters in Conditional Operator"

                },
                {

                    "name": "6.10.4.Solving.Problems.with.Nested.Loops.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.10.4.Solving.Problems.with.Nested.Loops.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.10.4.Solving.Problems.with.Nested.Loops.webm",

                    "size": 83314295,

                    "description": "6 10 4 Solving Problems with Nested Loops"

                },
                {

                    "name": "6.10.5.Else.Block.for.Loop.Infinite.Outer.Loop.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.10.5.Else.Block.for.Loop.Infinite.Outer.Loop.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.10.5.Else.Block.for.Loop.Infinite.Outer.Loop.webm",

                    "size": 84274874,

                    "description": "6 10 5 Else Block for Loop Infinite Outer Loop"

                },
                {

                    "name": "6.11.1.Homework.Review.Floating.Point.Numbers.int.float.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.11.1.Homework.Review.Floating.Point.Numbers.int.float.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.11.1.Homework.Review.Floating.Point.Numbers.int.float.webm",

                    "size": 127929282,

                    "description": "6 11 1 Homework Review Floating Point Numbers int float"

                },
                {

                    "name": "6.11.2.Input.of.Real.Number.Functions.float.and.round.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.11.2.Input.of.Real.Number.Functions.float.and.round.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.11.2.Input.of.Real.Number.Functions.float.and.round.webm",

                    "size": 107799267,

                    "description": "6 11 2 Input of Real Number Functions float and round"

                },
                {

                    "name": "6.11.3.Type.Casting.Between.int.and.float.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.11.3.Type.Casting.Between.int.and.float.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.11.3.Type.Casting.Between.int.and.float.webm",

                    "size": 72067200,

                    "description": "6 11 3 Type Casting Between int and float"

                },
                {

                    "name": "6.11.4.Mathematical.Functions.Working.with.the.math.Module.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.11.4.Mathematical.Functions.Working.with.the.math.Module.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.11.4.Mathematical.Functions.Working.with.the.math.Module.webm",

                    "size": 98804510,

                    "description": "6 11 4 Mathematical Functions Working with the math Module"

                },
                {

                    "name": "6.11.5.About.the.Next.Module.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.11.5.About.the.Next.Module.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.11.5.About.the.Next.Module.webm",

                    "size": 35372244,

                    "description": "6 11 5 About the Next Module"

                },
                {

                    "name": "6.12.1.Homework.Review.Functions.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.12.1.Homework.Review.Functions.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.12.1.Homework.Review.Functions.webm",

                    "size": 39357735,

                    "description": "6 12 1 Homework Review Functions"

                },
                {

                    "name": "6.12.2.Functions.and.Their.Calls.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.12.2.Functions.and.Their.Calls.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.12.2.Functions.and.Their.Calls.webm",

                    "size": 131132617,

                    "description": "6 12 2 Functions and Their Calls"

                },
                {

                    "name": "6.12.3.Functions.with.One.Parameter.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.12.3.Functions.with.One.Parameter.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.12.3.Functions.with.One.Parameter.webm",

                    "size": 89615990,

                    "description": "6 12 3 Functions with One Parameter"

                },
                {

                    "name": "6.12.4.Functions.with.Multiple.Parameters.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.12.4.Functions.with.Multiple.Parameters.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.12.4.Functions.with.Multiple.Parameters.webm",

                    "size": 104672705,

                    "description": "6 12 4 Functions with Multiple Parameters"

                },
                {

                    "name": "6.12.5.Nested.Function.Call.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.12.5.Nested.Function.Call.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.12.5.Nested.Function.Call.webm",

                    "size": 90084500,

                    "description": "6 12 5 Nested Function Call"

                },
                {

                    "name": "6.13.1.Review.of.Practical.Work.Float.2.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.13.1.Review.of.Practical.Work.Float.2.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.13.1.Review.of.Practical.Work.Float.2.webm",

                    "size": 44081162,

                    "description": "6 13 1 Review of Practical Work Float 2"

                },
                {

                    "name": "6.13.2.Return.Values.from.Functions.Operator.return.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.13.2.Return.Values.from.Functions.Operator.return.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.13.2.Return.Values.from.Functions.Operator.return.webm",

                    "size": 83768451,

                    "description": "6 13 2 Return Values from Functions Operator return"

                },
                {

                    "name": "6.13.3.Representation.of.Real.Numbers.in.the.Program.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.13.3.Representation.of.Real.Numbers.in.the.Program.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.13.3.Representation.of.Real.Numbers.in.the.Program.webm",

                    "size": 70992417,

                    "description": "6 13 3 Representation of Real Numbers in the Program"

                },
                {

                    "name": "6.13.4.Features.of.Working.with.Real.Numbers.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.13.4.Features.of.Working.with.Real.Numbers.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.13.4.Features.of.Working.with.Real.Numbers.webm",

                    "size": 44001341,

                    "description": "6 13 4 Features of Working with Real Numbers"

                },
                {

                    "name": "6.13.5.Algorithms.with.Given.Accuracy.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.13.5.Algorithms.with.Given.Accuracy.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.13.5.Algorithms.with.Given.Accuracy.webm",

                    "size": 57630623,

                    "description": "6 13 5 Algorithms with Given Accuracy"

                },
                {

                    "name": "6.2.1.Variables.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.2.1.Variables.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.2.1.Variables.webm",

                    "size": 56788246,

                    "description": "6 2 1 Variables"

                },
                {

                    "name": "6.2.2.Input.Operator.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.2.2.Input.Operator.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.2.2.Input.Operator.webm",

                    "size": 81935492,

                    "description": "6 2 2 Input Operator"

                },
                {

                    "name": "6.2.3.Strings.and.Concatenation.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.2.3.Strings.and.Concatenation.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.2.3.Strings.and.Concatenation.webm",

                    "size": 73641815,

                    "description": "6 2 3 Strings and Concatenation"

                },
                {

                    "name": "6.2.4.Features.of.Working.with.Variables.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.2.4.Features.of.Working.with.Variables.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.2.4.Features.of.Working.with.Variables.webm",

                    "size": 92398187,

                    "description": "6 2 4 Features of Working with Variables"

                },
                {

                    "name": "6.3.1.Homework.Review.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.3.1.Homework.Review.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.3.1.Homework.Review.webm",

                    "size": 60908194,

                    "description": "6 3 1 Homework Review"

                },
                {

                    "name": "6.3.2.Numbers.and.Arithmetic.Operations.with.Them.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.3.2.Numbers.and.Arithmetic.Operations.with.Them.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.3.2.Numbers.and.Arithmetic.Operations.with.Them.webm",

                    "size": 53298486,

                    "description": "6 3 2 Numbers and Arithmetic Operations with Them"

                },
                {

                    "name": "6.3.3.Priority.of.Arithmetic.Operations.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.3.3.Priority.of.Arithmetic.Operations.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.3.3.Priority.of.Arithmetic.Operations.webm",

                    "size": 35711780,

                    "description": "6 3 3 Priority of Arithmetic Operations"

                },
                {

                    "name": "6.3.4.Inputting.a.Number.from.Keyboard.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.3.4.Inputting.a.Number.from.Keyboard.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.3.4.Inputting.a.Number.from.Keyboard.webm",

                    "size": 74221505,

                    "description": "6 3 4 Inputting a Number from Keyboard"

                },
                {

                    "name": "6.3.5.Integer.Division.and.Division.with.Remainder.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.3.5.Integer.Division.and.Division.with.Remainder.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.3.5.Integer.Division.and.Division.with.Remainder.webm",

                    "size": 72135996,

                    "description": "6 3 5 Integer Division and Division with Remainder"

                },
                {

                    "name": "6.3.6.Shorthand.Operators.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.3.6.Shorthand.Operators.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.3.6.Shorthand.Operators.webm",

                    "size": 59819453,

                    "description": "6 3 6 Shorthand Operators"

                },
                {

                    "name": "6.3.7.Practical.Work.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.3.7.Practical.Work.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.3.7.Practical.Work.webm",

                    "size": 54005978,

                    "description": "6 3 7 Practical Work"

                },
                {

                    "name": "6.4.1.Homework.Review.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.4.1.Homework.Review.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.4.1.Homework.Review.webm",

                    "size": 72276404,

                    "description": "6 4 1 Homework Review"

                },
                {

                    "name": "6.4.2.Conditional.Operator.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.4.2.Conditional.Operator.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.4.2.Conditional.Operator.webm",

                    "size": 165607722,

                    "description": "6 4 2 Conditional Operator"

                },
                {

                    "name": "6.4.3.Full.Form.of.Conditional.Operator.if.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.4.3.Full.Form.of.Conditional.Operator.if.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.4.3.Full.Form.of.Conditional.Operator.if.webm",

                    "size": 100698803,

                    "description": "6 4 3 Full Form of Conditional Operator if"

                },
                {

                    "name": "6.4.4.Comments.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.4.4.Comments.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.4.4.Comments.webm",

                    "size": 102220223,

                    "description": "6 4 4 Comments"

                },
                {

                    "name": "6.5.1.Homework.Review.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.5.1.Homework.Review.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.5.1.Homework.Review.webm",

                    "size": 45207502,

                    "description": "6 5 1 Homework Review"

                },
                {

                    "name": "6.5.2.Nested.Conditions.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.5.2.Nested.Conditions.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.5.2.Nested.Conditions.webm",

                    "size": 99744254,

                    "description": "6 5 2 Nested Conditions"

                },
                {

                    "name": "6.5.3.Chains.of.Conditions.if-elif-else.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.5.3.Chains.of.Conditions.if-elif-else.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.5.3.Chains.of.Conditions.if-elif-else.webm",

                    "size": 76946344,

                    "description": "6 5 3 Chains of Conditions if-elif-else"

                },
                {

                    "name": "6.5.4.Logical.Operators.and.and.or.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.5.4.Logical.Operators.and.and.or.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.5.4.Logical.Operators.and.and.or.webm",

                    "size": 125582621,

                    "description": "6 5 4 Logical Operators and and or"

                },
                {

                    "name": "6.5.5.Using.Multiple.Logical.Operators.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.5.5.Using.Multiple.Logical.Operators.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.5.5.Using.Multiple.Logical.Operators.webm",

                    "size": 136706522,

                    "description": "6 5 5 Using Multiple Logical Operators"

                },
                {

                    "name": "6.6.1.Analysis.of.Practical.Work.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.6.1.Analysis.of.Practical.Work.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.6.1.Analysis.of.Practical.Work.webm",

                    "size": 86178463,

                    "description": "6 6 1 Analysis of Practical Work"

                },
                {

                    "name": "6.6.2.While.Operator.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.6.2.While.Operator.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.6.2.While.Operator.webm",

                    "size": 119003660,

                    "description": "6 6 2 While Operator"

                },
                {

                    "name": "6.6.3.Breaking.the.Loop.Break.Operator.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.6.3.Breaking.the.Loop.Break.Operator.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.6.3.Breaking.the.Loop.Break.Operator.webm",

                    "size": 89260033,

                    "description": "6 6 3 Breaking the Loop Break Operator"

                },
                {

                    "name": "6.6.4.Infinite.Loop.Boolean.Data.Type.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.6.4.Infinite.Loop.Boolean.Data.Type.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.6.4.Infinite.Loop.Boolean.Data.Type.webm",

                    "size": 102933468,

                    "description": "6 6 4 Infinite Loop Boolean Data Type"

                },
                {

                    "name": "6.6.5.While.Loop.with.Counter.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.6.5.While.Loop.with.Counter.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.6.5.While.Loop.with.Counter.webm",

                    "size": 78139919,

                    "description": "6 6 5 While Loop with Counter"

                },
                {

                    "name": "6.6.6.Continue.Operator.in.While.Loop.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.6.6.Continue.Operator.in.While.Loop.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.6.6.Continue.Operator.in.While.Loop.webm",

                    "size": 75008730,

                    "description": "6 6 6 Continue Operator in While Loop"

                },
                {

                    "name": "6.7.1.Homework.Review.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.7.1.Homework.Review.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.7.1.Homework.Review.webm",

                    "size": 93752696,

                    "description": "6 7 1 Homework Review"

                },
                {

                    "name": "6.7.2.For.Loop.Working.with.List.of.Numbers.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.7.2.For.Loop.Working.with.List.of.Numbers.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.7.2.For.Loop.Working.with.List.of.Numbers.webm",

                    "size": 83781689,

                    "description": "6 7 2 For Loop Working with List of Numbers"

                },
                {

                    "name": "6.7.3.Function.range.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.7.3.Function.range.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.7.3.Function.range.webm",

                    "size": 114267197,

                    "description": "6 7 3 Function range"

                },
                {

                    "name": "6.7.4.Function.range.with.Start.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.7.4.Function.range.with.Start.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.7.4.Function.range.with.Start.webm",

                    "size": 142743461,

                    "description": "6 7 4 Function range with Start"

                },
                {

                    "name": "6.7.5.Typical.Algorithms.with.Counting.Loops.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.7.5.Typical.Algorithms.with.Counting.Loops.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.7.5.Typical.Algorithms.with.Counting.Loops.webm",

                    "size": 97083063,

                    "description": "6 7 5 Typical Algorithms with Counting Loops"

                },
                {

                    "name": "6.8.1.Homework.Review.For.Loops.Part.2.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.8.1.Homework.Review.For.Loops.Part.2.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.8.1.Homework.Review.For.Loops.Part.2.webm",

                    "size": 80825314,

                    "description": "6 8 1 Homework Review For Loops Part 2"

                },
                {

                    "name": "6.8.2.Algorithmic.Tasks.with.Counting.Loops.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.8.2.Algorithmic.Tasks.with.Counting.Loops.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.8.2.Algorithmic.Tasks.with.Counting.Loops.webm",

                    "size": 122243156,

                    "description": "6 8 2 Algorithmic Tasks with Counting Loops"

                },
                {

                    "name": "6.8.3.Function.range.start.stop.step.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.8.3.Function.range.start.stop.step.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.8.3.Function.range.start.stop.step.webm",

                    "size": 142208847,

                    "description": "6 8 3 Function range start stop step"

                },
                {

                    "name": "6.8.4.Negative.Step.in.Function.range.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.8.4.Negative.Step.in.Function.range.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.8.4.Negative.Step.in.Function.range.webm",

                    "size": 118322378,

                    "description": "6 8 4 Negative Step in Function range"

                },
                {

                    "name": "6.8.5.User.Input.and.Function.range.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.8.5.User.Input.and.Function.range.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.8.5.User.Input.and.Function.range.webm",

                    "size": 135584400,

                    "description": "6 8 5 User Input and Function range"

                },
                {

                    "name": "6.9.1.Homework.Review.For.Loop.Working.with.Strings.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.9.1.Homework.Review.For.Loop.Working.with.Strings.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.9.1.Homework.Review.For.Loop.Working.with.Strings.webm",

                    "size": 55505976,

                    "description": "6 9 1 Homework Review For Loop Working with Strings"

                },
                {

                    "name": "6.9.2.String.Comparison.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.9.2.String.Comparison.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.9.2.String.Comparison.webm",

                    "size": 66120732,

                    "description": "6 9 2 String Comparison"

                },
                {

                    "name": "6.9.3.For.Loop.Iterating.Over.a.String.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.9.3.For.Loop.Iterating.Over.a.String.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.9.3.For.Loop.Iterating.Over.a.String.webm",

                    "size": 90728108,

                    "description": "6 9 3 For Loop Iterating Over a String"

                },
                {

                    "name": "6.9.4.Additional.Possibilities.of.the.print.Function.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.9.4.Additional.Possibilities.of.the.print.Function.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.9.4.Additional.Possibilities.of.the.print.Function.webm",

                    "size": 67686476,

                    "description": "6 9 4 Additional Possibilities of the print Function"

                },
                {

                    "name": "6.9.5.Typical.Algorithms.for.Working.with.Strings.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.9.5.Typical.Algorithms.for.Working.with.Strings.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/6.0.0/6.9.5.Typical.Algorithms.for.Working.with.Strings.webm",

                    "size": 93781278,

                    "description": "6 9 5 Typical Algorithms for Working with Strings"

                }
        ],
        "5.0.0": [
                {

                    "name": "5.1.1.Introduction.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.1.1.Introduction.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.1.1.Introduction.webm",

                    "size": 38282309,

                    "description": "5 1 1 Introduction"

                },
                {

                    "name": "5.1.2.Database.Overview.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.1.2.Database.Overview.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.1.2.Database.Overview.webm",

                    "size": 732381926,

                    "description": "5 1 2 Database Overview"

                },
                {

                    "name": "5.1.3.On.Premise.Databases.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.1.3.On.Premise.Databases.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.1.3.On.Premise.Databases.webm",

                    "size": 187290811,

                    "description": "5 1 3 On Premise Databases"

                },
                {

                    "name": "5.1.4.Cloud.Databases.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.1.4.Cloud.Databases.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.1.4.Cloud.Databases.webm",

                    "size": 312860546,

                    "description": "5 1 4 Cloud Databases"

                },
                {

                    "name": "5.1.5.Mobile.Databases.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.1.5.Mobile.Databases.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.1.5.Mobile.Databases.webm",

                    "size": 312325069,

                    "description": "5 1 5 Mobile Databases"

                },
                {

                    "name": "5.1.6.Database.Usage.Options.Comparison.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.1.6.Database.Usage.Options.Comparison.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.1.6.Database.Usage.Options.Comparison.webm",

                    "size": 129468269,

                    "description": "5 1 6 Database Usage Options Comparison"

                },
                {

                    "name": "5.2.1.Relational.Databases.Basics.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.1.Relational.Databases.Basics.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.1.Relational.Databases.Basics.webm",

                    "size": 44370461,

                    "description": "5 2 1 Relational Databases Basics"

                },
                {

                    "name": "5.2.3.MySQL.Setup.and.Usage.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.3.MySQL.Setup.and.Usage.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.3.MySQL.Setup.and.Usage.webm",

                    "size": 114606477,

                    "description": "5 2 3 MySQL Setup and Usage"

                },
                {

                    "name": "5.2.4.SQL.Query.Language.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.4.SQL.Query.Language.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.4.SQL.Query.Language.webm",

                    "size": 173022048,

                    "description": "5 2 4 SQL Query Language"

                },
                {

                    "name": "5.2.5.SELECT.Queries.and.Data.Filtering.1.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.5.SELECT.Queries.and.Data.Filtering.1.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.5.SELECT.Queries.and.Data.Filtering.1.webm",

                    "size": 50755853,

                    "description": "5 2 5 SELECT Queries and Data Filtering 1"

                },
                {

                    "name": "5.2.5.SELECT.Queries.and.Data.Filtering.2.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.5.SELECT.Queries.and.Data.Filtering.2.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.5.SELECT.Queries.and.Data.Filtering.2.webm",

                    "size": 22239062,

                    "description": "5 2 5 SELECT Queries and Data Filtering 2"

                },
                {

                    "name": "5.2.5.SELECT.Queries.and.Data.Filtering.3.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.5.SELECT.Queries.and.Data.Filtering.3.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.5.SELECT.Queries.and.Data.Filtering.3.webm",

                    "size": 20832688,

                    "description": "5 2 5 SELECT Queries and Data Filtering 3"

                },
                {

                    "name": "5.2.5.SELECT.Queries.and.Data.Filtering.4.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.5.SELECT.Queries.and.Data.Filtering.4.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.5.SELECT.Queries.and.Data.Filtering.4.webm",

                    "size": 21269743,

                    "description": "5 2 5 SELECT Queries and Data Filtering 4"

                },
                {

                    "name": "5.2.6.Sorting.and.Grouping.Results.1.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.6.Sorting.and.Grouping.Results.1.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.6.Sorting.and.Grouping.Results.1.webm",

                    "size": 19493793,

                    "description": "5 2 6 Sorting and Grouping Results 1"

                },
                {

                    "name": "5.2.6.Sorting.and.Grouping.Results.2.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.6.Sorting.and.Grouping.Results.2.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.6.Sorting.and.Grouping.Results.2.webm",

                    "size": 39906956,

                    "description": "5 2 6 Sorting and Grouping Results 2"

                },
                {

                    "name": "5.2.6.Sorting.and.Grouping.Results.3.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.6.Sorting.and.Grouping.Results.3.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.6.Sorting.and.Grouping.Results.3.webm",

                    "size": 29363581,

                    "description": "5 2 6 Sorting and Grouping Results 3"

                },
                {

                    "name": "5.2.6.Sorting.and.Grouping.Results.4.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.6.Sorting.and.Grouping.Results.4.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.6.Sorting.and.Grouping.Results.4.webm",

                    "size": 28934765,

                    "description": "5 2 6 Sorting and Grouping Results 4"

                },
                {

                    "name": "5.2.6.Sorting.and.Grouping.Results.5.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.6.Sorting.and.Grouping.Results.5.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.6.Sorting.and.Grouping.Results.5.webm",

                    "size": 17304029,

                    "description": "5 2 6 Sorting and Grouping Results 5"

                },
                {

                    "name": "5.2.6.Sorting.and.Grouping.Results.6.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.6.Sorting.and.Grouping.Results.6.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.6.Sorting.and.Grouping.Results.6.webm",

                    "size": 24724369,

                    "description": "5 2 6 Sorting and Grouping Results 6"

                },
                {

                    "name": "5.2.7.Joining.Tables.and.Results.JOIN.and.UNION.Operators.1.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.7.Joining.Tables.and.Results.JOIN.and.UNION.Operators.1.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.7.Joining.Tables.and.Results.JOIN.and.UNION.Operators.1.webm",

                    "size": 30199993,

                    "description": "5 2 7 Joining Tables and Results JOIN and UNION Operators 1"

                },
                {

                    "name": "5.2.7.Joining.Tables.and.Results.JOIN.and.UNION.Operators.2.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.7.Joining.Tables.and.Results.JOIN.and.UNION.Operators.2.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.7.Joining.Tables.and.Results.JOIN.and.UNION.Operators.2.webm",

                    "size": 79037730,

                    "description": "5 2 7 Joining Tables and Results JOIN and UNION Operators 2"

                },
                {

                    "name": "5.2.7.Joining.Tables.and.Results.JOIN.and.UNION.Operators.3.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.7.Joining.Tables.and.Results.JOIN.and.UNION.Operators.3.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.7.Joining.Tables.and.Results.JOIN.and.UNION.Operators.3.webm",

                    "size": 80969743,

                    "description": "5 2 7 Joining Tables and Results JOIN and UNION Operators 3"

                },
                {

                    "name": "5.2.7.Joining.Tables.and.Results.JOIN.and.UNION.Operators.4.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.7.Joining.Tables.and.Results.JOIN.and.UNION.Operators.4.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.7.Joining.Tables.and.Results.JOIN.and.UNION.Operators.4.webm",

                    "size": 57406185,

                    "description": "5 2 7 Joining Tables and Results JOIN and UNION Operators 4"

                },
                {

                    "name": "5.2.8.Data.Modification.Queries.UPDATE.INSERT.and.DELETE.1.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.8.Data.Modification.Queries.UPDATE.INSERT.and.DELETE.1.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.8.Data.Modification.Queries.UPDATE.INSERT.and.DELETE.1.webm",

                    "size": 26004115,

                    "description": "5 2 8 Data Modification Queries UPDATE INSERT and DELETE 1"

                },
                {

                    "name": "5.2.8.Data.Modification.Queries.UPDATE.INSERT.and.DELETE.2.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.8.Data.Modification.Queries.UPDATE.INSERT.and.DELETE.2.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.8.Data.Modification.Queries.UPDATE.INSERT.and.DELETE.2.webm",

                    "size": 12059880,

                    "description": "5 2 8 Data Modification Queries UPDATE INSERT and DELETE 2"

                },
                {

                    "name": "5.2.8.Data.Modification.Queries.UPDATE.INSERT.and.DELETE.3.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.8.Data.Modification.Queries.UPDATE.INSERT.and.DELETE.3.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.8.Data.Modification.Queries.UPDATE.INSERT.and.DELETE.3.webm",

                    "size": 31684514,

                    "description": "5 2 8 Data Modification Queries UPDATE INSERT and DELETE 3"

                },
                {

                    "name": "5.2.8.Data.Modification.Queries.UPDATE.INSERT.and.DELETE.4.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.8.Data.Modification.Queries.UPDATE.INSERT.and.DELETE.4.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.8.Data.Modification.Queries.UPDATE.INSERT.and.DELETE.4.webm",

                    "size": 15148334,

                    "description": "5 2 8 Data Modification Queries UPDATE INSERT and DELETE 4"

                },
                {

                    "name": "5.2.9.Structural.Queries.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.9.Structural.Queries.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.2.9.Structural.Queries.webm",

                    "size": 95490737,

                    "description": "5 2 9 Structural Queries"

                },
                {

                    "name": "5.3.1.Database.Architecture.on.the.Example.of.PostgreSQL.and.MongoDB.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.3.1.Database.Architecture.on.the.Example.of.PostgreSQL.and.MongoDB.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.3.1.Database.Architecture.on.the.Example.of.PostgreSQL.and.MongoDB.webm",

                    "size": 579319583,

                    "description": "5 3 1 Database Architecture on the Example of PostgreSQL and MongoDB"

                },
                {

                    "name": "5.3.2.Authentication.in.Databases.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.3.2.Authentication.in.Databases.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.3.2.Authentication.in.Databases.webm",

                    "size": 338848056,

                    "description": "5 3 2 Authentication in Databases"

                },
                {

                    "name": "5.3.3.Database.Utilities.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.3.3.Database.Utilities.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.3.3.Database.Utilities.webm",

                    "size": 227601705,

                    "description": "5 3 3 Database Utilities"

                },
                {

                    "name": "5.3.4.Users.and.Roles.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.3.4.Users.and.Roles.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.3.4.Users.and.Roles.webm",

                    "size": 223447333,

                    "description": "5 3 4 Users and Roles"

                },
                {

                    "name": "5.3.5.Server.Procedures.in.Databases.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.3.5.Server.Procedures.in.Databases.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.3.5.Server.Procedures.in.Databases.webm",

                    "size": 170563562,

                    "description": "5 3 5 Server Procedures in Databases"

                },
                {

                    "name": "5.4.1.Levels.of.System.Criticality.and.Data.Value.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.4.1.Levels.of.System.Criticality.and.Data.Value.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.4.1.Levels.of.System.Criticality.and.Data.Value.webm",

                    "size": 155958068,

                    "description": "5 4 1 Levels of System Criticality and Data Value"

                },
                {

                    "name": "5.4.2.DB.Recovery.and.Backup.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.4.2.DB.Recovery.and.Backup.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.4.2.DB.Recovery.and.Backup.webm",

                    "size": 209867598,

                    "description": "5 4 2 DB Recovery and Backup"

                },
                {

                    "name": "5.4.3.Export.and.Import.of.Data.in.PostgreSQL.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.4.3.Export.and.Import.of.Data.in.PostgreSQL.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.4.3.Export.and.Import.of.Data.in.PostgreSQL.webm",

                    "size": 166315894,

                    "description": "5 4 3 Export and Import of Data in PostgreSQL"

                },
                {

                    "name": "5.4.4.Hot.DB.Backup.on.PostgreSQL.Example.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.4.4.Hot.DB.Backup.on.PostgreSQL.Example.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.4.4.Hot.DB.Backup.on.PostgreSQL.Example.webm",

                    "size": 378680002,

                    "description": "5 4 4 Hot DB Backup on PostgreSQL Example"

                },
                {

                    "name": "5.4.5.Data.Flows.Vulnerability.Elimination.and.Software.Updates.DB.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.4.5.Data.Flows.Vulnerability.Elimination.and.Software.Updates.DB.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.4.5.Data.Flows.Vulnerability.Elimination.and.Software.Updates.DB.webm",

                    "size": 211285077,

                    "description": "5 4 5 Data Flows Vulnerability Elimination and Software Updates DB"

                },
                {

                    "name": "5.5.1.Introduction.to.the.Module.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.5.1.Introduction.to.the.Module.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.5.1.Introduction.to.the.Module.webm",

                    "size": 43439424,

                    "description": "5 5 1 Introduction to the Module"

                },
                {

                    "name": "5.5.2.Row.Level.Security.RLS.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.5.2.Row.Level.Security.RLS.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.5.2.Row.Level.Security.RLS.webm",

                    "size": 257163411,

                    "description": "5 5 2 Row Level Security RLS"

                },
                {

                    "name": "5.5.3.Transparent.Data.Encryption.Technologies.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.5.3.Transparent.Data.Encryption.Technologies.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.5.3.Transparent.Data.Encryption.Technologies.webm",

                    "size": 195453249,

                    "description": "5 5 3 Transparent Data Encryption Technologies"

                },
                {

                    "name": "5.5.4.Encryption.Using.DB.Means.pgcrypto.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.5.4.Encryption.Using.DB.Means.pgcrypto.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.5.4.Encryption.Using.DB.Means.pgcrypto.webm",

                    "size": 91228749,

                    "description": "5 5 4 Encryption Using DB Means pgcrypto"

                },
                {

                    "name": "5.5.5.Data.Masking.and.Anonymization.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.5.5.Data.Masking.and.Anonymization.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.5.5.Data.Masking.and.Anonymization.webm",

                    "size": 210298405,

                    "description": "5 5 5 Data Masking and Anonymization"

                },
                {

                    "name": "5.5.6.Obfuscation.of.Procedures.and.Functions.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.5.6.Obfuscation.of.Procedures.and.Functions.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/5.0.0/5.5.6.Obfuscation.of.Procedures.and.Functions.webm",

                    "size": 136194517,

                    "description": "5 5 6 Obfuscation of Procedures and Functions"

                }
        ],
        "4.0.0": [
                {

                    "name": "4.1.1.Introduction.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.1.1.Introduction.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.1.1.Introduction.webm",

                    "size": 26973509,

                    "description": "4 1 1 Introduction"

                },
                {

                    "name": "4.1.2.Local.Administration.Policies.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.1.2.Local.Administration.Policies.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.1.2.Local.Administration.Policies.webm",

                    "size": 310595591,

                    "description": "4 1 2 Local Administration Policies"

                },
                {

                    "name": "4.1.3.Local.Administration.Tools.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.1.3.Local.Administration.Tools.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.1.3.Local.Administration.Tools.webm",

                    "size": 305365913,

                    "description": "4 1 3 Local Administration Tools"

                },
                {

                    "name": "4.1.4.Storing.Credentials.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.1.4.Storing.Credentials.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.1.4.Storing.Credentials.webm",

                    "size": 222691610,

                    "description": "4 1 4 Storing Credentials"

                },
                {

                    "name": "4.1.5.Attacks.Aimed.at.Stealing.Credentials.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.1.5.Attacks.Aimed.at.Stealing.Credentials.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.1.5.Attacks.Aimed.at.Stealing.Credentials.webm",

                    "size": 395184318,

                    "description": "4 1 5 Attacks Aimed at Stealing Credentials"

                },
                {

                    "name": "4.1.6.Protecting.Credentials.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.1.6.Protecting.Credentials.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.1.6.Protecting.Credentials.webm",

                    "size": 227705859,

                    "description": "4 1 6 Protecting Credentials"

                },
                {

                    "name": "4.2.1.Group.Policy.Access.Management.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.2.1.Group.Policy.Access.Management.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.2.1.Group.Policy.Access.Management.webm",

                    "size": 15546823,

                    "description": "4 2 1 Group Policy Access Management"

                },
                {

                    "name": "4.2.2.Preparing.Work.Environment.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.2.2.Preparing.Work.Environment.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.2.2.Preparing.Work.Environment.webm",

                    "size": 255545095,

                    "description": "4 2 2 Preparing Work Environment"

                },
                {

                    "name": "4.2.3.Configuring.Group.Policy.Parameters.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.2.3.Configuring.Group.Policy.Parameters.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.2.3.Configuring.Group.Policy.Parameters.webm",

                    "size": 150843956,

                    "description": "4 2 3 Configuring Group Policy Parameters"

                },
                {

                    "name": "4.2.4.Using.Group.Policy.for.Remote.Software.Installation.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.2.4.Using.Group.Policy.for.Remote.Software.Installation.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.2.4.Using.Group.Policy.for.Remote.Software.Installation.webm",

                    "size": 157345305,

                    "description": "4 2 4 Using Group Policy for Remote Software Installation"

                },
                {

                    "name": "4.2.5.Configuring.Group.Policy.Parameters.for.Automatic.Updates.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.2.5.Configuring.Group.Policy.Parameters.for.Automatic.Updates.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.2.5.Configuring.Group.Policy.Parameters.for.Automatic.Updates.webm",

                    "size": 451992004,

                    "description": "4 2 5 Configuring Group Policy Parameters for Automatic Updates"

                },
                {

                    "name": "4.2.6.Advanced.Group.Policy.Management.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.2.6.Advanced.Group.Policy.Management.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.2.6.Advanced.Group.Policy.Management.webm",

                    "size": 353855164,

                    "description": "4 2 6 Advanced Group Policy Management"

                },
                {

                    "name": "4.2.7.Summary.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.2.7.Summary.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.2.7.Summary.webm",

                    "size": 6722936,

                    "description": "4 2 7 Summary"

                },
                {

                    "name": "4.3.1.Security.Audit.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.3.1.Security.Audit.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.3.1.Security.Audit.webm",

                    "size": 167231825,

                    "description": "4 3 1 Security Audit"

                },
                {

                    "name": "4.3.2.Basic.Security.Audit.Policies.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.3.2.Basic.Security.Audit.Policies.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.3.2.Basic.Security.Audit.Policies.webm",

                    "size": 185956597,

                    "description": "4 3 2 Basic Security Audit Policies"

                },
                {

                    "name": "4.3.3.Advanced.Security.Audit.Policies.Part1.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.3.3.Advanced.Security.Audit.Policies.Part1.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.3.3.Advanced.Security.Audit.Policies.Part1.webm",

                    "size": 379832182,

                    "description": "4 3 3 Advanced Security Audit Policies Part1"

                },
                {

                    "name": "4.3.4.Advanced.Security.Audit.Policies.Part2.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.3.4.Advanced.Security.Audit.Policies.Part2.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.3.4.Advanced.Security.Audit.Policies.Part2.webm",

                    "size": 332443032,

                    "description": "4 3 4 Advanced Security Audit Policies Part2"

                },
                {

                    "name": "4.3.5.Planning.and.Deploying.Advanced.Security.Audit.Policies.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.3.5.Planning.and.Deploying.Advanced.Security.Audit.Policies.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.3.5.Planning.and.Deploying.Advanced.Security.Audit.Policies.webm",

                    "size": 158973934,

                    "description": "4 3 5 Planning and Deploying Advanced Security Audit Policies"

                },
                {

                    "name": "4.3.6.Using.Advanced.Security.Audit.Capabilities.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.3.6.Using.Advanced.Security.Audit.Capabilities.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.3.6.Using.Advanced.Security.Audit.Capabilities.webm",

                    "size": 119037341,

                    "description": "4 3 6 Using Advanced Security Audit Capabilities"

                },
                {

                    "name": "4.4.1.Local.Accounts.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.4.1.Local.Accounts.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.4.1.Local.Accounts.webm",

                    "size": 246937847,

                    "description": "4 4 1 Local Accounts"

                },
                {

                    "name": "4.4.2.Service.Accounts.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.4.2.Service.Accounts.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.4.2.Service.Accounts.webm",

                    "size": 138702453,

                    "description": "4 4 2 Service Accounts"

                },
                {

                    "name": "4.4.3.Microsoft.Accounts.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.4.3.Microsoft.Accounts.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.4.3.Microsoft.Accounts.webm",

                    "size": 348174359,

                    "description": "4 4 3 Microsoft Accounts"

                },
                {

                    "name": "4.4.4.User.Account.Control.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.4.4.User.Account.Control.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.4.4.User.Account.Control.webm",

                    "size": 180460496,

                    "description": "4 4 4 User Account Control"

                },
                {

                    "name": "4.4.5.Windows.Firewall.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.4.5.Windows.Firewall.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.4.5.Windows.Firewall.webm",

                    "size": 257172877,

                    "description": "4 4 5 Windows Firewall"

                },
                {

                    "name": "4.5.1.Introduction.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.5.1.Introduction.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.5.1.Introduction.webm",

                    "size": 10114929,

                    "description": "4 5 1 Introduction"

                },
                {

                    "name": "4.5.2.Digital.Signatures.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.5.2.Digital.Signatures.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.5.2.Digital.Signatures.webm",

                    "size": 244061909,

                    "description": "4 5 2 Digital Signatures"

                },
                {

                    "name": "4.5.3.Using.Digital.Signatures.for.Authenticity.Verification.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.5.3.Using.Digital.Signatures.for.Authenticity.Verification.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.5.3.Using.Digital.Signatures.for.Authenticity.Verification.webm",

                    "size": 182967551,

                    "description": "4 5 3 Using Digital Signatures for Authenticity Verification"

                },
                {

                    "name": "4.5.4.Creating.a.Digital.Signature.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.5.4.Creating.a.Digital.Signature.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.5.4.Creating.a.Digital.Signature.webm",

                    "size": 343326231,

                    "description": "4 5 4 Creating a Digital Signature"

                },
                {

                    "name": "4.5.5.Using.Digital.Signatures.for.Signing.Files.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.5.5.Using.Digital.Signatures.for.Signing.Files.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.5.5.Using.Digital.Signatures.for.Signing.Files.webm",

                    "size": 241007127,

                    "description": "4 5 5 Using Digital Signatures for Signing Files"

                },
                {

                    "name": "4.5.6.Verifying.Digital.Signatures.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.5.6.Verifying.Digital.Signatures.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.5.6.Verifying.Digital.Signatures.webm",

                    "size": 89200973,

                    "description": "4 5 6 Verifying Digital Signatures"

                },
                {

                    "name": "4.6.1.Registry.Description.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.6.1.Registry.Description.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.6.1.Registry.Description.webm",

                    "size": 120665165,

                    "description": "4 6 1 Registry Description"

                },
                {

                    "name": "4.6.2.Information.in.the.Registry.Monitoring.Changes.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.6.2.Information.in.the.Registry.Monitoring.Changes.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.6.2.Information.in.the.Registry.Monitoring.Changes.webm",

                    "size": 491529468,

                    "description": "4 6 2 Information in the Registry Monitoring Changes"

                },
                {

                    "name": "4.6.3.Registry.Backup.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.6.3.Registry.Backup.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.6.3.Registry.Backup.webm",

                    "size": 286508801,

                    "description": "4 6 3 Registry Backup"

                },
                {

                    "name": "4.6.4.Registry.Recovery.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.6.4.Registry.Recovery.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.6.4.Registry.Recovery.webm",

                    "size": 409779610,

                    "description": "4 6 4 Registry Recovery"

                },
                {

                    "name": "4.7.1.Working.with.Objects.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.7.1.Working.with.Objects.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.7.1.Working.with.Objects.webm",

                    "size": 474445503,

                    "description": "4 7 1 Working with Objects"

                },
                {

                    "name": "4.7.2.Managing.Computers.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.7.2.Managing.Computers.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.7.2.Managing.Computers.webm",

                    "size": 322987890,

                    "description": "4 7 2 Managing Computers"

                },
                {

                    "name": "4.7.3.Managing.Processes.and.Services.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.7.3.Managing.Processes.and.Services.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.7.3.Managing.Processes.and.Services.webm",

                    "size": 323185336,

                    "description": "4 7 3 Managing Processes and Services"

                },
                {

                    "name": "4.7.4.Managing.Disks.and.Files.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.7.4.Managing.Disks.and.Files.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.7.4.Managing.Disks.and.Files.webm",

                    "size": 891041212,

                    "description": "4 7 4 Managing Disks and Files"

                },
                {

                    "name": "4.7.5.Working.with.Network.and.Data.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.7.5.Working.with.Network.and.Data.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.7.5.Working.with.Network.and.Data.webm",

                    "size": 921073593,

                    "description": "4 7 5 Working with Network and Data"

                },
                {

                    "name": "4.8.1.Starting.Work.with.Active.Directory.Domain.Services.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.8.1.Starting.Work.with.Active.Directory.Domain.Services.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.8.1.Starting.Work.with.Active.Directory.Domain.Services.webm",

                    "size": 395191745,

                    "description": "4 8 1 Starting Work with Active Directory Domain Services"

                },
                {

                    "name": "4.8.2.Planning.and.Designing.Domain.Services.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.8.2.Planning.and.Designing.Domain.Services.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.8.2.Planning.and.Designing.Domain.Services.webm",

                    "size": 287566584,

                    "description": "4 8 2 Planning and Designing Domain Services"

                },
                {

                    "name": "4.8.3.Installation.and.Demotion.of.Domain.Services.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.8.3.Installation.and.Demotion.of.Domain.Services.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.8.3.Installation.and.Demotion.of.Domain.Services.webm",

                    "size": 493673250,

                    "description": "4 8 3 Installation and Demotion of Domain Services"

                },
                {

                    "name": "4.8.4.Accounts.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.8.4.Accounts.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/4.0.0/4.8.4.Accounts.webm",

                    "size": 431523855,

                    "description": "4 8 4 Accounts"

                }
        ],
        "3.0.0": [
                {

                    "name": "1.1.Principles.of.Building.Networks.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/1.1.Principles.of.Building.Networks.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/1.1.Principles.of.Building.Networks.txt",

                    "size": 66967353,

                    "description": "1 1 Principles of Building Networks"

                },
                {

                    "name": "1.2.OSI.Model.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/1.2.OSI.Model.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/1.2.OSI.Model.txt",

                    "size": 57871564,

                    "description": "1 2 OSI Model"

                },
                {

                    "name": "1.3.Network.File.System.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/1.3.Network.File.System.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/1.3.Network.File.System.txt",

                    "size": 7892575,

                    "description": "1 3 Network File System"

                },
                {

                    "name": "10.1.Monitoring.and.Alerts.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/10.1.Monitoring.and.Alerts.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/10.1.Monitoring.and.Alerts.txt",

                    "size": 39310617,

                    "description": "10 1 Monitoring and Alerts"

                },
                {

                    "name": "10.2.Installation.and.Configuration.of.NIDS.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/10.2.Installation.and.Configuration.of.NIDS.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/10.2.Installation.and.Configuration.of.NIDS.txt",

                    "size": 79396426,

                    "description": "10 2 Installation and Configuration of NIDS"

                },
                {

                    "name": "10.3.Checking.System.Performance.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/10.3.Checking.System.Performance.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/10.3.Checking.System.Performance.txt",

                    "size": 265224988,

                    "description": "10 3 Checking System Performance"

                },
                {

                    "name": "2.1.Protocols.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/2.1.Protocols.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/2.1.Protocols.txt",

                    "size": 53073362,

                    "description": "2 1 Protocols"

                },
                {

                    "name": "2.2.ICMP.Protocol.Work.and.Other.Network.Level.Protocols.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/2.2.ICMP.Protocol.Work.and.Other.Network.Level.Protocols.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/2.2.ICMP.Protocol.Work.and.Other.Network.Level.Protocols.txt",

                    "size": 151926320,

                    "description": "2 2 ICMP Protocol Work and Other Network Level Protocols"

                },
                {

                    "name": "2.3.IPsec.Protocol.Set.Work.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/2.3.IPsec.Protocol.Set.Work.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/2.3.IPsec.Protocol.Set.Work.txt",

                    "size": 23063811,

                    "description": "2 3 IPsec Protocol Set Work"

                },
                {

                    "name": "2.4.Transport.Level.Protocols.Work.TCP.IP.Protocol.Stack.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/2.4.Transport.Level.Protocols.Work.TCP.IP.Protocol.Stack.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/2.4.Transport.Level.Protocols.Work.TCP.IP.Protocol.Stack.txt",

                    "size": 90820852,

                    "description": "2 4 Transport Level Protocols Work TCP IP Protocol Stack"

                },
                {

                    "name": "2.5.FTP.Protocol.Work.and.Other.Application.Level.Protocols.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/2.5.FTP.Protocol.Work.and.Other.Application.Level.Protocols.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/2.5.FTP.Protocol.Work.and.Other.Application.Level.Protocols.txt",

                    "size": 51699881,

                    "description": "2 5 FTP Protocol Work and Other Application Level Protocols"

                },
                {

                    "name": "3.1.Network.Routes.and.Routing.Table.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/3.1.Network.Routes.and.Routing.Table.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/3.1.Network.Routes.and.Routing.Table.txt",

                    "size": 103351202,

                    "description": "3 1 Network Routes and Routing Table"

                },
                {

                    "name": "3.2.Static.Routing.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/3.2.Static.Routing.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/3.2.Static.Routing.txt",

                    "size": 58316118,

                    "description": "3 2 Static Routing"

                },
                {

                    "name": "3.3.Dynamic.Routing.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/3.3.Dynamic.Routing.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/3.3.Dynamic.Routing.txt",

                    "size": 73323250,

                    "description": "3 3 Dynamic Routing"

                },
                {

                    "name": "3.4.inetd.xinetd.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/3.4.inetd.xinetd.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/3.4.inetd.xinetd.txt",

                    "size": 41264987,

                    "description": "3 4 inetd xinetd"

                },
                {

                    "name": "3.5.Remote.Access.Configuration.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/3.5.Remote.Access.Configuration.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/3.5.Remote.Access.Configuration.txt",

                    "size": 216298332,

                    "description": "3 5 Remote Access Configuration"

                },
                {

                    "name": "3.6.Work.with.Mail.Service.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/3.6.Work.with.Mail.Service.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/3.6.Work.with.Mail.Service.txt",

                    "size": 116195438,

                    "description": "3 6 Work with Mail Service"

                },
                {

                    "name": "4.1.NFS.Basics.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/4.1.NFS.Basics.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/4.1.NFS.Basics.txt",

                    "size": 19313263,

                    "description": "4 1 NFS Basics"

                },
                {

                    "name": "4.2.NFS.Analysis.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/4.2.NFS.Analysis.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/4.2.NFS.Analysis.txt",

                    "size": 195355169,

                    "description": "4 2 NFS Analysis"

                },
                {

                    "name": "4.3.DNS.Basics.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/4.3.DNS.Basics.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/4.3.DNS.Basics.txt",

                    "size": 25118805,

                    "description": "4 3 DNS Basics"

                },
                {

                    "name": "4.4.DNS.Work.Organization.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/4.4.DNS.Work.Organization.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/4.4.DNS.Work.Organization.txt",

                    "size": 142597514,

                    "description": "4 4 DNS Work Organization"

                },
                {

                    "name": "4.5.Wireless.Connections.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/4.5.Wireless.Connections.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/4.5.Wireless.Connections.txt",

                    "size": 66227523,

                    "description": "4 5 Wireless Connections"

                },
                {

                    "name": "5.1.Apache.Web.Server.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/5.1.Apache.Web.Server.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/5.1.Apache.Web.Server.txt",

                    "size": 52056716,

                    "description": "5 1 Apache Web Server"

                },
                {

                    "name": "5.2.Apache.Web.Server.Configuration.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/5.2.Apache.Web.Server.Configuration.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/5.2.Apache.Web.Server.Configuration.txt",

                    "size": 221518872,

                    "description": "5 2 Apache Web Server Configuration"

                },
                {

                    "name": "5.3.SSL.Technology.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/5.3.SSL.Technology.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/5.3.SSL.Technology.txt",

                    "size": 153249319,

                    "description": "5 3 SSL Technology"

                },
                {

                    "name": "6.1.Packet.Filters.Basics.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/6.1.Packet.Filters.Basics.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/6.1.Packet.Filters.Basics.txt",

                    "size": 26014673,

                    "description": "6 1 Packet Filters Basics"

                },
                {

                    "name": "6.2.Work.with.iptables.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/6.2.Work.with.iptables.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/6.2.Work.with.iptables.txt",

                    "size": 53086473,

                    "description": "6 2 Work with iptables"

                },
                {

                    "name": "6.3.Traffic.Management.with.iptables.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/6.3.Traffic.Management.with.iptables.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/6.3.Traffic.Management.with.iptables.txt",

                    "size": 597726651,

                    "description": "6 3 Traffic Management with iptables"

                },
                {

                    "name": "7.1.Network.Operability.Support.Basics.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/7.1.Network.Operability.Support.Basics.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/7.1.Network.Operability.Support.Basics.txt",

                    "size": 267945728,

                    "description": "7 1 Network Operability Support Basics"

                },
                {

                    "name": "7.2.Work.with.Network.Operability.Support.Utilities.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/7.2.Work.with.Network.Operability.Support.Utilities.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/7.2.Work.with.Network.Operability.Support.Utilities.txt",

                    "size": 417449023,

                    "description": "7 2 Work with Network Operability Support Utilities"

                },
                {

                    "name": "7.3.Network.Operability.Checks.Conducting.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/7.3.Network.Operability.Checks.Conducting.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/7.3.Network.Operability.Checks.Conducting.txt",

                    "size": 1274386378,

                    "description": "7 3 Network Operability Checks Conducting"

                },
                {

                    "name": "7.4.Logs.Work.Basics.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/7.4.Logs.Work.Basics.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/7.4.Logs.Work.Basics.txt",

                    "size": 623581069,

                    "description": "7 4 Logs Work Basics"

                },
                {

                    "name": "8.1.Basic.Incidents.in.Local.Network.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/8.1.Basic.Incidents.in.Local.Network.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/8.1.Basic.Incidents.in.Local.Network.txt",

                    "size": 177916856,

                    "description": "8 1 Basic Incidents in Local Network"

                },
                {

                    "name": "8.2.Incident.Detection.Inside.Network.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/8.2.Incident.Detection.Inside.Network.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/8.2.Incident.Detection.Inside.Network.txt",

                    "size": 375016,

                    "description": "8 2 Incident Detection Inside Network"

                },
                {

                    "name": "8.3.Incident.Detection.Beyond.Network.Perimeter.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/8.3.Incident.Detection.Beyond.Network.Perimeter.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/8.3.Incident.Detection.Beyond.Network.Perimeter.txt",

                    "size": 405307102,

                    "description": "8 3 Incident Detection Beyond Network Perimeter"

                },
                {

                    "name": "8.4.Auxiliary.Utilities.for.Network.Work.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/8.4.Auxiliary.Utilities.for.Network.Work.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/8.4.Auxiliary.Utilities.for.Network.Work.txt",

                    "size": 152243053,

                    "description": "8 4 Auxiliary Utilities for Network Work"

                },
                {

                    "name": "9.1.Attacks.on.Linux.Systems.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/9.1.Attacks.on.Linux.Systems.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/9.1.Attacks.on.Linux.Systems.txt",

                    "size": 120015734,

                    "description": "9 1 Attacks on Linux Systems"

                },
                {

                    "name": "9.2.Searching.for.Compromise.Traces.in.Linux.OS.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/9.2.Searching.for.Compromise.Traces.in.Linux.OS.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/9.2.Searching.for.Compromise.Traces.in.Linux.OS.txt",

                    "size": 275629282,

                    "description": "9 2 Searching for Compromise Traces in Linux OS"

                },
                {

                    "name": "9.3.Security.Hardening.mp4",

                    "url": "https://github.com/st93642/Assets/releases/download/3.0.0/9.3.Security.Hardening.mp4",

                    "text_url": "https://github.com/st93642/Assets/releases/download/3.0.0/9.3.Security.Hardening.txt",

                    "size": 113176997,

                    "description": "9 3 Security Hardening"

                }
        ],
        "2.0.0": [
                {

                    "name": "10.1.Services.Configuration.Files.and.Device.Manager.Linux.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/10.1.Services.Configuration.Files.and.Device.Manager.Linux.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/10.1.Services.Configuration.Files.and.Device.Manager.Linux.webm",

                    "size": 364736472,

                    "description": "10 1 Services Configuration Files and Device Manager Linux"

                },
                {

                    "name": "10.2.Loaded.Kernel.Modules.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/10.2.Loaded.Kernel.Modules.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/10.2.Loaded.Kernel.Modules.webm",

                    "size": 110308167,

                    "description": "10 2 Loaded Kernel Modules"

                },
                {

                    "name": "10.3.Upstart.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/10.3.Upstart.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/10.3.Upstart.webm",

                    "size": 25459743,

                    "description": "10 3 Upstart"

                },
                {

                    "name": "10.4.Date.and.Time.in.Linux.System.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/10.4.Date.and.Time.in.Linux.System.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/10.4.Date.and.Time.in.Linux.System.webm",

                    "size": 38179137,

                    "description": "10 4 Date and Time in Linux System"

                },
                {

                    "name": "10.5.Cron.Task.Scheduler.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/10.5.Cron.Task.Scheduler.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/10.5.Cron.Task.Scheduler.webm",

                    "size": 61689402,

                    "description": "10 5 Cron Task Scheduler"

                },
                {

                    "name": "10.6.At.Task.Scheduler.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/10.6.At.Task.Scheduler.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/10.6.At.Task.Scheduler.webm",

                    "size": 51639104,

                    "description": "10 6 At Task Scheduler"

                },
                {

                    "name": "10.7.Creating.a.Backdoor.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/10.7.Creating.a.Backdoor.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/10.7.Creating.a.Backdoor.webm",

                    "size": 92038947,

                    "description": "10 7 Creating a Backdoor"

                },
                {

                    "name": "11.1.Logging.and.Monitoring.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.1.Logging.and.Monitoring.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.1.Logging.and.Monitoring.webm",

                    "size": 156814062,

                    "description": "11 1 Logging and Monitoring"

                },
                {

                    "name": "11.10.Covering.Tracks.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.10.Covering.Tracks.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.10.Covering.Tracks.webm",

                    "size": 172222666,

                    "description": "11 10 Covering Tracks"

                },
                {

                    "name": "11.11.Threat.Hunting.and.Forensics.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.11.Threat.Hunting.and.Forensics.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.11.Threat.Hunting.and.Forensics.webm",

                    "size": 48636769,

                    "description": "11 11 Threat Hunting and Forensics"

                },
                {

                    "name": "11.2.Structure.of.etc.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.2.Structure.of.etc.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.2.Structure.of.etc.webm",

                    "size": 23666111,

                    "description": "11 2 Structure of etc"

                },
                {

                    "name": "11.3.Searching.for.Open.Files.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.3.Searching.for.Open.Files.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.3.Searching.for.Open.Files.webm",

                    "size": 96354500,

                    "description": "11 3 Searching for Open Files"

                },
                {

                    "name": "11.4.Monitoring.Access.to.Resources.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.4.Monitoring.Access.to.Resources.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.4.Monitoring.Access.to.Resources.webm",

                    "size": 230108530,

                    "description": "11 4 Monitoring Access to Resources"

                },
                {

                    "name": "11.5.Streams.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.5.Streams.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.5.Streams.webm",

                    "size": 129015600,

                    "description": "11 5 Streams"

                },
                {

                    "name": "11.6.Resource.Management.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.6.Resource.Management.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.6.Resource.Management.webm",

                    "size": 74510058,

                    "description": "11 6 Resource Management"

                },
                {

                    "name": "11.7.Systemd.Journal.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.7.Systemd.Journal.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.7.Systemd.Journal.webm",

                    "size": 124399921,

                    "description": "11 7 Systemd Journal"

                },
                {

                    "name": "11.8.Reading.rsyslogd.Log.Messages.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.8.Reading.rsyslogd.Log.Messages.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.8.Reading.rsyslogd.Log.Messages.webm",

                    "size": 247419919,

                    "description": "11 8 Reading rsyslogd Log Messages"

                },
                {

                    "name": "11.9.Collecting.Hardware.Data.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.9.Collecting.Hardware.Data.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/11.9.Collecting.Hardware.Data.webm",

                    "size": 28328326,

                    "description": "11 9 Collecting Hardware Data"

                },
                {

                    "name": "12.1.Package.Installation.Repositories.Package.Managers.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/12.1.Package.Installation.Repositories.Package.Managers.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/12.1.Package.Installation.Repositories.Package.Managers.webm",

                    "size": 118536957,

                    "description": "12 1 Package Installation Repositories Package Managers"

                },
                {

                    "name": "12.2.RPM.Package.Manager.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/12.2.RPM.Package.Manager.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/12.2.RPM.Package.Manager.webm",

                    "size": 21905085,

                    "description": "12 2 RPM Package Manager"

                },
                {

                    "name": "12.3.DEB.Package.Manager.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/12.3.DEB.Package.Manager.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/12.3.DEB.Package.Manager.webm",

                    "size": 9037544,

                    "description": "12 3 DEB Package Manager"

                },
                {

                    "name": "12.4.Compiling.Source.Code.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/12.4.Compiling.Source.Code.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/12.4.Compiling.Source.Code.webm",

                    "size": 109578170,

                    "description": "12 4 Compiling Source Code"

                },
                {

                    "name": "12.5.APT.Package.Manager.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/12.5.APT.Package.Manager.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/12.5.APT.Package.Manager.webm",

                    "size": 47515221,

                    "description": "12 5 APT Package Manager"

                },
                {

                    "name": "12.6.YUM.Package.Manager.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/12.6.YUM.Package.Manager.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/12.6.YUM.Package.Manager.webm",

                    "size": 17769065,

                    "description": "12 6 YUM Package Manager"

                },
                {

                    "name": "12.7.Utilities.for.Information.Security.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/12.7.Utilities.for.Information.Security.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/12.7.Utilities.for.Information.Security.webm",

                    "size": 31029658,

                    "description": "12 7 Utilities for Information Security"

                },
                {

                    "name": "12.8.Hacker.Utilities.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/12.8.Hacker.Utilities.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/12.8.Hacker.Utilities.webm",

                    "size": 47414525,

                    "description": "12 8 Hacker Utilities"

                },
                {

                    "name": "13.1.Security.Settings.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/13.1.Security.Settings.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/13.1.Security.Settings.webm",

                    "size": 120325341,

                    "description": "13 1 Security Settings"

                },
                {

                    "name": "13.2.Chroot.Utility.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/13.2.Chroot.Utility.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/13.2.Chroot.Utility.webm",

                    "size": 5430215,

                    "description": "13 2 Chroot Utility"

                },
                {

                    "name": "13.3.PAM.AppArmor.PolicyKit.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/13.3.PAM.AppArmor.PolicyKit.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/13.3.PAM.AppArmor.PolicyKit.webm",

                    "size": 192179263,

                    "description": "13 3 PAM AppArmor PolicyKit"

                },
                {

                    "name": "13.4.Protection.and.Assessment.of.IS.Security.Level.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/13.4.Protection.and.Assessment.of.IS.Security.Level.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/13.4.Protection.and.Assessment.of.IS.Security.Level.webm",

                    "size": 83689972,

                    "description": "13 4 Protection and Assessment of IS Security Level"

                },
                {

                    "name": "14.1.Backup.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/14.1.Backup.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/14.1.Backup.webm",

                    "size": 70367797,

                    "description": "14 1 Backup"

                },
                {

                    "name": "14.2.Automating.Backup.Task.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/14.2.Automating.Backup.Task.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/14.2.Automating.Backup.Task.webm",

                    "size": 53999420,

                    "description": "14 2 Automating Backup Task"

                },
                {

                    "name": "14.3.Data.Recovery.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/14.3.Data.Recovery.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/14.3.Data.Recovery.webm",

                    "size": 26102604,

                    "description": "14 3 Data Recovery"

                },
                {

                    "name": "14.4.Data.Recovery.with.tar.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/14.4.Data.Recovery.with.tar.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/14.4.Data.Recovery.with.tar.webm",

                    "size": 6430534,

                    "description": "14 4 Data Recovery with tar"

                },
                {

                    "name": "14.5.Information.Security.Assurance.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/14.5.Information.Security.Assurance.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/14.5.Information.Security.Assurance.webm",

                    "size": 47377271,

                    "description": "14 5 Information Security Assurance"

                },
                {

                    "name": "14.6.Organizational.Protection.of.Information.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/14.6.Organizational.Protection.of.Information.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/14.6.Organizational.Protection.of.Information.webm",

                    "size": 17603852,

                    "description": "14 6 Organizational Protection of Information"

                },
                {

                    "name": "2.1.1.Introduction.to.Information.Security.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.1.1.Introduction.to.Information.Security.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.1.1.Introduction.to.Information.Security.webm",

                    "size": 89534524,

                    "description": "2 1 1 Introduction to Information Security"

                },
                {

                    "name": "2.1.2.Information.Protection.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.1.2.Information.Protection.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.1.2.Information.Protection.webm",

                    "size": 231449362,

                    "description": "2 1 2 Information Protection"

                },
                {

                    "name": "2.1.3.Career.in.Information.Security.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.1.3.Career.in.Information.Security.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.1.3.Career.in.Information.Security.webm",

                    "size": 265315698,

                    "description": "2 1 3 Career in Information Security"

                },
                {

                    "name": "2.1.4.Course.Overview.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.1.4.Course.Overview.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.1.4.Course.Overview.webm",

                    "size": 44125051,

                    "description": "2 1 4 Course Overview"

                },
                {

                    "name": "2.2.1.Introduction.to.OS.Security.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.2.1.Introduction.to.OS.Security.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.2.1.Introduction.to.OS.Security.webm",

                    "size": 107165546,

                    "description": "2 2 1 Introduction to OS Security"

                },
                {

                    "name": "2.2.2.Linux.as.Target.System.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.2.2.Linux.as.Target.System.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.2.2.Linux.as.Target.System.webm",

                    "size": 339255138,

                    "description": "2 2 2 Linux as Target System"

                },
                {

                    "name": "2.2.3.Linux.as.Home.OS.for.Security.Specialist.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.2.3.Linux.as.Home.OS.for.Security.Specialist.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.2.3.Linux.as.Home.OS.for.Security.Specialist.webm",

                    "size": 174827042,

                    "description": "2 2 3 Linux as Home OS for Security Specialist"

                },
                {

                    "name": "2.2.4.Linux.File.System.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.2.4.Linux.File.System.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.2.4.Linux.File.System.webm",

                    "size": 85369341,

                    "description": "2 2 4 Linux File System"

                },
                {

                    "name": "2.3.1.Creating.User.Account.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.3.1.Creating.User.Account.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.3.1.Creating.User.Account.webm",

                    "size": 137823230,

                    "description": "2 3 1 Creating User Account"

                },
                {

                    "name": "2.3.2.Delegation.of.Rights.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.3.2.Delegation.of.Rights.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.3.2.Delegation.of.Rights.webm",

                    "size": 88193917,

                    "description": "2 3 2 Delegation of Rights"

                },
                {

                    "name": "2.3.3.Inheritance.of.Rights.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.3.3.Inheritance.of.Rights.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.3.3.Inheritance.of.Rights.webm",

                    "size": 162765638,

                    "description": "2 3 3 Inheritance of Rights"

                },
                {

                    "name": "2.3.4.Superuser.Rights.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.3.4.Superuser.Rights.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.3.4.Superuser.Rights.webm",

                    "size": 84635139,

                    "description": "2 3 4 Superuser Rights"

                },
                {

                    "name": "2.3.5.Malware.Characteristics.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.3.5.Malware.Characteristics.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.3.5.Malware.Characteristics.webm",

                    "size": 91863540,

                    "description": "2 3 5 Malware Characteristics"

                },
                {

                    "name": "2.3.6.Types.of.Malware.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.3.6.Types.of.Malware.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.3.6.Types.of.Malware.webm",

                    "size": 213605599,

                    "description": "2 3 6 Types of Malware"

                },
                {

                    "name": "2.4.1.Users.and.Groups.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.4.1.Users.and.Groups.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.4.1.Users.and.Groups.webm",

                    "size": 224121028,

                    "description": "2 4 1 Users and Groups"

                },
                {

                    "name": "2.4.2.Access.Rights.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.4.2.Access.Rights.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.4.2.Access.Rights.webm",

                    "size": 218213288,

                    "description": "2 4 2 Access Rights"

                },
                {

                    "name": "2.4.3.Sudo.and.Su.Commands.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.4.3.Sudo.and.Su.Commands.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.4.3.Sudo.and.Su.Commands.webm",

                    "size": 224019517,

                    "description": "2 4 3 Sudo and Su Commands"

                },
                {

                    "name": "2.4.4.MAC.and.DAC.Access.Control.Model.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.4.4.MAC.and.DAC.Access.Control.Model.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.4.4.MAC.and.DAC.Access.Control.Model.webm",

                    "size": 145163574,

                    "description": "2 4 4 MAC and DAC Access Control Model"

                },
                {

                    "name": "2.4.5.Privileges.in.Linux.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.4.5.Privileges.in.Linux.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.4.5.Privileges.in.Linux.webm",

                    "size": 46629605,

                    "description": "2 4 5 Privileges in Linux"

                },
                {

                    "name": "2.4.6.Privilege.Escalation.in.Linux.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.4.6.Privilege.Escalation.in.Linux.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.4.6.Privilege.Escalation.in.Linux.webm",

                    "size": 117780549,

                    "description": "2 4 6 Privilege Escalation in Linux"

                },
                {

                    "name": "2.6.1.IO.in.Linux.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.6.1.IO.in.Linux.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.6.1.IO.in.Linux.webm",

                    "size": 71633406,

                    "description": "2 6 1 IO in Linux"

                },
                {

                    "name": "2.6.2.File.Writing.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.6.2.File.Writing.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.6.2.File.Writing.webm",

                    "size": 86830060,

                    "description": "2 6 2 File Writing"

                },
                {

                    "name": "2.6.3.Reading.from.File.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.6.3.Reading.from.File.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.6.3.Reading.from.File.webm",

                    "size": 208137110,

                    "description": "2 6 3 Reading from File"

                },
                {

                    "name": "2.6.4.Search.and.Filtering.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.6.4.Search.and.Filtering.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.6.4.Search.and.Filtering.webm",

                    "size": 123143054,

                    "description": "2 6 4 Search and Filtering"

                },
                {

                    "name": "2.6.5.Pipeline.Processing.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.6.5.Pipeline.Processing.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.6.5.Pipeline.Processing.webm",

                    "size": 42673574,

                    "description": "2 6 5 Pipeline Processing"

                },
                {

                    "name": "2.6.6.Information.Search.and.Exfiltration.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.6.6.Information.Search.and.Exfiltration.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.6.6.Information.Search.and.Exfiltration.webm",

                    "size": 82618773,

                    "description": "2 6 6 Information Search and Exfiltration"

                },
                {

                    "name": "2.6.7.Analysis.of.Exfiltration.Attacks.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.6.7.Analysis.of.Exfiltration.Attacks.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.6.7.Analysis.of.Exfiltration.Attacks.webm",

                    "size": 97684576,

                    "description": "2 6 7 Analysis of Exfiltration Attacks"

                },
                {

                    "name": "2.6.8.Lateral.Movement.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.6.8.Lateral.Movement.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.6.8.Lateral.Movement.webm",

                    "size": 53078095,

                    "description": "2 6 8 Lateral Movement"

                },
                {

                    "name": "2.7.1.Linux.Kernel.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.7.1.Linux.Kernel.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.7.1.Linux.Kernel.webm",

                    "size": 91360161,

                    "description": "2 7 1 Linux Kernel"

                },
                {

                    "name": "2.7.2.Linux.Kernel.Initialization.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.7.2.Linux.Kernel.Initialization.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.7.2.Linux.Kernel.Initialization.webm",

                    "size": 95719867,

                    "description": "2 7 2 Linux Kernel Initialization"

                },
                {

                    "name": "2.7.3.Linux.Kernel.Parameters.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.7.3.Linux.Kernel.Parameters.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.7.3.Linux.Kernel.Parameters.webm",

                    "size": 112825006,

                    "description": "2 7 3 Linux Kernel Parameters"

                },
                {

                    "name": "2.7.4.Bootloader.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.7.4.Bootloader.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.7.4.Bootloader.webm",

                    "size": 82068012,

                    "description": "2 7 4 Bootloader"

                },
                {

                    "name": "2.7.5.GRUB.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.7.5.GRUB.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.7.5.GRUB.webm",

                    "size": 113981159,

                    "description": "2 7 5 GRUB"

                },
                {

                    "name": "2.7.6.MBR.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.7.6.MBR.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.7.6.MBR.webm",

                    "size": 68100203,

                    "description": "2 7 6 MBR"

                },
                {

                    "name": "2.7.7.UEFI.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.7.7.UEFI.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.7.7.UEFI.webm",

                    "size": 18262735,

                    "description": "2 7 7 UEFI"

                },
                {

                    "name": "2.7.8.Kernel.and.Modules.Security.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.7.8.Kernel.and.Modules.Security.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.7.8.Kernel.and.Modules.Security.webm",

                    "size": 98549127,

                    "description": "2 7 8 Kernel and Modules Security"

                },
                {

                    "name": "2.7.9.Shellcodes.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.7.9.Shellcodes.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/2.0.0/2.7.9.Shellcodes.webm",

                    "size": 49036582,

                    "description": "2 7 9 Shellcodes"

                }
        ],
        "1.0.0": [
                {

                    "name": "1.Area.of.use.Linux.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/1.Area.of.use.Linux.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/1.Area.of.use.Linux.webm",

                    "size": 91516994,

                    "description": "1 Area of use Linux"

                },
                {

                    "name": "10.User.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/10.User.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/10.User.webm",

                    "size": 73548284,

                    "description": "10 User"

                },
                {

                    "name": "11.User.space.kernel.space.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/11.User.space.kernel.space.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/11.User.space.kernel.space.webm",

                    "size": 53361495,

                    "description": "11 User space kernel space"

                },
                {

                    "name": "12.File.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/12.File.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/12.File.webm",

                    "size": 96959529,

                    "description": "12 File"

                },
                {

                    "name": "13.File.system.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/13.File.system.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/13.File.system.webm",

                    "size": 149388450,

                    "description": "13 File system"

                },
                {

                    "name": "14.Packet.manager.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/14.Packet.manager.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/14.Packet.manager.webm",

                    "size": 101724737,

                    "description": "14 Packet manager"

                },
                {

                    "name": "15.Kernel.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/15.Kernel.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/15.Kernel.webm",

                    "size": 227804356,

                    "description": "15 Kernel"

                },
                {

                    "name": "16.Memory.swapping.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/16.Memory.swapping.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/16.Memory.swapping.webm",

                    "size": 76399203,

                    "description": "16 Memory swapping"

                },
                {

                    "name": "17.Process.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/17.Process.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/17.Process.webm",

                    "size": 147783469,

                    "description": "17 Process"

                },
                {

                    "name": "18.Socket.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/18.Socket.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/18.Socket.webm",

                    "size": 42342699,

                    "description": "18 Socket"

                },
                {

                    "name": "2.Intro.to.setup.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/2.Intro.to.setup.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/2.Intro.to.setup.webm",

                    "size": 38927283,

                    "description": "2 Intro to setup"

                },
                {

                    "name": "3.Types.of.setup.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/3.Types.of.setup.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/3.Types.of.setup.webm",

                    "size": 122777455,

                    "description": "3 Types of setup"

                },
                {

                    "name": "4.1.What.is.Terminal.Console.and.Command.Shell.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/4.1.What.is.Terminal.Console.and.Command.Shell.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/4.1.What.is.Terminal.Console.and.Command.Shell.webm",

                    "size": 59412547,

                    "description": "4 1 What is Terminal Console and Command Shell"

                },
                {

                    "name": "4.2.Overview.of.Command.Shells.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/4.2.Overview.of.Command.Shells.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/4.2.Overview.of.Command.Shells.webm",

                    "size": 129996776,

                    "description": "4 2 Overview of Command Shells"

                },
                {

                    "name": "4.3.Basic.Navigation.in.File.System.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/4.3.Basic.Navigation.in.File.System.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/4.3.Basic.Navigation.in.File.System.webm",

                    "size": 237230489,

                    "description": "4 3 Basic Navigation in File System"

                },
                {

                    "name": "4.4.Input.Output.Redirection.Error.Format.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/4.4.Input.Output.Redirection.Error.Format.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/4.4.Input.Output.Redirection.Error.Format.webm",

                    "size": 88938371,

                    "description": "4 4 Input Output Redirection Error Format"

                },
                {

                    "name": "4.5.Basic.File.Operations.Commands.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/4.5.Basic.File.Operations.Commands.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/4.5.Basic.File.Operations.Commands.webm",

                    "size": 138062480,

                    "description": "4 5 Basic File Operations Commands"

                },
                {

                    "name": "4.6.Search.and.Filtering.Pipelines.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/4.6.Search.and.Filtering.Pipelines.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/4.6.Search.and.Filtering.Pipelines.webm",

                    "size": 161474222,

                    "description": "4 6 Search and Filtering Pipelines"

                },
                {

                    "name": "4.File.system.and.directories.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/4.File.system.and.directories.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/4.File.system.and.directories.webm",

                    "size": 62666303,

                    "description": "4 File system and directories"

                },
                {

                    "name": "5.1.Device.Names.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/5.1.Device.Names.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/5.1.Device.Names.webm",

                    "size": 135091893,

                    "description": "5 1 Device Names"

                },
                {

                    "name": "5.2.Device.Files.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/5.2.Device.Files.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/5.2.Device.Files.webm",

                    "size": 29463979,

                    "description": "5 2 Device Files"

                },
                {

                    "name": "5.Disk.encryption.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/5.Disk.encryption.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/5.Disk.encryption.webm",

                    "size": 49281546,

                    "description": "5 Disk encryption"

                },
                {

                    "name": "6.1.Disks.and.Partitions.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/6.1.Disks.and.Partitions.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/6.1.Disks.and.Partitions.webm",

                    "size": 140929512,

                    "description": "6 1 Disks and Partitions"

                },
                {

                    "name": "6.2.Working.with.Partition.Table.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/6.2.Working.with.Partition.Table.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/6.2.Working.with.Partition.Table.webm",

                    "size": 101257720,

                    "description": "6 2 Working with Partition Table"

                },
                {

                    "name": "6.3.Working.with.Disk.Creating.Partition.and.Formatting.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/6.3.Working.with.Disk.Creating.Partition.and.Formatting.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/6.3.Working.with.Disk.Creating.Partition.and.Formatting.webm",

                    "size": 245726468,

                    "description": "6 3 Working with Disk Creating Partition and Formatting"

                },
                {

                    "name": "6.4.Disk.Checking.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/6.4.Disk.Checking.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/6.4.Disk.Checking.webm",

                    "size": 153395557,

                    "description": "6 4 Disk Checking"

                },
                {

                    "name": "6.Boot.loader.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/6.Boot.loader.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/6.Boot.loader.webm",

                    "size": 32199343,

                    "description": "6 Boot loader"

                },
                {

                    "name": "7.1.Introduction.to.File.Systems.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/7.1.Introduction.to.File.Systems.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/7.1.Introduction.to.File.Systems.webm",

                    "size": 194260383,

                    "description": "7 1 Introduction to File Systems"

                },
                {

                    "name": "7.2.Inodes.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/7.2.Inodes.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/7.2.Inodes.webm",

                    "size": 169472273,

                    "description": "7 2 Inodes"

                },
                {

                    "name": "7.3.File.System.and.File.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/7.3.File.System.and.File.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/7.3.File.System.and.File.webm",

                    "size": 144229955,

                    "description": "7 3 File System and File"

                },
                {

                    "name": "7.4.Recovering.Deleted.Files.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/7.4.Recovering.Deleted.Files.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/7.4.Recovering.Deleted.Files.webm",

                    "size": 212138548,

                    "description": "7 4 Recovering Deleted Files"

                },
                {

                    "name": "7.Emergency.boot.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/7.Emergency.boot.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/7.Emergency.boot.webm",

                    "size": 39600040,

                    "description": "7 Emergency boot"

                },
                {

                    "name": "8.Install.process.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/8.Install.process.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/8.Install.process.webm",

                    "size": 129573097,

                    "description": "8 Install process"

                },
                {

                    "name": "9.Linux.structure.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/9.Linux.structure.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/9.Linux.structure.webm",

                    "size": 27590865,

                    "description": "9 Linux structure"

                },
                {

                    "name": "Intro.to.Linux.webm",

                    "url": "https://github.com/st93642/Assets/releases/download/1.0.0/Intro.to.Linux.webm",

                    "text_url": "https://github.com/st93642/Assets/releases/download/1.0.0/Intro.to.Linux.webm",

                    "size": 64723536,

                    "description": "Intro to Linux"

                }
        ]
}

    @classmethod
    def get_all_videos(cls) -> List[Dict[str, Any]]:
        """Get all videos from all releases."""
        all_videos = []
        for release_videos in cls.VIDEOS.values():
            all_videos.extend(release_videos)
        return all_videos

    @classmethod
    def get_videos_by_release(cls, release_tag: str) -> List[Dict[str, Any]]:
        """Get videos for a specific release."""
        return cls.VIDEOS.get(release_tag, [])

    @classmethod
    def get_release_tags(cls) -> List[str]:
        """Get all available release tags."""
        return list(cls.VIDEOS.keys())

    @classmethod
    def get_tree_structure(cls) -> Dict[str, List[str]]:
        """Get tree structure of releases and their video names."""
        return {tag: [video["name"] for video in videos] for tag, videos in cls.VIDEOS.items()}
