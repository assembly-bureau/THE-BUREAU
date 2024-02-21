---
# Mandatory fields
id: "0f0f1e94-cdfa-48b6-b449-1b4f827f8b5c"
# Optional fields
title: "Callouts"
tags: ["book/nonfiction"]
source: ""
source_title: ""
source_description: ""
source_image_url: ""
created_date: "2024-02-17"
modified_date: "2024-02-17"
---
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
   note:     '🔵 ✏ Note',
   info:     '🟢 ℹ Info',
   todo:     '🟢 ✔️ Todo',
   asidecleanright: '⚪ 💬commentaire',
   tip:      '🌐 🔥 Tip / Hint / Important',
   abstract: '🌐 📋 Abstract / Summary / TLDR',
   question: '🟡 ❓ Question / Help / FAQ',
   quote:    '🔘 💬 Quote / Cite',
   example:  '🟣 📑 Example',
   success:  '🟢 ✔ Success / Check / Done',
   warning:  '🟠 ⚠ Warning / Caution / Attention',
   failure:  '🔴 ❌ Failure / Fail / Missing',
   danger:   '🔴 ⚡ Danger / Error',
   bug:      '🔴 🐞 Bug',
   recite:   '⚪ 🎞️ recite',
   sommaire: '🟠 📋 sommaire',
   idea:     '🟡 💡 idée',
   daily:    '🔵 📆 daily',
   day:      '⚪ ✒️ day'
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

<%*
//get selection
noteContent = tp.file.selection();
//return fold
const fold = await tp.system.suggester(['None', 'Expanded', 'Collapsed'], ['', '+', '-'], true, 'Select callout fold option.');
//get array of lines
lines = noteContent.split('\n')
//make a new string with > prepended to each line
let newContent = "";
lines.forEach(l => {
	newContent += '> ' + l + "\n";
})
//remove the last newline character
//inset your desired callout after the !
newContent = newContent.replace(/\n$/, "");
//define callout header
header = ">[!tbox]"+fold + "\n"
// Return the complete callout block
return header + newContent;
%>

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
//inset your desired callout after the !
newContent = newContent.replace(/\n$/, "");
//define callout header
header = ">[!tbox]"+ "\n"
// Return the complete callout block
return header + newContent;
%>
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
   note:     '🔵 ✏ Note',
   info:     '🟢 ℹ Info',
   todo:     '🟢 ✔️ Todo',
   asidecleanright: '⚪ 💬commentaire',
   tip:      '🌐 🔥 Tip / Hint / Important',
   abstract: '🌐 📋 Abstract / Summary / TLDR',
   question: '🟡 ❓ Question / Help / FAQ',
   quote:    '🔘 💬 Quote / Cite',
   example:  '🟣 📑 Example',
   success:  '🟢 ✔ Success / Check / Done',
   warning:  '🟠 ⚠ Warning / Caution / Attention',
   failure:  '🔴 ❌ Failure / Fail / Missing',
   danger:   '🔴 ⚡ Danger / Error',
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



Obsidian Grid Callouts
tldr: Jump straight to the implementation.
Arranging Obsidian content in columns without any plugins
Recently, I’ve been looking to rearrange the way I structure notes on books in Obsidian. In order to be able to display, sort and query book notes in various ways, I usually add a ton of metadata in the note’s frontmatter.
It works, but it’s not pretty. Anytime I open a book note there is a gray wall of text to scroll past.
Screenshot of book note in Obsidian. Frontmatter takes up a lot of space.
To make this a bit more manageable, I separated the metadata into fields related to the book (“About”) and my progress (“Reading”). Especially with Obsidian’s 1.0 redesign, callouts have become as nice looking as practical. I moved the fields from the YAML metadata to inline dataview fields.
Screenshot of book note with two callouts full of metadata.
Looks much cleaner and is much easier to scan! However, it still takes up a fair bit of vertical space despite the content not being too long.
Some callout and CSS grid magic and here we go:
Screenshot of Obsidian note with two callouts horizontally next to each other.
I added a bit of styling and am pretty happy with the result:
Screenshot of Obsidian note with both callouts being styled nicely.
Implementation
The two callouts that are displayed side by side are actually encapsulated by another callout. This callout arranges all its content in columns.
Obsidian note showing one larger callout containing two smaller ones within.
This is what it looks like in the note:
> [!even-columns]
>
> > [!abstract] About
> >
> > - Type: #book/nonfiction
> > - [Author:: [[Cal Newport]]]
> > - [pages:: 305]
> > - [ddc:: 650.1]
> > - [Year published:: [[2012]]]
>
> > [!bookinfo] Reading
> >
> > - [status:: read]
> > - [rating:: 4.75]
> > - [added:: 2022-10-29]
> > - [started:: 2022-10-29]
> > - [read:: 2022-10-29]
A CSS snippet in Obsidian applies the styling.
.obsidian/snippets/callouts.css:
/* Even columns */
.callout[data-callout="even-columns"] {
  /* Removes padding and background colour from the container */
  padding: 0;
  background-color: transparent;
}
.callout[data-callout="even-columns"] > .callout-content {
  /* Arranges the content in columns */
  display: grid;
  /* minmax sets the minimum width of a column. Make the columns 'skinnier' by setting 15rem to a smaller number */
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
  gap: 12px;
}
.callout[data-callout="even-columns"] > .callout-title {
  /* Hides the callout title */
  display: none;
}
That’s it! Simply copy the above code into your snippets folder and activate it. Anytime you add a callout with the name even-columns, the content inside is arrange in, well, even columns.
What we are using here is a CSS property called grid. You can read more about grid at CSS-tricks.
The great thing about grid is that it is really flexible. Each new line in our callout automatically moves into a new column.
> [!even-columns]
> left
>
> center
>
> right
Three columns in an Obsidian note.
On a smaller display size, for example on mobile, the columns stack responsively depending on how much space is available.
There are a couple of plugins out there that implement this functionality and might offer a bit more fine-grained control. For a basic use-case like mine, it is quite impressive how far you can get with a callout class and some CSS. It’s great how much customisation Obsidian already supports out of the box.



.callout[data-callout="idea"] {
    --callout-color: 245, 213, 55;
    --callout-icon: lucide-lightbulb;
}

/* don't display title for idea and quote callouts */
.callout[data-callout="idea"] .callout-title-inner,
.callout[data-callout="quote"] .callout-title-inner {
    display: none;
}

/* remove top and bottom margins and add left margin for idea and quote callouts */
.callout[data-callout="idea"] .callout-content p,
.callout[data-callout="quote"] .callout-content p {
    margin-block-start: 0;
    margin-block-end: 0;
    margin-left: .5em;
}

/* align icon and content side-by-side */
.callout[data-callout="idea"],
.callout[data-callout="quote"] {
    display: flex;
    align-items: flex-start;
}

/* v-align icon in center of first line */
.callout[data-callout="idea"] .callout-title .callout-icon,
.callout[data-callout="quote"] .callout-title .callout-icon {
    min-height: 1.5em;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
