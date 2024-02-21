---
# Mandatory fields
id: "0f5ca0d1-7ecb-467b-b86c-30abb613946c"
# Optional fields
title: "00 Master Powescript"
tags: []
source: ""
source_title: ""
source_description: ""
source_image_url: ""
created_date: "2024-02-18"
modified_date: "2024-02-18"
---
# Define the root path for the Obsidian Vault
$rootPath = "C:\Path\To\Your\ObsidianVault"
$bookProjectPath = Join-Path -Path $rootPath -ChildPath "Book Projects\BOOK ONE - LIFE PLANNING"

# Define chapters
$chapters = @(
    "1.1 Discover Your Archetype - A Gateway to Personalized Planning",
    "1.2 Additional Personality Assessments - Broadening Your Self-Understanding",
    "1.3 The Journey Begins",
    "1.4 Life - A Continuous Project in Motion",
    "1.5 The Art of Time Management",
    "1.6 Personal Values Clarification",
    "1.7 Building Social and Community Engagement",
    "1.8 Embracing Creativity and Innovation",
    "1.9 Real-Life Strategy Examples",
    "1.10 Future Forecasting and Scenario Planning",
    "1.11 Health and Wellness - A Holistic Approach",
    "1.12 Career Planning and Development",
    "1.13 Digital Life Management",
    "1.14 Environmental Awareness and Sustainability",
    "1.15 Crisis Management and Resilience",
    "1.16 Mindfulness and Self-Care",
    "1.17 Cultural and Social Dynamics",
    "1.18 The Power of Habit",
    "1.19 The Art of Feedback - Personal Growth Guide",
    "1.20 Leaving a Legacy",
    "1.21 Living Your Plan - Taking Action",
    "1.22 Continual Growth and Lifelong Learning",
    "1.23 Crafting Your One-Pager Life Strategy Plan",
    "1.24 Advanced Exercises for Each",
    "1.25 Supplementary Online Resources"
)

# Define content files for each chapter with prefix
$contentFiles = @("01 Outline", "02 Introduction", "03 Main Content", "04 Worksheets", "05 Conclusion", "06 WIKI")

# Current date for created and last_modified fields
$currentDate = Get-Date -Format "yyyy-MM-dd"

# Helper function to create chapter directories and files with front matter
function New-ChapterFiles {
    param (
        [string]$chapterPath,
        [string]$chapterTitle,
        [int]$chapterIndex,
        [string[]]$files
    )

    foreach ($fileIndex in 0..($files.Length-1)) {
        $fileTitle = $files[$fileIndex].Split(' ')[1]
        $fileName = "{0}.{1:D2} {2}.md" -f $chapterIndex, ($fileIndex + 1), $fileTitle
        $filePath = Join-Path -Path $chapterPath -ChildPath $fileName
        $content = @"
---
title: '$fileTitle'
chapter: '$chapterTitle'
tags: []
status: Drafting
priority: Medium
author: Author Name
contributors: ['Contributor1', 'Contributor2']
created: '$currentDate'
last_modified: '$currentDate'
deadline: '$currentDate'
summary: 'Brief summary or abstract of the page content'
keywords:
  - Keyword1
  - Keyword2
  - Keyword3
references:
  - Reference1
  - Reference2
related: ['Related Page Title 1', 'Related Page Title 2']
workflow_steps:
  - Step1
  - Step2
current_step: Step1
next_step_due: '$currentDate'
review_round: 1
notes: 'Any additional notes or comments'
---
"@
        New-Item -ItemType File -Path $filePath -Force
        Set-Content -Path $filePath -Value $content
    }
}

# Create book project directory
New-Item -ItemType Directory -Path $bookProjectPath -Force | Out-Null

# Create chapters and their content files
foreach ($chapter in $chapters) {
    $chapterIndex = $chapter.Split(' ')[0]
    $chapterName = $chapter -replace "^\d+\.\d+\s", ""
    $chapterPath = Join-Path -Path $bookProjectPath -ChildPath $chapter
    New-Item -ItemType Directory -Path $chapterPath -Force | Out-Null
    New-ChapterFiles -chapterPath $chapterPath -chapterTitle $chapterName -chapterIndex $chapterIndex -files $contentFiles
}

Write-Host "Obsidian Vault structure with chapters and content files has been created."