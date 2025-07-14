##  Coverage

### coverage

Install
```shell
  pip install coverage
```
Run
```shell
  coverage run -m unittest/pytest/nose2
```
Results

```shell
  coverage report
  coverage html
```

### pytest-cov

```shell
  pip install pytest-cov
```

Run/Results

```shell
  python -m pytest --cov-report html:cov.html --cov=. src/api/ -vs
```

## Retry

Use in cases:

 * External dependencies
 * Asynchronous operations
 * Flaky tests

Install

```shell
  pip install tenacity
```

Example
```python
 @retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=4, max=10))
```

Refs.

> coverage https://pypi.org/project/coverage/

> pytest-cov https://pypi.org/project/pytest-cov/
