# Add Windows sublime to bash

Edit your `.bashrc` file to have an alias to the windows Sublime executable.

```bash
alias subl='"/mnt/c/Program Files/Sublime Text 3/subl.exe"'
```

The Path to where Sublime is installed may be different.

# Make a development directory both Linux and Windows can access.

Move to your Windows user Documents directory.
```bash
cd /mnt/c/Users/<USER_NAME>/Documents
```

Make a development directory and move to it.

```bash
mkdir dev
cd dev
```

Make a link to the development directory from your Linux users home. Then move back to your Linux users home
```bash
ln -s `pwd`\ ~/dev
cd
```

All development should be done in this `dev` directory so both Windows and Linux programs can access it correctly.
