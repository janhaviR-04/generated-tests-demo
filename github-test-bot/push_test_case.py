from github import Github

# Replace with your GitHub token
GITHUB_TOKEN = "your_github_token_here"

# Repo details
REPO_NAME = "janhaviR-04/generated-tests-demo"
FILE_PATH = "tests/generated.test.js"
COMMIT_MESSAGE = "Add generated test case"
BRANCH = "main"  # or your working branch

test_case_code = """\
describe('test2', () => {
  it('should work', () => {
    expect(true).toBe(true);
  });
});
"""

# Authenticate with GitHub
g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

# Check if file exists and update or create
try:
    contents = repo.get_contents(FILE_PATH, ref=BRANCH)
    repo.update_file(
        path=FILE_PATH,
        message=COMMIT_MESSAGE,
        content=test_case_code,
        sha=contents.sha,
        branch=BRANCH
    )
    print("✅ File updated successfully.")
except:
    repo.create_file(
        path=FILE_PATH,
        message=COMMIT_MESSAGE,
        content=test_case_code,
        branch=BRANCH
    )
    print("✅ File created and pushed successfully.")
