import mcp.types as types

class PromptTemplate:

    def __init__(self, mcp_app):
        self.mcp_app = mcp_app

        PROMPTS = {
            "summarize_issues": types.Prompt(
                name="summarize_issues",
                description="""
                Gets a list of open issues from a github repository
                and summarizes the issues so you can easily find which ones to work on.
                """,
                arguments=[
                    types.PromptArgument(
                        name="repo_url",
                        description="""
                        The URL of the github repository.\n
                        Ex: https://github.com/flutter/flutter
                        """,
                        required=True
                    ),
                    types.PromptArgument(
                        name="issue_count",
                        description="""
                        Number of issues to look at.\n
                        Defaults to 5
                        """,
                        required=False,
                    )
                ],
            ),
        }

        @mcp_app.list_prompts()
        async def list_prompts() -> list[types.Prompt]:
            return list(PROMPTS.values())
        
        @mcp_app.get_prompt()
        async def get_prompt(
            name: str, arguments: dict[str, str] | None = None
        ) -> types.GetPromptResult:
            if name not in PROMPTS:
                raise ValueError(f"Prompt not found: {name}")

            if name == "summarize_issues":
                repo_url = arguments.get("repo_url") if arguments else ""
                issue_count = arguments.get("issue_count") if arguments else 5
                return types.GetPromptResult(
                    messages=[
                        types.PromptMessage(
                            role="user",
                            content=types.TextContent(
                                type="text",
                                text=f"Get {issue_count} issues from {repo_url}  for the user"
                            )
                        )
                    ]
                )

            raise ValueError("Prompt implementation not found")


