---
layout: default
title: Publications
---
<a href="{{ site.baseurl }}/" class="back-link"><i class="fa-solid fa-arrow-left"></i> Back to Main Page</a>

<section id="journals">
    <h3 class="section-title">Journal Articles</h3>
    {% for pub in site.data.publications.journals %}
    <div class="pub-item">
        <div class="pub-year">{{ pub.year }}</div>
        <div class="pub-title">
            <a href="{{ pub.url | default: '#' }}" target="_blank" rel="noopener noreferrer">{{ pub.title }}</a>
        </div>
        <div class="pub-authors">{{ pub.authors }}</div>
        <div class="pub-journal">{{ pub.journal }}</div>
        {% if pub.abstract and pub.abstract != "No abstract available." %}
        <details class="pub-abstract" style="margin-top: 10px;">
            <summary style="cursor: pointer; font-weight: 600; color: var(--accent);">Abstract</summary>
            <p style="margin-top: 10px; border-left: 2px solid var(--card-hover); padding-left: 15px; font-size: 0.9rem;">{{ pub.abstract }}</p>
        </details>
        {% endif %}
    </div>
    {% endfor %}
</section>

<section id="conferences">
    <h3 class="section-title">Conference Proceedings</h3>
    {% for pub in site.data.publications.conferences %}
    <div class="pub-item">
        <div class="pub-year">{{ pub.year }}</div>
        <div class="pub-title">
            <a href="{{ pub.url | default: '#' }}" target="_blank" rel="noopener noreferrer">{{ pub.title }}</a>
        </div>
        <div class="pub-authors">{{ pub.authors }}</div>
        <div class="pub-journal">{{ pub.journal }}</div>
        {% if pub.abstract and pub.abstract != "No abstract available." %}
        <details class="pub-abstract" style="margin-top: 10px;">
            <summary style="cursor: pointer; font-weight: 600; color: var(--accent);">Abstract</summary>
            <p style="margin-top: 10px; border-left: 2px solid var(--card-hover); padding-left: 15px; font-size: 0.9rem;">{{ pub.abstract }}</p>
        </details>
        {% endif %}
    </div>
    {% endfor %}
</section>
