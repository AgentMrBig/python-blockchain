**Activate the virtual environment**

\\Test
```
source blockchain-env/bin/activate
NOTE: on windows machine the command is
blockchain-env\Scripts\activate
```

** Install all pachages**

```
pip3 install -r requirements.txt
```

**Run the tests**

Make sure to activate the virtual environment.
```
(in my particular machine, its python, it may be python3 on yours)
python -m pytest backend/tests
```
