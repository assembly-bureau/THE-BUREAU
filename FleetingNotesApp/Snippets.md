---
# Mandatory fields
id: "0c2fa756-5416-4114-8504-7689045b1372"
# Optional fields
title: "Snippets"
tags: ["c2dfe3", "9db8bf"]
source: ""
source_title: ""
source_description: ""
source_image_url: ""
created_date: "2024-02-20"
modified_date: "2024-02-20"
---



PRAKASH JOSHI PAXOBSIDIAN
27 Awesome CSS Snippets For Customizing Obsidian
Customize Obsidian to the need of your heart

CSS snippets are powerful tools to add a custom style to your Obsidian vault. They can be used to redefine various parts of the user interface such as size, position and color of different UI elements. 

With CSS, you can create a personalized look and feel in Obsidian that is more aligned with your personality and work style. CSS can also help you to enhance productivity and improve the overall user experience. 

By adding different styles and customizations, you can create a workspace that is not only functional but also visually appealing. 

This can make the note-taking process more enjoyable and fulfilling. 

This article is a compilation of useful CSS snippets collected from Reddit, Obsidian Forum, & Obsidian Discord. The credit for the CSS goes to the respective creators. I’ve added a link to the original source wherever possible. 

How to Add CSS Snippets to Your Vault

Before we dive deep into the CSS snippets, here’s how you can add these inside your vault. 

Here’s how you can add all of the CSS snippets in this article to your vault:

Open settings
Go to Appearance> CSS snippets> Open Snippets Folder
Download the CSS Snippets or create them inside this folder. 
Get back to Obsidian
Reload snippets
Toggle on the Snippets
I’ve created Obsidian Vault with all the CSS snippets mentioned in this article. If you don’t want to go to every single link, you can get all of them directly on Gumroad or Buy Me a Coffee.

Background for Kanban Board

This custom CSS adds a custom background. You can change the wallpaper by changing the URL in the CSS.

view-content .kanban-plugin::after {
  content: "";
  position: fixed;
  background-image: url(https://images.unsplash.com/photo-1513735718075-2e2d37cb7cc1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8bGlnaHRob3VzZXxlbnwwfHwwfHw%3D&w=1000&q=80);
  background-repeat: no-repeat;
  background-size: cover;
  filter: blur(1px) brightness(70%) saturate(100%);
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  z-index: -1;
}


Custom background on Kanban board
Source

Bigger Preview Popover

This CSS snippet will increase the popover on the links inside Obsidian. This is helpful when you have large information on notes and you want to see more of them that note rather than just a small part.

.popover.hover-popover > .markdown-embed {
    height: 100%;
    max-height: 60vh;
    max-width: 60vh;    
    overflow: scroll;
}

Source

Canvas Cards with Images

This CSS snippet adds an image top on the canvas cards.

.canvas img[alt~="canvas-top"] {
 position: relative;
 left: -24px;
 top: -24px;
 object-fit: cover;
 width: calc(100% + 48px);
 max-width: none;
 display: block;
 margin-bottom: -12px;
}


Source
Source

Kanban Redesign CSS Snippet

Fan of kanban or use kanban on daily basis? This snippet will improve your experience with Kanban.

Learn how to use it on your vault from here. Kudos to TheKoTech for creating this as well as the previous snippet.


Source

Blockquote Hover Effect

This snippet adds a hover effect on quotes in the preview mode inside Obsidian.

/* quote container */
.markdown-preview-view .quoteback {
  border: 1px solid #c2dfe3;
  border-radius: 8px;
  color: rgb(70, 74, 77);
  padding: 1rem 1rem 0rem 1rem;
  position: relative;
}
/* make border darker on hover */
.markdown-preview-view .quoteback:hover {
 border: 1px solid #9db8bf;
}
/* quote footer */
.markdown-preview-view .quoteback>footer {
  border-top: 1px solid lightblue;
  font-size: .875rem;
  font-weight: 600;
  margin: 0.5rem -1rem auto -1rem;
  padding: 0.5rem 1rem 0 1rem;
}
/* quote link */
.markdown-preview-view .quoteback>footer>cite>a {
 height: 100%;
 left: 0;
 margin: 0;
 opacity: 0;
 position: absolute;
 top: 0;
 width: 100%;
}
/* quote title */
.markdown-preview-view .quoteback::after {
  display: block;
  color: rgb(92, 109, 115);
  content: attr(data-title);
  font-size: .875rem;
  font-weight: 600;
  margin: 0 -1rem;
  padding: 0 1rem 0.5rem 1rem;
}
blockquote {
  transition-duration: 0.2s;
}
blockquote:hover {
  box-shadow: 0 10px 16px lightgrey;
  transform: translateY(-10px);
}


Quotes Callout

This snippet adds a beautiful quote-styled callout.

.callout[data-callout="quote"] {
    display: flex;
    flex-direction: column-reverse;
    /* --callout-padding: 8px 1rem; */
  }.callout[data-callout="quote"] > .callout-title {
    /* margin-block: .5em; */
   text-indent: 1.25em;
  }
.callout[data-callout="quote"] > .callout-title > .callout-icon,
  .callout[data-callout="cite"] > .callout-title > .callout-icon {
    transform: scale(-1, 1);
  }
  .callout[data-callout='quote'] .callout-content p/* ,
.callout[data-callout='cite'] .callout-content p  */{
   margin-top: 0;
}


Minimal Cards CSS

One of the major features of minimal theme is Cards view of dataview tables. But it doesn’t work with other themes. To do so, you have to strip out the CSS snippet and make some changes. This CSS snippet will work with any obsidian theme to create cards view in dataview table query.


Clean Embeds CSS

This CSS snippet will change the embedding style inside the note and make it look like a note itself.

Source

Centered Heading 1

This aligns the H1 in your markdown notes to the center.

Centered H1
/* EDIT MODE */
.HyperMD-header.HyperMD-header-1 {
    text-align: center;
}
/* PREVIEW MODE */
.markdown-preview-view h1 {
    text-align: center;
}

Add a custom background

This CSS snippet allows you to set a custom background image to your vault. 

Source

Dashboard CSS 

Created by TFThacker, this CSS snippet helps you to create a beautiful-looking dashboard inside Obsidian.


Dashboard CSS
source

Daily Notes CSS

This CSS snippet creates links to the previous day’s daily note, tomorrow’s daily note, and a year ago’s daily note. 

Learn how to use this snippet

Media Grid CSS

Meta grid CSS creates a more visually interesting markdown note by grouping sets of images, videos, and even audio tracks in a grid layout. 


Source

Rainbow outline Indents

It creates rainbow-colored indented lists inside obsidian. 


Source

PDF page break Export

This CSS snippet makes it easy to export your note to PDF. There will always be a page break before an H1 heading. 

/* Page breaks */
@media print {
  h1 { 
    page-break-before: always;
  }
  h2, h3, h4, h5, h6 {
    page-break-after: avoid;
  }
  /* optional */
  .internal-embed{
    page-break-after: avoid;
    page-break-before: avoid;}
}

If you want to get a page break even after h2 and h3, edit the code according to your preferences. 

Source

Pretty Highlights

This CSS snippet helps you to separate text blocks in your note using realistic highlighting colors. 


Source

Pretty Tables

This is a CSS snippet for Tables. It helps you customize tables in obsidian to look pretty and appealing. 


Source

Scrollable Slides

The slides plugin creates slideshows from your notes where — — — acts as a slide unit. And the slides are not much responsive with the core plugin. When you add more content to the slide, it overflows and the content is hidden below the container. 

This CSS snippet adds a scrollbar so that all the content can be viewed during the slideshow. 

Source

Tasks Redesign

This CSS snippet redesigns the dialog popup of tasks to make it cleaner and easier to navigate. 


Source

Vertical Kanban

By default, Kanban works in horizontal mode. With this CSS Snippet works in vertical mode. This is really helpful if you want to put Kanban board in the sidebar and operate from there. 


WWW icon next to the Link

This is another CSS snippet that adds a www icon next to all external links inside your vault. 



.theme-dark .external-link {
    color:blanchedalmond !important;
    font-size: 1.01em!important;
    font-weight:500;
    background-position: left!important;
    background-repeat: no-repeat!important;
    background-image: linear-gradient(transparent, transparent), url(https://i.imgur.com/As68C4R.png)!important;
    background-size: 30px!important;
    padding:10px 2px 10px 35px!important;
    background-position-y: 0px!important;
    cursor: pointer!important;
  }
  
  .theme-light .external-link {
    color:chocolate !important;
    font-size: 1.01em!important;
    font-weight:500;
    background-position: left!important;
    background-repeat: no-repeat!important;
    background-image: linear-gradient(transparent, transparent), url(https://i.imgur.com/As68C4R.png)!important;
    background-size: 30px!important;
    padding:10px 2px 10px 35px!important;
    background-position-y: 0px!important;
    cursor: pointer!important;
  }

Zoom Image on Hover

This CSS snippet creates a zoom effect on the images you have on your vault when you hover over them. 

Source

Folder & File Icon

This CSS snippet adds a small icon on the left side of folders and files in the file explorer.


Folder & File Icons
.nav-folder-children .nav-file-title-content:first-child::before {
    content: "\e924  ";
    font-family: 'IcoMoon-Free';
  }
  .nav-folder-children .nav-folder-title-content::before {
    content: '\e930  ';
    font-family: 'IcoMoon-Free';
  }

  .nav-folder-children .nav-file-title-content:first-child::before { content: '🗒 '; }
.nav-folder-children .nav-folder-title-content::before { content: '📂 '; }

Hide Ribbon

This CSS snippet hides the ribbon when the sidebar is collapsed. And it will show up when you hover over it.

SourceRainbow Colored Tags

Want to add different colors to your tags instead of the default one? This CSS snippet will help you achieve that.


Source

Rainbow Colored Folders

This CSS snippet adds eye-pleasing colors to folders in obsidian’s file explorer. 


Source

Beautiful Blockquote

This CSS snippet is stripped from the Wiselight theme. It works better in light theme. But if you want to use it with dark theme, you can change the colors to make it suit your personal needs. 


Gradient Workspace

This is my personal favorite one. I prefer to use it whenever possible. It adds gradient colors to all of the vault. I actually stripped this from Royal Velvet Theme. And I’m not a pro at CSS, so it might conflict with the theme you are using. 

But it works for me pretty well.

I really like the visual appearance of obsidian with these bright and eye-pleasing gradient colors. 


If you want to get all of these CSS snippets in one place, I’ve collected them and created a vault that you can download from Buy Me a Coffee or Gumroad.

0
SHARES


PREVIOUS
NEXT

Leave a Reply

Your email address will not be published. Required fields are marked *
Name
 *

Email
 *

Website
Add Comment
 *

Save my name, email, and website in this browser for the next time I comment.
I accept the Privacy Policy*
This site uses Akismet to reduce spam. Learn how your comment data is processed.

Related Posts


Obsidian Showcases: Movie Catalogue, Callouts, Sticky Notes, Homepage, & More
February 17, 2024

Obsidian Meeting Notes Template & Workflow
January 26, 2024

How to Create Multiple Columns On Obsidian
January 13, 2024
Prakash Joshi Pax participates in the Amazon Services LLC Associates Program, an affiliate advertising program designed to provide a means for sites to earn advertising commissions by linking to Amazon.
Social Icons

Copyright © 2024 Prakash Joshi Pax. All rights reserved
