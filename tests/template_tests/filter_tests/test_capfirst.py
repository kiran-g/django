from django.test import SimpleTestCase
from django.utils.safestring import mark_safe

from ..utils import render, setup


class CapfirstTests(SimpleTestCase):

    @setup({'capfirst01': '{% autoescape off %}{{ a|capfirst }} {{ b|capfirst }}{% endautoescape %}'})
    def test_capfirst01(self):
        output = render('capfirst01', {'a': 'fred>', 'b': mark_safe('fred&gt;')})
        self.assertEqual(output, 'Fred> Fred&gt;')

    @setup({'capfirst02': '{{ a|capfirst }} {{ b|capfirst }}'})
    def test_capfirst02(self):
        output = render('capfirst02', {'a': 'fred>', 'b': mark_safe('fred&gt;')})
        self.assertEqual(output, 'Fred&gt; Fred&gt;')
