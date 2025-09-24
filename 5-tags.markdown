---
layout: page
title: Tags
permalink: /tags/
---

## Browse by Tag

{% for tag in site.tags %}
### {{ tag[0] | capitalize }}

<ul>
  {% assign posts = tag[1] %}
  {% for post in posts %}
    <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> ({{ post.date | date: "%B %-d, %Y" }})</li>
  {% endfor %}
</ul>

{% endfor %}
