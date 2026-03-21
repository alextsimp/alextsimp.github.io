---
layout: default
title: Publications
---
<a href="{{ site.baseurl }}/" class="back-link"><i class="fa-solid fa-arrow-left"></i> Back to Main Portfolio</a>

<section id="journals">
    <h3 class="section-title">Journal Articles</h3>
    {% for pub in site.data.publications.journals %}
    <div class="pub-item">
        <div class="pub-year">{{ pub.year }}</div>
        <div class="pub-title">{{ pub.title }}</div>
        <div class="pub-authors">{{ pub.authors }}</div>
        <div class="pub-journal">{{ pub.journal }}</div>
    </div>
    {% endfor %}
</section>

<section id="conferences">
    <h3 class="section-title">Conference Proceedings</h3>
    {% for pub in site.data.publications.conferences %}
    <div class="pub-item">
        <div class="pub-year">{{ pub.year }}</div>
        <div class="pub-title">{{ pub.title }}</div>
        <div class="pub-authors">{{ pub.authors }}</div>
        <div class="pub-journal">{{ pub.journal }}</div>
    </div>
    {% endfor %}
</section>
