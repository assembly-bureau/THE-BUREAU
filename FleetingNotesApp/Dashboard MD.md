---
# Mandatory fields
id: "1491de90-b3ad-4b94-9938-a38c0e2dd522"
# Optional fields
title: "Dashboard MD"
tags: []
source: ""
source_title: ""
source_description: ""
source_image_url: ""
created_date: "2024-02-18"
modified_date: "2024-02-18"
---
---
cssclass: multi-column
cssclass: dashboard
---

<div class="button-row">
  <button class="button-50" role="button" onclick="window.location.href='obsidian://open?vault=YourVaultName&file=Page1'">Page 1</button>
  <button class="button-50" role="button" onclick="window.location.href='obsidian://open?vault=YourVaultName&file=Page2'">Page 2</button>
  <!-- ... Add more buttons for each page ... -->
  <button class="button-50" role="button" onclick="window.location.href='obsidian://open?vault=YourVaultName&file=Page10'">Page 10</button>
</div>
<div class="button-row">
  <button class="button-50" role="button" onclick="window.location.href='obsidian://open?vault=YourVaultName&file=Page11'">Page 11</button>
  <button class="button-50" role="button" onclick="window.location.href='obsidian://open?vault=YourVaultName&file=Page12'">Page 12</button>
  <!-- ... Add more buttons for each page ... -->
  <button class="button-50" role="button" onclick="window.location.href='obsidian://open?vault=YourVaultName&file=Page20'">Page 20</button>
</div>

## My Book Writing Dashboard

<div class="multi-column">
  <!-- Column 1 -->
  <div>
    <div class="callout-green">
      <div class="callout-green-header">Idea Backlog</div>
      <div class="callout-green-content">
        ```dataview
        TABLE status, due by "Book Ideas"
        WHERE status = "Backlog"
        SORT due ASC
        ```
      </div>
    </div>
    <div class="callout-green">
      <div class="callout-green-header">Research</div>
      <div class="callout-green-content">
        ```dataview
        TABLE status, due by "Book Research"
        WHERE status = "In Progress"
        SORT due ASC
        ```
      </div>
    </div>
  </div>

  <!-- Column 2 -->
  <div>
    <div class="callout-green">
      <div class="callout-green-header">Chapters Drafting</div>
      <div class="callout-green-content">
        ```dataview
        TABLE file.name AS Chapter, status, due by "Chapters"
        WHERE status = "Drafting"
        SORT due ASC
        ```
      </div>
    </div>
    <div class="callout-green">
      <div class="callout-green-header">Chapters Review</div>
      <div class="callout-green-content">
        ```dataview
        TABLE status, due by "Chapters"
        WHERE status = "Review"
        SORT due ASC
        ```
      </div>
    </div>
  </div>

  <!-- Column 3 -->
  <div>
    <div class="callout-green">
      <div class="callout-green-header">Final Edits</div>
      <div class="callout-green-content">
        ```dataview
        TABLE status, due by "Chapters"
        WHERE status = "Final Edits"
        SORT due ASC
        ```
      </div>
    </div>
    <div class="callout-green">
      <div class="callout-green-header">Ready to Publish</div>
      <div class="callout-green-content">
        ```dataview
        TABLE status, due by "Chapters"
        WHERE status = "Ready"
        SORT due ASC
        ```
      </div>
    </div>
  </div>
</div>