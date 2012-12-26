Use case:
You have a fciv generated xml file in Windows.
After those files copied to Linux machines, you will need to verify the integrity in Linux.


The generated MD5.xml file will be the input of this script which could be executed in Linux machine.


In Linux machine usage example:

~/parseMD5xml.py MD5.xml > md5.txt

md5sum -c md5.txt

Assume all files are in the same folder.


For more info about fciv: http://support.microsoft.com/kb/841290
The xml file was generated using this command in Windows environment

%path_to_fciv%\fciv %folder% -wp -bp %folder% -xml MD5.xml

Where %folder% will be replaced by the name that you will run the md5 check.

