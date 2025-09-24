import os

# Path to your tags folder (will be created if it doesn't exist)
tags_dir = "tags"
os.makedirs(tags_dir, exist_ok=True)

# List all your tags
tags = ["algorithms", "paper-review", "jekyll", "update"]  # Add all your tags here

# Template for each tag page
template = """---
layout: page
title: "Tag: {tag_title}"
permalink: /tags/{tag_url}/
tag: {tag_url}
---

## Posts with tag: **{tag_title}**

<ul>
{{% assign posts_with_tag = site.tags[page.tag] %}}
{{% for post in posts_with_tag %}}
  <li>
    <a href="{{{{ post.url | relative_url }}}}">{{{{ post.title }}}}</a>
    ({{{{ post.date | date: "%B %-d, %Y" }}}})
  </li>
{{% endfor %}}
</ul>
"""

# Generate a file per tag
for tag in tags:
    filename = os.path.join(tags_dir, f"{tag}.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(template.format(tag_title=tag.capitalize(), tag_url=tag))

print(f"Created {len(tags)} tag pages in '{tags_dir}/'")
