import os

import requests


def post_to_medium(title: str, content: str, canonical_url: str, public: bool = False):

    response = requests.post(
        f"https://api.medium.com/v1/users/{os.environ.get('MEDIUM_ID')}/posts",
        headers={"Authorization": f"Bearer {os.environ.get('MEDIUM_TOKEN')}"},
        data={
            "title": title,
            "contentFormat": "markdown",
            "content": content,
            "canonicalUrl": canonical_url,
            "publishStatus": "public" if public else "draft",
        },
    )

    try:
        response.raise_for_status()
    except Exception as e:
        print(response.json())
        print(e)


def post_from_markdown_file(
    path: str, title: str, canonical_url: str, public: bool = False
):
    with open(path, "r") as markdown_file:
        return post_to_medium(title, markdown_file.read(), canonical_url, public)
