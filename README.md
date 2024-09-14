# TestingFramework

First install conda dependencies

```
conda env create -f testing_framework.yaml
```

Activate the environment

```
conda activate testing-framework
```

Wait until all the dependences for conda are installed

```
playwright install
```

Follow steps if required by the console.

Reload the console for changes to take place by using the following command:

Oh-my-zsh : 
```
source ~/.zshrc
```

Bash:
```
~/.bash_profile or ~/.bashrc.
```

Or force close the terminal and reopen it.

To verify the Framework is working as expected you can try the examples provided
using the command:

Navigate to the base directory of the project:

```
cd $PYTHONPATH
```

Web Example:
Then run the API and Web Example:
```
pytest -v tests/web --headless -m smoke
```
or use tags

```
pytest -v tests/ --headless -m web
```

Api Example:
```
pytest -v tests/api -m smoke
```


Get conda up to date:
In order to have conda up to date yo have to run the command:
```
conda update -n base conda
```

If you get an error like this:
``` 
==> WARNING: A newer version of conda exists. <==
  current version: 4.5.11
  latest version: 4.6.4
```

Then your conda-python version has to be updated. You can do it run this command:
```
conda update python
```
and run again:
```
conda update -n base conda
```
