# FirstIssue-MCP
MCP server implementation for FirstIssue project

Checkout FirstIssue here: [FirstIssue](https://firstissue.web.app/)

Checkout The Video about it here: [Youtube](https://youtu.be/C5M5xq9S8Tw)

# Features
1. summarize_issues:
Finds n number of issues from a given repository and summarizes it. "N" is defaulted to 5 if nothing is provided
Example: 
[get_issues](./assets/get_issues.png)

2. get_single_issue
Summarizes a single issue from a github repository
Example:
[single_issue](./assets/single_issue.png)

# Pre-Requisite
1. Claude Desktop
2. Python Version >=3.11
3. Github Personal Access Token: [Get One Here](https://github.com/settings/personal-access-tokens)

Select one of the following:

&nbsp;&nbsp; a. Public repositories

&nbsp;&nbsp; b. All repositories

# Setup
1. Clone this repository:
```git
git clone https://github.com/srivats22/firstissue-mcp.git
```
2. Open the project in an editor of choice
3. Either in the editors terminal or system terminal run the below command in the project directory
```git
uv sync
```
4. Open the following location:
```
MacOS/Linux: ~/Library/Application Support/Claude/claude_desktop_config.json
Windows: %APPDATA%\Claude\claude_desktop_config.json
```
5. Paste the below
```json
 "firstissue": {
    "command": "uv",
    "args": [
        "--directory",
        "<parent-path>/firstissue-mcp",
        "run",
        "firstissue.py"
    ],
    "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "Replace with Personal Access Token"
    }
}
```
6. Should look something like below:
```json
{
  "mcpServers": {
    "firstissue": {
      "command": "uv",
      "args": [
        "--directory",
        "<parentfolder>/firstissue-mcp",
        "run",
        "firstissue.py"
      ],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "token"
      }
    }
  }
}
```