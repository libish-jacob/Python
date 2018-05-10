#!/usr/bin/python - on top of the file is a must if you want this to run on linux.


If you are editing with visual studio or other windows editor, then you have to make sure that the line endings are in UNIX format. If not then it will not work in linux.

To do this in VS,

"File > Advanced Save Options" has been removed by microsoft due to "uncommon use". Whatever that means. https://developercommunity.visualstudio.com/content/problem/8290/file-advanced-save-options-option-is-missed.html You can add it back by going to "Tools>Customize", then "Commands" tab, select the drop down next to "Menu Bar" select "File" then "Add Command">File>Advanced Save Options..". You can then reorder it in the file menu by using "move down".
Then goto File->Advanced Save Options and choose the line ending as UNIX.