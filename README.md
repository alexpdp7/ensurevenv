```
$ python3 -m pip install --user git+https://github.com/alexpdp7/ensurevenv.git
```

Once that is installed, you can create executable scripts that start with:

```
#!/usr/bin/env python3
try:
    import ensurevenv
    ensurevenv.get(["some", "packages", "here])
except Exception:
    pass
	
...
```

And when running the script, the script will create a virtual environment, install the dependencies, and then restart in the virtual environment, with the dependencies installed.
