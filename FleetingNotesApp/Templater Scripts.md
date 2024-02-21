---
# Mandatory fields
id: "ab4f8c9a-ce6e-4483-97ba-5183c5da1b11"
# Optional fields
title: "Templater Scripts"
tags: ["made", "made"]
source: ""
source_title: ""
source_description: ""
source_image_url: ""
created_date: "2024-02-20"
modified_date: "2024-02-21"
---



PRAKASH JOSHI PAXOBSIDIAN
Obsidian Templater Snippets I Wish I Knew Sooner
Level up your workflow with these templater scripts

Obsidian Templater Snippets
Templater is a powerful Obsidian community plugin. But most people use it on the base level only. But it can perform much more powerful operations.

The core plugin template is good if you want to do simple templating but for more advanced work, templater is the way. 

I like to call Templater a ‘Templates plugin on Steriods’. 

It allows you to insert variables and functions in your notes to automate a lot of manual work. This can help to create a streamlined workflow in Obsidian. 

In this article, I’m sharing templater snippets to add a lot of pro-level functionalities to the Obsidian app. All of these templater scripts are collected from Templater’s Discussion, Obsidian discord group, Obsidian Forum, and online articles. 

Note: These templater scripts might need some tweaks depending on your actual template, workflow, and needs. 
Today’s Date

This templater snippet adds today’s date in the note. You can change the date format easily. Here is the reference guide.

<% tp.date.now("Do MMMM YYYY") %>


Today’s date from file title

This templater snippet can be useful for your daily notes. It retrieves today’s date in the specified format from the file title. 

This script won’t work if the file name doesn’t have a date. 

<% moment(tp.file.title,'YYYY-MM-DD').format("dddd, MMMM DD, YYYY") %>

Link to previous and next day’s daily note

This templater script is popularly used in daily notes to easily navigate between daily note files. 

Previous day: [[<% fileDate = moment(tp.file.title, 'YYYY-MM-DD').subtract(1, 'd').format('YYYY-MM-DD') %>|Yesterday]]
Next day: [[<% fileDate = moment(tp.file.title, 'YYYY-MM-DD').add(1, 'd').format('YYYY-MM-DD') %>|Tomorrow]]


Day of the year

This template script will display the day of the year. Again it will only work if the note title is a date. 

You can use the date.now function to make it work on notes other than daily notes.

<% moment(tp.file.title, 'YYYY-MM-DD').format("DDD[/365]") %>

Templater Scripts for periodic notes plugin

These templater scripts will work if you have installed the periodic notes plugin. These snippets can be used to create a structured and well-organized periodic notes template in Obsidian.

This day: <% tp.date.now("Do MMMM YYYY") %>
This week: <%tp.date.now("gggg-[W]ww")%>
This month: <%tp.date.now("YYYY-MM")%>


Again, this is using the date.now function. You might have to switch to tp.file.title functions if you want to use these along with periodic note templates. 

Link to last week’s and next week’s Note

This templater script will add a link to last week’s and next week’s weekly note. Depending on the week format you use in your notes, you might need to tweak it a bit. 

Next Week: [[<% moment(tp.file.title, "ww YYYY").add(1, "weeks").format("gggg-[W]ww") %>]]
Last Week: [[<% moment(tp.file.title, "ww YYYY").subtract(1, "weeks").format("gggg-[W]ww") %>]]

Link to all daily notes of the week

This templater script will link to all the daily notes of this week. 

[[<% tp.date.weekday("YYYY-MM-DD", 0, tp.file.title, "YYYY-[W]ww") %>]]
[[<% tp.date.weekday("YYYY-MM-DD", 1, tp.file.title, "YYYY-[W]ww") %>]]
[[<% tp.date.weekday("YYYY-MM-DD", 2, tp.file.title, "YYYY-[W]ww") %>]]
[[<% tp.date.weekday("YYYY-MM-DD", 3, tp.file.title, "YYYY-[W]ww") %>]]
[[<% tp.date.weekday("YYYY-MM-DD", 4, tp.file.title, "YYYY-[W]ww") %>]]
[[<% tp.date.weekday("YYYY-MM-DD", 5, tp.file.title, "YYYY-[W]ww") %>]]
[[<% tp.date.weekday("YYYY-MM-DD", 6, tp.file.title, "YYYY-[W]ww") %>]]

For better formatting, you can also use the following templater snippet.

S [[{{sunday:YYYY-MM-DD}}|{{sunday:DD}}]] · M [[{{monday:YYYY-MM-DD}}|{{monday:DD}}]] · T [[{{tuesday:YYYY-MM-DD}}|{{tuesday:DD}}]] · W [[{{wednesday:YYYY-MM-DD}}|{{wednesday:DD}}]] · T [[{{thursday:YYYY-MM-DD}}|{{thursday:DD}}]] · F [[{{friday:YYYY-MM-DD}}|{{friday:DD}}]] · S [[{{saturday:YYYY-MM-DD}}|{{saturday:DD}}]] ^{{date:ww}}


Link to all weekly notes of the month

This is another templater snippet for periodic notes. It adds a link to all weekly notes of the month. 

Again, depending on the weekly note format you use, you need to tweak it a bit. 

<%*
// Get year and month from note name, assumes format of "YYYY-MM"
const [year, month] = tp.file.title.split("-");

// Momentjs works with months starting at 0 index (January is month 0, February is month 1, etc)
// Subtract one to convert to starting at 0 index
const monthZeroIndex = month - 1;

// Get number of days in month
const monthDate = moment([year, monthZeroIndex]);
const daysInMonth = monthDate.daysInMonth();

// For each day in month
const weeks = [];
for (let dayOfMonth = 1; dayOfMonth <= daysInMonth; ++dayOfMonth) {
// Get week for day of month
const week = moment([year, monthZeroIndex, dayOfMonth]).week();

// If week is a new week, add to list of weeks for month
if (!weeks.some(x => x === week)) {
weeks.push(week);
}
}

// Format weeks to be links, formatted at "[[YYYY-[W]WW]]"
const weeksFormatted = weeks.map(week => (
`[[${year}-W${String(week).padStart(2, "0")}]]`
)).join("\n");
-%>

<% weeksFormatted %>

Build a calendar with a link to daily notes

This templater script creates a calendar view with a link to daily notes in table format. |

sun | mo | tu | we | th | fr | sat | 
|:--:|:--:|:--:|:--:|:--:|:--:|:--:| 
<%* const days = parseInt(moment().daysInMonth()) + parseInt(moment().startOf("month").format("d")) const table = [] table.push("|") for (let i = 0; i < days; i++) { if (i > 0 && i % 7 === 0) { table.push("\n|") } table.push(`[[${moment().day(i).format("YYYY-MM-DD")}]]|`) } tR += table.join("") %>


Automatically create periodic notes

This template snippet will automatically create periodic notes. For that, you can add this template to startup templates. 

This script will check if there is a file for daily, weekly, monthly, and yearly notes in your vault based on the provided path. 

If the file doesn’t exist, it will create one for you in the target location. 

Remember: It will not apply the templates for the periodic notes. It will only create files in the target location. 
You can use the folder templates feature to automatically apply the periodic notes template. 

<%*
async function createIfNotExists(tp, filepath){
if (!(await tp.file.exists(filepath))){
app.fileManager.createAndOpenMarkdownFile(filepath)
}
}

await createIfNotExists(tp, "Journal/Daily Journal/" + tp.date.now("YYYY/YYYY-MM-DD") + ".md")

await createIfNotExists(tp, "Journal/Weekly Journal/" + tp.date.now("YYYY/gggg-[W]ww") + ".md")

await createIfNotExists(tp, "Journal/Monthly Journal/" + tp.date.now("YYYY/YYYY-MM") + ".md")

await createIfNotExists(tp, "Journal/Yearly Journal/" + tp.date.now("YYYY") + ".md")
%>

Or you can also use this templater startup script, which does the work of adding templates as well to the periodic notes. 

<%*
let wk = tp.date.now('GGGG-[W]WW');
let mnth = tp.date.now('MM MMMM');
let qrtr = tp.date.now('Qo [Quarter]');
let yr = tp.date.now('YYYY');
let template = '';

if (!tp.file.exists(wk)) {
template = tp.file.find_tfile('Periodic Note - Weekly');
await tp.file.create_new(template, wk);
};

if (!tp.file.exists('[[Personal/Journal/' + yr + '/' + qrtr + '/' + mnth + '/' + mnth + ']]')) {
template = tp.file.find_tfile('Periodic Note - Monthly');
await tp.file.create_new(template, yr + '/' + qrtr + '/' + mnth + '/' + mnth);
};

if (!tp.file.exists('[[Personal/Journal/' + yr + '/' + qrtr + '/' + qrtr + ']]')) {
template = tp.file.find_tfile('Periodic Note - Quarterly');
await tp.file.create_new(template, yr + '/' + qrtr + '/' + qrtr);
};

if (!tp.file.exists('[[Personal/Journal/' + yr + '/' + yr + ']]')) {
template = tp.file.find_tfile('Periodic Note - Yearly');
await tp.file.create_new(template, yr + '/' + yr);
};
%>

Source

Create a Countdown Timer in Your Notes

Want to use your daily notes to keep an eye on important dates? This templater function will help you do that.

Add the target date and the name of the event. And add it to the top of your daily notes.

<%*
const elixirConfDate = new Date('2024-02-05');
const now = new Date();
const diff = elixirConfDate - now;
const days = Math.floor(diff / (1000 * 3600 * 24));
%><% days %> days until my event!

Add file title as H1

This templater script will automatically add the title of your note as Heading 1. 

# <% tp.file.title %> `

Get a random note

This templater snippet will return a random note from your vault. You can also configure the script to fetch the note from a specific folder.

<%*
const files = app.vault.getFiles()
const random = Math.floor(Math.random() * (files.length - 1))
const randomNote = files[random]
%>

Today's random note is [[<% randomNote.basename %> ]]

Source

Templater web module

This snippet can be used to make web requests. 

For example: You can get a daily quote and new banner images on your daily notes.

// Daily quote
<% tp.web.daily_quote() %>

// Random picture
<% tp.web.random_picture() %>
// Random picture with size
<% tp.web.random_picture("200x200") %>
// Random picture with size and query
<% tp.web.random_picture("200x200", "landscape,water") %>


Source

Automatically move notes to a particular folder

With this templater snippet, you won’t have to manually move a note to a folder. Add this templater snippet to your template note. 

Then whenever you insert that templater, it automatically moves to the target folder. 

<% await tp.file.move("/Review/Goals" + tp.file.title) %>

Callouts Templater Script

This templater script allows you to choose the callout you want to use. Instead of remembering and typing the syntax for callout, it makes your job easy. 

Insert the template where you want to add a callout and It will prompt you for the type of callout you want to use. 

<%*
//get selection
noteContent = await tp.file.selection();

// Check if the selected text has one or two strings
let numberOfStrings = noteContent.split('\n').length;
let titre;
let corps;

if (numberOfStrings === 1) {
// Ingest titre only
titre = noteContent.match(/.*/g)[0];
corps = "";
} else if (numberOfStrings > 1) {
// Ingest titre and corps
titre = noteContent.match(/.*(?=\n.*)/g)[0];
corps = noteContent.match(/(?<=.*\n)(.|\n)*/g).join('\n');
}
console.log(corps);
// list callouts
const callouts = {
note: '🔵 ✏️ Note',
info: '🟢 ℹ️ Info',
todo: '🟢 ✔️ Todo',
asidecleanright: '⚪️ 💬commentaire',
tip: '🌐 🔥 Tip / Hint / Important',
abstract: '🌐 📋 Abstract / Summary / TLDR',
question: '🟡 ❓ Question / Help / FAQ',
quote: '🔘 💬 Quote / Cite',
example: '🟣 📑 Example',
success: '🟢 ✔️ Success / Check / Done',
warning: '🟠 ⚠️ Warning / Caution / Attention',
failure: '🔴 ❌ Failure / Fail / Missing',
danger: '🔴 ⚡️ Danger / Error',
resources: 'resources',
code: 'code',
code2: 'code version 2',
proof: 'transparent callout'
};
// return callout
const type = await tp.system.suggester(Object.values(callouts), Object.keys(callouts), true, 'Select callout type.');
//return fold
const fold = await tp.system.suggester(['None', 'Expanded', 'Collapsed'], ['', '+', '-'], true, 'Select callout fold option.');

//return titler
const title = await tp.system.prompt('Title:', titre , true);

//get array of lines
lines = corps.split('\n');
//make a new string with > prepended to each line
let newContent = "";
lines.forEach(l => {
newContent += '> ' + l + "\n";
})
//remove the last newline character
newContent = newContent.replace(/\n$/, "");
//define callout header
header = "> [!"+type+"]"+fold + " " + title +"\n";
// Return the complete callout block
return header + newContent;
%>


Callout Template
Source

Get the YouTube video details

Take a lot of notes from YouTube videos? This is going to be helpful. 

This template automatically gets the title, Channel name, and upload date for the YouTube link. You can also customize it to fit your needs. 

<%*
let url = await tp.system.clipboard();
let page = await tp.obsidian.request({url});
let p = new DOMParser();
let doc = p. parseFromString(page, "text/html");
let $ = s => doc.querySelector(s);

let qcFileName1 = $("meta[property='og:title']").content;
let qcFileName = qcFileName1.replace(/:/g, "_");
titleName = "🎬 " + qcFileName;
await tp.file.move("/Videos/" + titleName);
let duration2 = $("meta[itemprop='duration']").content.slice(2);
let duration1 = duration2.replace(/M/gi, " Min ") ;
let duration = duration1.replace(/S/gi, " Sec ") ;
%>

---
- `Channel/Host:` <%
$("link[itemprop='name']").getAttribute("content") %>
- `Reference:` Details: <% $("meta[itemprop='description']").content %>
- `Publish Date:` <%
$("meta[itemprop='uploadDate']").content.slice(0, 4) %>
- `Duration`: <% duration %>
- `Status`: Not watched yet
- `Reviewed Date:` [[<%tp.date.now()%>]]

Details: <% $("meta[itemprop='description']").getAttribute("content") %>

For this templater script to work, the youtube link you are trying to get details should be copied to the clipboard first. Then insert this templater script and Boom! You have your video details. 


source

Table of contents

This templater snippet will automatically add a table of contents to your notes. This can be useful if you have a long note. 

Especially in the case of book notes. Insert this templater script and you’ll have a Table of contents for your note at the cursor position.

<%*
// Constants for TOC markers
const markerTOCstart = '>[!SUMMARY]+ Table of Contents';
const markerTOCend = '%%ENDTOC%%';

// Get the active file and its metadata
const activeFile = await this.app.workspace.getActiveFile();
const mdCache = await this.app.metadataCache.getFileCache(activeFile);

// Get the current file content and split it into lines
const fileContent = await tp.file.content;
const fileContentSplit = fileContent.split('\n');

// Check if the file starts with a YAML frontmatter block
let hasYAML = fileContentSplit[0] === '---' && fileContentSplit.indexOf('---', 1) > 0;
let yamlEndLine = hasYAML ? fileContentSplit.indexOf('---', 1) : -1;

// Find existing TOC start and end positions
let TOCstart = fileContentSplit.indexOf(markerTOCstart);
let TOCend = fileContentSplit.indexOf(markerTOCend, TOCstart);

// Remove existing TOC if it exists
if (TOCstart !== -1 && TOCend !== -1) {
fileContentSplit.splice(TOCstart, TOCend - TOCstart + 1);
}

// Initialize an empty array to hold new TOC lines
let newTOC = [];

// Get header limit from user
let header_limit = await tp.system.prompt("Show Contents Down to Which Header Level (1-6)?", "3");

const mdCacheListItems = mdCache.headings;
if (mdCacheListItems && mdCacheListItems.length > 0) {
// Generate new TOC
mdCacheListItems.forEach(item => {
var header_text = item.heading;
var header_level = item.level;

if (header_level <= header_limit) {
let file_title = tp.file.title.replace(/ /g, '%20');
let header_url = header_text.replace(/ /g, '%20');
let header_link = `[${header_text}](${file_title}.md#${header_url})`;
newTOC.push(`>${' '.repeat(header_level - 1) + '- ' + header_link}`);
}
});
}

// Determine where to insert the new TOC
let insertPosition = hasYAML ? yamlEndLine + 1 : 0;
if (TOCstart !== -1) insertPosition = TOCstart;

// Add or remove TOC based on newTOC's content
if (newTOC.length > 0) {
// Insert the new TOC into the file content
fileContentSplit.splice(insertPosition, 0, markerTOCstart, ...newTOC, "", markerTOCend);
} else if (TOCstart !== -1 && TOCend !== -1) {
// Remove the markers when there are no headers
fileContentSplit.splice(TOCstart, TOCend - TOCstart + 1);
}

// Update the file with the new content
await app.vault.modify(activeFile, fileContentSplit.join('\n'));
%>


Source

Obsidian Quick capture template

This template will maintain your workflow when using Obsidian. Instead of opening a new note when you have an idea or a thought, you can let this template do its work. 

This template opens up a text box where you can write your ideas. This way you don’t interrupt your workflow. 

All of your thoughts are stored in a new note called Quick Capture with timestamps. 

<%*
//v1.4: Adding option for including a header for each DNP day to fold

//'first' will add to top of file. 'last' will add to bottom of file
let firstOrLastLine = 'first';

//Name of the Quick Capture file. Do NOT include extension '.md'
let qcFileName = 'Quick Capture';

//Leave this blank if you want to use the default file path location (set to '/' to use root of vault)
let folderOverride = '';

//Add a header for each day to nest the quick capture notes under (only works when firstOrLastLine = 'first')
let bAddHeader = false;

let curDateFormat = '[' + '[' + tp.date.now("YYYY-MM-DD") + ']]';
let finalTimestamp = curDateFormat;
let curTimeFormat = tp.date.now("hh:mm A");
if(curTimeFormat != ''){finalTimestamp = finalTimestamp + ' ' + curTimeFormat}

let qcFolderLocation;
if(folderOverride) {
qcFolderLocation = folderOverride;
} else {
if(this.app.vault.config.newFileLocation != 'current') {
qcFolderLocation = this.app.fileManager.getNewFileParent().path;
} else {
qcFolderLocation = '/';
}
}
if(qcFolderLocation != ''){qcFolderLocation = qcFolderLocation + '/'}
qcFolderLocation = qcFolderLocation.replace(/\/\//g,'/');
if(qcFolderLocation == '/'){qcFolderLocation = ''}
if(qcFolderLocation.startsWith('/')){qcFolderLocation = qcFolderLocation.substring(1)}

let qcFilePath = qcFolderLocation + qcFileName + '.md';
let qcFile = this.app.vault.getAbstractFileByPath(qcFilePath);
if(!qcFile) {
qcFile = await this.app.vault.create(qcFilePath, '');
}

if(qcFile) {
let qcNote = await tp.system.prompt("Enter a Quick Capture note");
let isTodo = qcNote.startsWith(';');
let finalNote = (isTodo ? '- [ ] ' : '') + finalTimestamp + ' - ' + (isTodo ? qcNote.substring(1) : qcNote);
let curContent = await this.app.vault.read(qcFile);
let newContents;
if(firstOrLastLine == 'last'){newContents = curContent + '\n' + finalNote}
else {
if(bAddHeader) {
let curDateHeader = '# ' + curDateFormat;
curContent = curContent.replace('\n' + curDateHeader + '\n\n', '');
newContents = '\n' + curDateHeader + '\n\n' + finalNote + '\n' + curContent;
} else {
newContents = finalNote + '\n' + curContent
}
}
this.app.vault.modify(qcFile, newContents);
}
%>


Source

Speed reading widget template

This template allows you to speed-read your notes. For this templater script to work, you need to add the javascript file from the source link in the obsidian vault. 

Then tell the templater plugin where to look for the .js file and create a template. This template can be used on any open note to show the speed reading too. 


Source

Obsidian scrapers

This is not just one templater script but multiple scripts. It is a mini-collection of templater scripts integrated to get information from different sites with a copied link.

You can see a complete guide on how to set this up on the readme page. 


Source

Extract highlights from a note

This template is based on the Progressive summarization workflow by Tiago Forte. 

When you have highlighted text in your notes, it will create a new note with the highlighted text only.

<%*
//check if an editor is the active view
const editor = app.workspace.activeLeaf?.view?.editor;
if(!editor) return;

const separator = " ... ";

function getHighlight (i) {
const line = editor.getLine(i);
const match = line.matchAll(/==(.*?)==/g);
const heading = line.match(/^(#+)\s/);
const sketch = line.match(/^(!\[\[.*?]])/);
let result = null;
while(!(highlight = match.next()).done) {
result = result ? result + separator + highlight.value[1] : highlight.value[1];
}
if(result) return (heading ? heading[0]:"") + result;
if(sketch) return sketch[0];
return null;
}

let output = [];

const linecount = editor.lineCount();
for(i=0;i<linecount;i++) {
const highlight = getHighlight(i);
if(highlight) output.push(highlight);
}

window.navigator.clipboard.writeText(output.join("\n\n"));
new Notice("Extracted highlights are available on the clipboard.",4000);
%>

Source

Index pages

This is an alternative to dataview. And it has some advantages too. The index page created this way is future-proof. 

This template displays the files that include a wikilink to the current note. And you can also group them by different properties. 

That’s COOL! right?

---
title: <%tp.file.title%>
aliases: <%tp.file.title%> Index
datecreated: <%tp.file.creation_date("YYYY-MM-DD")%>
datemodified: <%tp.date.now("YYYY-MM-DD")%>
---
%% to update page select all, delete, and call [[MD Index Pages]] Template %%

# <%tp.file.title%> Index

Made

<%* const made = DataviewAPI.pages("[[" + tp.file.title + "]]" + 'and #made')
.where(p => p.file.name !="Main Page" && !p.file.folder.includes("Admin/Templates"))
.sort(p => p.file.name, 'asc')
.map(p => p.file.link);
const listMade = DataviewAPI.markdownList(made);
-%>
<%- listMade -%>

To Try
<%* const toTry = DataviewAPI.pages("[[" + tp.file.title + "]]" + 'and !#made')
.where(p => p.file.name !="Main Page" && p.file.folder.includes("Recipes"))
.sort(p => p.file.name, 'asc')
.map(p => p.file.link);
const listToTry = DataviewAPI.markdownList(toTry);
-%>
<%- listToTry -%>

Reference
<%* const reference = DataviewAPI.pages("[[" + tp.file.title + "]]")
.where(p => p.file.folder.includes("Reference"))
.sort(p => p.file.name, 'asc')
.map(p => p.file.link);
const listReference = DataviewAPI.markdownList(reference);
-%>
<%- listReference -%>

Source

Current time with clock emoji

This templater script adds a current time with the corresponding clock emoji. 

<%*
const string = ["🕛","🕧","🕐","🕜","🕑","🕝","🕒","🕞","🕓","🕟","🕔","🕠","🕕","🕡","🕖","🕢","🕗","🕣","🕘","🕤","🕙","🕥","🕚","🕦"];
var currentdate = new Date();
var time = Number((2 * (currentdate.getHours() + currentdate.getMinutes() / 60)).toFixed()) % 24;
tR += tp.date.now("LT ") + string[time];
%>


Source

Process kindle clippings

This template will process your Kindle highlights when you add them to your vault. 

If you are not using third-party tools like Readwise to sync your Kindle highlights, this templater script can come in handy. 

Just drop your clippigs.txt file and use this templater script. 

Then you will have a well-organized kindle highlight for your books. 

<%*
/*
1. Download "My Clippings.txt" from your Kindle and place the file in your Obsidian Vault. If you have don't have "Settings/Files & Links/Detect all file extensions" enabled, you will not see the file, but the file will be there.
2. Open the file containing your downloaded literature note for the book you are reading.
3. Start the script by pressing ALT/OPT+E or opening the Templater insert Template Modal
4. Select "PS - Process Kindle Clippings - v2" or whatever name you've given your script
5. Select the book you want to get the clippings for
6. If you already have imported highlights for the book, the script will detect it and offer you to only load new highlights.
7. When the script is done, the result is placed on the clipboard, you need to manually paste the text into the file
```js
*/
const file = app.metadataCache.getFirstLinkpathDest("My Clippings.txt","")
if(!file) {
new Notice("I could not find 'My Clippings.txt' in your Vault", 6000);
return;
}
new Notice(`Using ${file.path}`);

const myClippingsTxt = await app.vault.read(file);
if(!myClippingsTxt || myClippingsTxt.trim() === "") {
new Notice("Could not load 'My Clippings.txt' or the file is empty");
return;
}

// Define the data structure
const myBooks = new Map();

// Split the myClippingsTxt into separate entries using a regular expression
const entries = myClippingsTxt.split(/\r\n|\r|\n/).join('\n').split('==========\n');

// Process each entry
entries.forEach(entry => {
const lines = entry.trim().split('\n');
if (lines.length < 2) return;

// Extract book title
const title = lines[0].trim();

// Extract page and location
const pageInfo = lines[1].match(/page\s*(\d+)\s*\|\s*location\s*(\d+-?\d*)/i);
const page = pageInfo ? pageInfo[1] : '';
let location = pageInfo ? pageInfo[2] : '';

// Check if location is in the format number-samenumber and replace it
if (/^(\d+)-\1$/.test(location)) {
location = location.split('-')[0];
}

// Extract dateTime
const dateTimeInfo = lines[1].match(/Added on (.+)$/);
const dateTime = dateTimeInfo ? dateTimeInfo[1] : '';

// Check if it's a highlight or a note
const isHighlight = lines[1].includes("Highlight");
const content = lines.slice(2).join('\n').trim();

// Check if this title already exists in the map
if (!myBooks.has(title)) {
myBooks.set(title, []);
}

// Check if there's already an entry for this location
const existingEntry = myBooks.get(title).find(e => e.location === location);
if (existingEntry) {
// Update the existing entry
if (isHighlight) {
existingEntry.highlight = content;
} else {
existingEntry.note = content;
}
} else {
// Create a new entry
const bookData = {
location: location,
page: page,
dateTime: dateTime,
highlight: isHighlight ? content : '',
note: isHighlight ? '' : content
};
myBooks.get(title).push(bookData);
}
});

// Sorting each book's data by location
for (let [book, data] of myBooks.entries()) {
data.sort((a, b) => parseInt(a.location.split('-')[0]) - parseInt(b.location.split('-')[0]));
}

const titles = [...myBooks.keys()];
const title = await tp.system.suggester(titles, titles,false,"Select book from list");

if(!title) {
new Notice("The script was terminated");
return;
}

let lastLocation = null;
const currentFile = app.workspace.activeLeaf.view.file;
if(currentFile) {
const contents = await app.vault.read(currentFile);
const matches = [...contents.matchAll(/\^(\d+(?:\-\d+)?)(?:\n|$)/g)];
lastLocation = matches.length > 0 ? matches[matches.length - 1][1] : null;
lastLocation = lastLocation
? isNaN(parseInt(lastLocation.match(/^\d+/)))
? null
: parseInt(lastLocation.match(/^\d+/))
: null;
if (lastLocation) {
const options = [`Load all highlights`,`Load highlights after location ${lastLocation}`];
const action = await tp.system.suggester(options,options,false,"I found already loaded highlights");
if(!action || action === "Load all highlights") {
lastLocation = null;
}
}
}

const bookData = myBooks.get(title);

const output = [];

(lastLocation ? bookData.filter(a=>parseInt(a.location.split('-')[0]) > lastLocation) : bookData).forEach(item => {
if(item.note !== "" && item.note.match(/^#+\s/)) {
output.push(item.note);
return;
}
if(item.highlight !== "" && item.note !== "" && item.note.trim().match(/^\.h\d/)) {
const heading = "#".repeat(parseInt(item.note.trim().match(/^\.h(\d)/)[1]));
if(heading && heading !== "") {
output.push(`${heading} ${item.highlight}`);
return;
}
}
if(item.highlight === "" && item.note !== "" && item.note.trim().match(/^\.h\d/)) {
return;
}
if(item.highlight !== "") {
output.push(`> ${item.highlight} ^${item.location}`);
}
if(item.note !== "") {
item.note.replaceAll(/(\s|^)\.(\w+)(\s|$)/g, "$1#$2$3");
output.push(`> [!note]\n> ${item.note.split("\n").join("\n> ")}`);
}
});

window.navigator.clipboard.writeText(output.join("\n\n"));
new Notice ("Extracted kindle highlights are available on the clipboard.",4000);
%>

Source

Format Text Selection into Callout Block

This template creates creates a callout block by selecting text in Obsidian.

<%*
//get selection
noteContent = tp.file.selection();
//get array of lines
lines = noteContent.split('\n')
//make a new string with > prepended to each line
let newContent = "";
lines.forEach(l => {
newContent += '> ' + l + "\n";
})
//remove the last newline character
newContent = newContent.replace(/\n$/, "");
//define callout header
header = "> [!quote]-\n"
// Return the complete callout block
return header + newContent;
%>


Source

File creation and modification date

This templater script will add the file creation date and modification date to your notes. Adding this to the frontmatter will be helpful in times when you want to make such query with dataview.

---
creation date: <% tp.file.creation_date() %>
modification date: <% tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %>
---

List all files created today

This templater script is an easy way to create a link to files created today. By the way, you can also use dataview for this task. 

This works perfectly if you add a file creation date as frontmatter in your notes. 

<%*
const today = tp.date.now("YYYY-MM-DD");
// Filter out files that shouldn't be included
const filteredFiles = app.vault.getMarkdownFiles().filter(file => {
const fileCache = app.metadataCache.getFileCache(file);
// If the file has a createdOn field and it's value is today, include it
return fileCache?.frontmatter?.createdOn === today;
});
// Convert list of files into list of links
const links = filteredFiles.map(file => `[[${file.basename}]]`).join("\n");
tR += links;
_%>

Source

Note: These templater scripts might need some tweaks depending on your actual template, workflow, and needs.

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
