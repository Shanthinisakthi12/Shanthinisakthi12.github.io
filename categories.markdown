---
layout: page
title: Categories
permalink: /categories/
---

## Browse by Category

{% for category in site.categories %}
- [{{ category[0] | capitalize }}](/categories/{{ category[0] }}/) ({{ category[1].size }})
{% endfor %}