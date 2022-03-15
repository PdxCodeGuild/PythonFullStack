# Command Line Cheat Sheet

Check out the [Command Line Crash Course](https://cglab.ca/~morin/teaching/1405/clcc/book/cli-crash-course.html)

Recommended bash emulator for Windows: [cmder](https://cmder.net)

#### Note: this guide is for bash consoles.  Most, but not all, of these command will work on Windows' PowerShell console.

## Read-Only Commands: `pwd` & `ls`
These commands are your best friends when trying to understand where you are in your filesystem and what other files and directories are there with you.

### `pwd`
`pwd`, or **print working directory**, prints the filepath to your working directory, where you currently are:

```sh
> pwd
/Users/pete/code-guild/class_koi
```

The `/` at the very start represents the root of the filesystem.  On Windows, this is the C: drive.  In this Mac filesystem, there is a directory at the root called `Users/`.  Inside of that is the directory for the user `pete/`, and so on and so forth.

#### Note: the `>` in the examples is not something that you type.  It represents the terminal cursor.  You would just type `pwd` in the example above.

### `ls`
`ls`, or **list**, prints out the files and folders in your working directory:

```sh
> ls
0 Intro/  1 Python/  2 Flask/  3 HTML + CSS/  4 Django/  5 JavaScript/  6 Capstone/  code/  koi.png  LICENSE  README.md
```

#### Note: the terms "directory" and "folder" are used interchangeably here.  They mean the same thing.

### `ls -a`
`ls -a` or **list all** is an example of the use of a flag.  The `-a` is a flag that will list hidden files and folders as well:

```sh
> ls -a
.  ..  .git/  .gitignore  0 Intro/  1 Python/  2 Flask/  3 HTML + CSS/  4 Django/  5 JavaScript/  6 Capstone/  code/  koi.png  LICENSE  README.md
```
Now you can see a hidden file: `.gitignore` 

And hidden directories: `.`, `..` & `.git`

#### Note: `.` and `..` are special notations that are always in your working directory. `.` always represents where you currently are and `..` always represents the parent directory.  We'll come back to this later when talking about `cd`.

### `ls [filepath]`
You can also give `ls` a filepath argument.  By default, `ls` shows the contents of the working directory.  But, given a valid filepath to another direcoty, it will list the contents of that one instead:

```sh
> ls code
dustin/  lisa/  pete/
```
The `code/` folder contains folders of the work of students and staff.  Everyone who contributes to the repo will have their own folder here to upload assignments.  `ls code` here shows us the child folders of `code`, one for each staff member.

## Navigation: `cd`

### `cd [filepath]`
`cd`, or "change directory" is used for changing your working directory.  Given a valid filepath to another directory, it will change your working directory to that one.

#### Note: just like Python, `#` can be used for comments in the terminal.  Anything after `#` will be ignored and won't be interpreted as a command:

```sh
> # use pwd to double check where we are
> pwd
/Users/pete/code-guild/class_koi
> # cd into the code directory
> cd code
> # check filepath now
> pwd
/Users/pete/code-guild/class_koi/code
> # see what's inside this folder
> ls
dustin  lisa  pete
```

### `cd ..`
`..` is a special notation that *always* represents the parent folder of the working directory.  Therefore, you can *always* use `cd ..` to "go up" one directory:
```sh
> pwd
/Users/pete/code-guild/class_koi/code
> # we're still in the code folder, let's go back into class_koi
> cd ..
> pwd
/Users/pete/code-guild/class_koi
> # let's go up another and get outside of class_koi
> cd ..
> pwd 
/Users/pete/code-guild
> # by the way, you can chain together a longer filepath to traverse multiple directories in one command
> cd class_koi/code
> pwd
/Users/pete/code-guild/class_koi/code
```

### `cd /`
The previous arguments given to `cd` have been **relative filepaths**.  This is an example of an **absolute filepath**.  `cd /` takes you to the root of your filesystem.  It is the parent folder of all of the data saved on your computer.  Use `ls` there to take a peek at what all is stored at the root.

#### Note: an **absolute filepath** represents the same location in the filesystem no matter where your working directory is.  A **relative filepath** is relative to the working directory.

### `cd ~`
`~` represents the current user's home directory in the file system.  For me, that is `/Users/pete`.  Let's say I've `cd`-ed into many folders and I'm now here:
```sh
> pwd
/Users/pete/code-guild/class_koi/code/lisa/javascript/examples/vueseum
> cd ~
> pwd
/Users/pete
```

#### Note: in most bash terminals, `cd` with no arguments has the same effect as `cd ~`.  Both commands go to the home directory.

## Making and Removing Directories: `mkdir` & `rmdir`

### `mkdir [dirname]`
`mkdir`, or **make directory**, creates a new folder (directory/folder: same difference).  The dirname argument is the name of the new folder you are creating.  Let's say we're inside of the `code/pete/` folder, which is currently empty:
```sh
> pwd
/Users/pete/code-guild/class_koi/code/pete
> ls # shows us nothing becuase there's nothing to show
> mkdir test1
> ls
test1/
> # you can pass multiple arguments to mkdir to create multiple directories at once
> mkdir test2 test3 test4
> ls
test1/  test2/  test3/  test4/
```

### `rmdir [dirname]`
`rmdir`, or **remove directory**, will remove an empty directory.  Like `mkdir`, it can take multiple arguments:

```sh
> pwd
/Users/pete/code-guild/class_koi/code/pete
> ls
test1/  test2/  test3/  test4/
> rmdir test2
> ls
test1/  test3/  test4/
> rmdir test3 test4 test1
> ls
> # we see nothing since it's empty now
```

#### Note: using `rmdir` on a non-empty directory will give you feedback saying the directory is not empty instead of deleting it:
```sh
> pwd
/Users/pete/code-guild/class_koi
> ls # check what's here...
> 0 Intro/  1 Python/  2 Flask/  3 HTML + CSS/  4 Django/  5 JavaScript/  6 Capstone/  code/  koi.png  LICENSE  README.md
> # trying to remove code/, even though it has other directories inside of it:
> rmdir code
rmdir: code: Directory not empty
> ls # see that code is still here
> 0 Intro/  1 Python/  2 Flask/  3 HTML + CSS/  4 Django/  5 JavaScript/  6 Capstone/  code/  koi.png  LICENSE  README.md
```

## Working With Files: `touch`, `cp` & `rm`

### `touch [filename]`
`touch` can be used to **create files**.  It's original purpose was to change the last-modified date of a file to the present.  However, like many of these old Unix commands, it has a secondary effect for which it is *way* more commonly used: if the file does not yet exist, `touch` will create it:
```sh
> # let's say were trying to create a python file
> pwd
/Users/pete/code-guild/class_koi/code/pete/python
> ls
> # we're in my python directory, it's empty right now
> touch lab01.py
> ls
lab01.py
> # touch can also take multiple arguments
> touch lab02.py lab03.py
> ls
lab01.py  lab02.py  lab03.py
```

### `cp [filepath-to-copy] [filepath-to-be-copied-to]`
`cp`, or **copy**, can be used to copy one or many files to another location:
```sh
> ls # let's see the current files
lab01.py  lab02.py  lab03.py
> cp lab01.py lab01_copy.py
> ls
lab01.py  lab01_copy.py  lab02.py  lab03.py
```

You can also pass a directory as the last argument (`[filepath-to-be-copied-to]`) to copy a file to a different directory but with the same filename:
```sh
> mkdir copies
> ls
copies/  lab01.py  lab02.py  lab03.py
> cp lab01.py copies
> ls copies # list what's inside of copies/
lab01.py
> # just like touch or mkdir, you can give multiple arguments of files to copy
> cp lab02.py lab03.py copies
> ls copies
lab01.py  lab02.py  lab03.py
```

### `cp -r`
With the `-r` (**recursive**) flag, you can copy the contents of an entire directory:

```sh
> pwd
/Users/pete/code-guild/class_koi
> ls
0 Intro/  1 Python/  2 Flask/  3 HTML + CSS/  4 Django/  5 JavaScript/  6 Capstone/  code/  koi.png  LICENSE  README.md
> cp -r code code-backup
> ls
0 Intro/  1 Python/  2 Flask/  3 HTML + CSS/  4 Django/  5 JavaScript/  6 Capstone/  code/  code-backup/  koi.png  LICENSE  README.md
> # code-backup/ has the exact same contents as code/
```

### `rm [filepath]`
`rm`, or **remove**, can be used to delete files:

```sh
> pwd
/Users/pete/code-guild/class_koi/code/pete/python
> ls
lab01.py  lab02.py  lab03.py
> rm lab01.py
> ls
lab02.py  lab03.py
```

#### Note: `rm` can be given multiple files to remove.  Removed files are not placed in your trash/recycling and are **permanently** deleted.

### `rm -r`
The `-r` flag indicates recursion.  `rm -r` will recursively delete everything inside of a directory.  Unlike `rmdir`, `rm -r` is what you use to delete a directory that is not empty:

```sh
> pwd
/Users/pete/code-guild/class_koi/code/pete
> ls # see what's in my code folder
javascript/  python/
> ls python # see what's inside of python
lab02.py  lab03.py
> rm -r python # delete the python folder and everything in it
> ls
javascript
```

## `echo`
`echo` does just what it sounds like, given a string it will echo that text back to the shell:

```sh
> echo hello world
hello world
```

#### Note: this might not seem very useful on its own, but you can combine this functionality with other unix tools, like `>`, the **output redirector**:

```sh
> echo "It was a dark and stormy night." > story.txt
```

That command wrote the contents of that string to `story.txt`.  Let's see how we can read its contents with...

## `cat`
`cat`, short for **concatenate**, it is another old Unix command made for the purpose of concatenating the contents of text files.  But, given just filepath as an argument, it will print out the contents of that file:

```sh
> cat story.txt
It was a dark and stormy night.
> # that read the contents of the file
> # let's add more to the end of it
> echo "And they lived happily ever after." >> story.txt
> cat story.txt
It was a dark and stormy night.
And they lived happily ever after.
```

#### Note: `>>` is another **output redirector**, but instead of overwriting the entire contents of the file, it will append that string to the end.

`bat` is a not a standard Unix tool, but a special package that works like `cat` but has other helpful features like syntax-highlighting and line numbers. 

Check out how to install it on the github repo: 

[https://github.com/sharkdp/bat](https://github.com/sharkdp/bat)