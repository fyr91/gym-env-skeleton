# A skeleton for customized gym environment

File structure
```
gym-env-skeleton/
  README.md
  setup.py
  customized_env/
    __init__.py
    envs/
      __init__.py
      customized_env.py
      customzied_extrahard_env.py
```

Add any other dependencies for this customized environment in setup.py

If want to add more environments:
1. Add environment files in `envs` folder
2. Register new environments in `customized_env/__init__.py`
3. Import new environments in `envs/__init__.py`

More info can check https://github.com/openai/gym/blob/master/docs/creating-environments.md
