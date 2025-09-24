---
layout: page
title: Categories
permalink: /categories/
---

## 📂 Browse by Category

{% for category in site.categories %}
### {{ category[0] | capitalize }}

<ul>
  {% assign posts = category[1] %}
  {% for post in posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      ({{ post.date | date: "%B %-d, %Y" }})
    </li>
  {% endfor %}
</ul>

{% endfor %}
