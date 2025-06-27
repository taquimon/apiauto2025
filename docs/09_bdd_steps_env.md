## Steps

### step parameters
You may additionally use parameters in your step names.
These will be handled by either the default simple parser (parse), its extension “cfparse” or
by regular expressions if you invoke
**use_step_matcher().**

* re
```python
@then('The status code is (\d+)')
```
* parse
```python
@then('The status code is {status_code:d}')
```

## Environment

### Functions

```python

    def before_all(context):

    def before_feature(context, feature):

    def before_scenario(context, scenario):

    def after_scenario(context, scenario):

    def after_feature(context, feature):

    def after_all(context):

    def before_tag(context, tag),

    def after_tag(context, tag)
```

### Context Management:
* Context is an object.
* They can store setup results or resources on the context object for use by step implementations.
* The cleanup part of a fixture is automatically triggered when the corresponding context layer (scenario, feature, or test run) is removed.
