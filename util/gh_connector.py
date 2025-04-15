import json
import requests
import os
from pydantic import Field

from util.constants import all_issues_query, single_issue_query

class GhConnector:
    def __init__(self):
        self.gh_base_url = "https://api.github.com/graphql"
        self.gh_api_key = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")

    def req_helper(self, payload):
        headers = {
            "Authorization": f"Bearer {self.gh_api_key}",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github.v4.idl"
        }

        try:
            response = requests.post(self.gh_base_url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()

            raw_issues = data.get("data", {}).get("repository", {}).get("issues", {}).get("nodes", [])
            formatted_issues = []

            for issue in raw_issues:
                issue_dets = f"""
                    Title: {issue['title']}
                    URL: {issue['url']}
                    Body: {issue.get('bodyText', 'No body provided')}
                """
                formatted_issues.append(issue_dets)
                    

            return "\n---\n".join(formatted_issues)

        except requests.exceptions.RequestException as e:
            return f"An error occurred: {e}"
        except json.JSONDecodeError:
            return "Failed to decode the JSON response."


    def get_all_issues(
            self, 
            owner: str = Field(description="The Owner of the github repository", default=""),
            repo: str = Field(description="The Repository to look at", default=""), 
            issue_count: int = Field(description="Number of issues to look at", default=5),
        ) -> str:
        variables = {
            "owner": owner,
            "repo": repo,
            "issue_cnt": issue_count
        }

        json_payload = {
            "query": all_issues_query,
            "variables": variables
        }

        if not self.gh_api_key:
            return "Personal Access Token Not Passed"

        headers = {
            "Authorization": f"Bearer {self.gh_api_key}",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github.v4.idl"
        }

        try:
            response = requests.post(self.gh_base_url, headers=headers, json=json_payload)
            response.raise_for_status()
            data = response.json()

            raw_issues = data.get("data", {}).get("repository", {}).get("issues", {}).get("nodes", [])
            formatted_issues = []

            for issue in raw_issues:
                issue_dets = f"""
                    Title: {issue['title']}
                    URL: {issue['url']}
                    Body: {issue.get('bodyText', 'No body provided')}
                """
                formatted_issues.append(issue_dets)
                    

            return "\n---\n".join(formatted_issues)

        except requests.exceptions.RequestException as e:
            return f"An error occurred: {e}"
        except json.JSONDecodeError:
            return "Failed to decode the JSON response."
    
    def get_single_issue(
        self,
        owner: str = Field(description="The Owner of the github repository", default=""),
        repo: str = Field(description="The Repository to look at", default=""), 
        issue_num: str = Field(description="Number of the issue to look at", default=None)
    ) -> str:
        variables = {
            "owner": owner,
            "repo": repo,
            "issueNumber": issue_num
        }

        json_payload = {
            "query": single_issue_query,
            "variables": variables
        }

        if not self.gh_api_key:
            return "Personal Access Token Not Passed"

        headers = {
            "Authorization": f"Bearer {self.gh_api_key}",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github.v4.idl"
        }

        try:
            response = requests.post(self.gh_base_url, headers=headers, json=json_payload)
            response.raise_for_status()
            data = response.json()

            issue = data.get("data", {}).get("repository", {}).get("issue")
            if issue:
                issue_dets = f"""
                    Title: {issue['title']}
                    Body: {issue['body']}
                    URL: {issue['url']}
                """
                return issue_dets
            else:
                return "Issue not found"

        except requests.exceptions.RequestException as e:
            return f"An error occurred: {e}"
        except json.JSONDecodeError:
            return "Failed to decode the JSON response."
    