# renegade-x-configsetter  
Usage:  
``python rxConfigSetter.py marathon\``  
  
Script will look at the provided game directory, match the name to one of the template folders, and then proceeds to scan the files in the template directory.  
Once the files are scanned, they'll be opened, split on '&' and store the setting & value in its memory. Then it will open the game's config files and replace the setting and value.  