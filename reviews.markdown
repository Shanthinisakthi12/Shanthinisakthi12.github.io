---
layout: page
title: Paper Reviews
permalink: /reviews/
---

## 📑 Research Paper Reviews

This page automatically lists all my paper review posts along with key highlights.

---

{% assign review_posts = site.categories.reviews | sort: 'date' | reverse %}

{% for post in review_posts %}
### [{{ post.title }}]({{ post.url }})
- **Date:** {{ post.date | date: "%B %-d, %Y" }}
- **Tags:** {% for tag in post.tags %}{{ tag }}{% unless forloop.last %}, {% endunless %}{% endfor %}
- **Excerpt:** {{ post.excerpt | strip_html | truncatewords: 30 }}

{% if post.intuition %}
{% include callout.html type="info" title="Intuition Box" content=post.intuition %}
{% endif %}

{% if post.challenge %}
{% include callout.html type="warning" title="Challenge Corner" content=post.challenge %}
{% endif %}

---
{% endfor %}