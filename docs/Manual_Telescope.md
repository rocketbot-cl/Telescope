



# Rocketbot Telescope
  
Module for Rocketbot Telescope  
  
![banner](/imgs/Banner_Telescope.png)

## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  

## How to use this module

To use this module you must:

1. Create project
2. Generate the template
   1. Take a reference point.
   2. Select the data you want to extract.
   3. Save the Template.
   4. Upload and process a file.
   5. Check the extracted data.
3. Save the generated token for the template
4. Create a file called telescope.ini containing:
   [USER]
   user = aaaa@rocketbot.cl
   password = robot1111
   server = http://11.11.1.111/api

## Description of the commands

### Login Telescope
  
Command to login to Telescope
|Parameters|Description|example|
| --- | --- | --- |
|Path to .ini file|Select the .ini file to connect|C:/Users/User/Desktop/file.ini|

### Upload document
  
Upload document to get text
|Parameters|Description|example|
| --- | --- | --- |
|Select File|Select the document to upload to get the text|C:/Users/User/Desktop/document.jpg|
|Template token|Template token in Telescope|RCKU2GKCUP4XB5VW|
|Set to var|Variable where the text obtained will be stored|var|

### Upload documents
  
Upload multiple documents to get text
|Parameters|Description|example|
| --- | --- | --- |
|Select Folder|Select the folder where the documents to upload are located|C:/Users/User/Desktop/folder|
|Template ID|Template ID in Telescope|RCKU2GKCUP4XB5VW|
|Set to var|Variable where the content of the documents will be stored|var|

### Check result status
  
Returns the status of a result
|Parameters|Description|example|
| --- | --- | --- |
|Result Token|Result token of a text extraction process|4YLXHLLD4IXM621P|
|Set to var|Variable where the result of the check will be stored|var|

### Get result
  
Get data from a result
|Parameters|Description|example|
| --- | --- | --- |
|Result token|Result token of a text extraction process|RCKU2GKCUP4XB5VW|
|Set result to var|Variable where the result will be stored||
