---
# Mandatory fields
id: "9338b40f-604b-4095-906d-5a709b24fe6a"
# Optional fields
title: "Dashboard Mater CSS"
tags: ["3c763d", "ebf5eb", "2b542c", "fff", "fff", "fff", "3c763d", "ebf5eb", "2b542c"]
source: ""
source_title: ""
source_description: ""
source_image_url: ""
created_date: "2024-02-18"
modified_date: "2024-02-18"
---



/* Multi-column layout CSS */
.multi-column {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 3 columns */
  grid-gap: 20px; /* Adjust the gap between columns as needed */
  margin-bottom: 20px; /* Adjust the bottom margin for spacing between rows */
}

/* Callout CSS with a green theme */
.callout-green {
  border-left: 3px solid #3c763d; /* Green color for the left border */
  background-color: #ebf5eb; /* Light green background */
  padding: 12px 16px; /* Padding inside the callout */
  margin: 10px 0; /* Margin around the callout */
  border-radius: 5px; /* Rounded corners for the callout */
}

/* Callout heading */
.callout-green-header {
  font-weight: bold;
  color: #2b542c; /* Darker green color for the header text */
  margin-bottom: 5px;
}

/* Callout content */
.callout-green-content {
  font-size: 0.9em;
}

/* CSS */
.button-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: start;
  margin-bottom: 20px; /* Adjust the bottom margin for spacing between rows */
}


<!-- HTML !-->
<button class="button-50" role="button">Button 50</button>

/* CSS */
.button-50 {
  appearance: button;
  background-color: #000;
  background-image: none;
  border: 1px solid #000;
  border-radius: 4px;
  box-shadow: #fff 4px 4px 0 0,#000 4px 4px 0 1px;
  box-sizing: border-box;
  color: #fff;
  cursor: pointer;
  display: inline-block;
  font-family: ITCAvantGardeStd-Bk,Arial,sans-serif;
  font-size: 14px;
  font-weight: 400;
  line-height: 20px;
  margin: 0 5px 10px 0;
  overflow: visible;
  padding: 12px 40px;
  text-align: center;
  text-transform: none;
  touch-action: manipulation;
  user-select: none;
  -webkit-user-select: none;
  vertical-align: middle;
  white-space: nowrap;
}

.button-50:focus {
  text-decoration: none;
}

.button-50:hover {
  text-decoration: none;
}

.button-50:active {
  box-shadow: rgba(0, 0, 0, .125) 0 3px 5px inset;
  outline: 0;
}

.button-50:not([disabled]):active {
  box-shadow: #fff 2px 2px 0 0, #000 2px 2px 0 1px;
  transform: translate(2px, 2px);
}

@media (min-width: 768px) {
  .button-50 {
    padding: 12px 50px;
  }

/* Multi-column layout CSS */
.multi-column {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 3 columns */
  grid-gap: 20px; /* Adjust the gap between columns as needed */
  margin-bottom: 20px; /* Adjust the bottom margin for spacing between rows */
}

/* Callout CSS with a green theme */
.callout-green {
  border-left: 3px solid #3c763d; /* Green color for the left border */
  background-color: #ebf5eb; /* Light green background */
  padding: 12px 16px; /* Padding inside the callout */
  margin: 10px 0; /* Margin around the callout */
  border-radius: 5px; /* Rounded corners for the callout */
}

/* Callout heading */
.callout-green-header {
  font-weight: bold;
  color: #2b542c; /* Darker green color for the header text */
  margin-bottom: 5px;
}

/* Callout content */
.callout-green-content {
  font-size: 0.9em;
}



/* Add the rest of the button CSS provided here */
/* ... */