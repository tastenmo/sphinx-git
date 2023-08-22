# -*- coding: utf-8 -*-
import os


from datetime import datetime
from docutils.parsers.rst import Directive, directives

import six

from sphinx_git import GitTags

class TestDirective(Directive):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {}
    has_content = True

    node_class = None


options = TestDirective()


table = GitTags(options)

