from mcp.server.fastmcp import FastMCP
import mcp.types as types
from pydantic import Field
from util.gh_connector import GhConnector

# Initialize FastMCP server
mcp = FastMCP("firstissue")

@mcp.tool(
        name= "summarize_issues",
        description="""
        Gets a list of open issues for a github repo
        Args:
            repo_url The URL of the github Repo
            issue_count Number of issues to look at
        """
)
async def summarize_issues(
    repo_url: str = Field(description="The URL of the github repository", default=""),
    issue_count: int = Field(description="Number of issues to look at", default=5)
) -> str:
    """
        Connects to Githubs GraphQL api to get a list of open issues for a repository
        Args:
            repo_url: The URL of the github repository
            issue_count: Number of issues to look at
        return:
            formated string with Title, Url and Body of the issue
    """
    url_parts = repo_url.split("/")
    owner = url_parts[-2]
    repo = url_parts[-1]
    connecter = GhConnector()
    issues = connecter.get_all_issues(owner, repo, issue_count)
    return issues

@mcp.tool(
    name="get_single_issue",
    description="""
    Get a single issue to look at
    Args:
        repo_url: The URL of the github repository
        issue_num: Github Issue Number to look at from the repo
    """
)
async def get_single_issue(
    repo_url: str = Field(description="The URL of the github repository", default=""),
    issue_num: int = Field(description="Number of the issue to look at", default=None)
) -> str:
    """
        Connects to Githubs GraphQL api to get a list of open issues for a repository
        Args:
            repo_url: The URL of the github repository
            issue_count: Number of issues to look at
        return:
            formated string with Title, Url and Body of the issue
    """
    url_parts = repo_url.split("/")
    owner = url_parts[-2]
    repo = url_parts[-1]
    connecter = GhConnector()
    issue = connecter.get_single_issue(owner, repo, issue_num)
    return issue

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')