#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by NotSqrt
# Copyright (c) 2014 NotSqrt
#
# License: MIT
#

"""This module exports the Dennis plugin class."""

from SublimeLinter.lint import Linter, util


class Dennis(Linter):

    """Provides an interface to dennis."""

    syntax = 'gettext'
    cmd = 'dennis-cmd lint --reporter line'
    executable = None
    version_args = 'lint'  # no --version flag, so trick it by not providing the file path
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.6.0'
    regex = r'^.*:(?P<line>\d+):(\d+):(?P<code>(?:(?P<error>[E])|(?P<warning>[W]))\d+):(?P<message>.+)$'
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = 'po'
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {
        '--errorsonly:': False,
    }
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*#'
