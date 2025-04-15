all_issues_query = """
    query IssuesWithLabels($owner: String!, $repo: String!, $issue_cnt: Int!) {
        repository(owner: $owner, name: $repo) {
            issues(first: $issue_cnt, states: [OPEN], orderBy: { field: CREATED_AT, direction: DESC }) {
                nodes {
                    title
                    number
                    bodyText
                    url
                    labels(first: 1) {
                        nodes {
                            name
                        }
                    }
                }
            }
        }
    }
"""

single_issue_query = """
    query GetIssue($owner: String!, $repo: String!, $issueNumber: Int!) {
        repository(owner: $owner, name: $repo) {
            issue(number: $issueNumber) {
                title
                body
                url
            }
        }
    }
"""