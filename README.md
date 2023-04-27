# Generate API documentation of any packages on PyPI in seconds

Example:

```
pypi-doc --pack pythran beniget gast
```

Example with specific package version:
```
pypi-doc --pack numpy==1.23.5 pandas==1.5.3
```

Example with custom pydoctor options:
```
pypi-doc --pack pythran --option docformat=google project-name=pythran
```

For repeatable arguments, one may use the literal list format to supply multiple values:

```
pypi-doc --pack pydoctor --option \
    "intersphinx=['https://docs.python.org/3/objects.inv','https://docs.twisted.org/en/stable/api/objects.inv']" \
    "privacy=public:**"
```