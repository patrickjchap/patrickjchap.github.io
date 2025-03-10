# LLELLM: Bug Detection

## Bug Types

{% tabs bugs %}

{%tab bugs npe %}

{% tabs graphs %}

{% tab graphs diff %}
```php
var_dump('hello');
```
{% endtab %}

{% tab graphs trace %}
```javascript
console.graphs('hello');
```
{% endtab %}

{% tab graphs total %}
```javascript
pputs 'hello'
```
{% endtab %}

{% endtabs %}

{% endtab %}

{% endtabs %}