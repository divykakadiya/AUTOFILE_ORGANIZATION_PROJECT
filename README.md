-->first,we import  two modules os and shutil. These are inbuilt module. 

--> Now, we take source path.

--> Now, we make list of all the file by using os.listdir.

-->next, we move list of the files in a extension wise into the empty list "exlist" by using .split method and add the files into exlist using .append method

-->Now, we use set method to remove duplicate extension in a list.

-->Now, we take destination path where we transfer our files of list extension wise.

-->using os.mkdir method extension wise folders are created.

-->finally shutil.move method all the files move to destination folder then we run the code.
