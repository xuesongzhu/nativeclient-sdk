#!/usr/bin/env python

# Copyright (c) 2010 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
Verifies build of an executable with C++ define specified by a gyp define using
various special characters such as quotes, commas, etc.
"""

import os
import TestGyp

test = TestGyp.TestGyp()

# Tests string literals, percents, and backslash escapes.
try:
  os.environ['GYP_DEFINES'] = \
      """test_format='%s\\n' test_args='"Simple test of %s with a literal"'"""
  test.run_gyp('defines-escaping.gyp')
finally:
  del os.environ['GYP_DEFINES']

test.build('defines-escaping.gyp')

expect = """\
Simple test of %s with a literal
"""
test.run_built_executable('defines_escaping', stdout=expect)


# Test multiple comma-and-space-separated string literals.
try:
  os.environ['GYP_DEFINES'] = \
      """test_format='%s and %s\\n' test_args='"foo", "bar"'"""
  test.run_gyp('defines-escaping.gyp')
finally:
  del os.environ['GYP_DEFINES']

test.sleep()
test.touch('defines-escaping.c')
test.build('defines-escaping.gyp')

expect = """\
foo and bar
"""
test.run_built_executable('defines_escaping', stdout=expect)


# Test string literals containing quotes.
try:
  os.environ['GYP_DEFINES'] = \
     ("""test_format='%s %s %s %s %s\\n' """ +
      """test_args='"\\"These,\\"",""" +
                """ "\\"words,\\"","""
                """ "\\"are,\\"",""" +
                """ "\\"in,\\"",""" +
                """ "\\"quotes.\\""'""")
  test.run_gyp('defines-escaping.gyp')
finally:
  del os.environ['GYP_DEFINES']

test.sleep()
test.touch('defines-escaping.c')
test.build('defines-escaping.gyp')

expect = """\
"These," "words," "are," "in," "quotes."
"""
test.run_built_executable('defines_escaping', stdout=expect)


# Test string literals containing single quotes.
try:
  os.environ['GYP_DEFINES'] = \
     ("""test_format='%s %s %s %s %s\\n' """ +
      """test_args="\\"'These,'\\",""" +
                """ \\"'words,'\\","""
                """ \\"'are,'\\",""" +
                """ \\"'in,'\\",""" +
                """ \\"'quotes.'\\"" """)
  test.run_gyp('defines-escaping.gyp')
finally:
  del os.environ['GYP_DEFINES']

test.sleep()
test.touch('defines-escaping.c')
test.build('defines-escaping.gyp')

expect = """\
'These,' 'words,' 'are,' 'in,' 'quotes.'
"""
test.run_built_executable('defines_escaping', stdout=expect)


# Test string literals containing different numbers of backslashes before quotes
# (to exercise Windows' quoting behaviour).
try:
  os.environ['GYP_DEFINES'] = \
     ("""test_format='%s\\n%s\\n%s\\n' """ +
      """test_args='"\\\\\\"1 visible slash\\\\\\"",""" +
                """ "\\\\\\\\\\"2 visible slashes\\\\\\\\\\"","""
                """ "\\\\\\\\\\\\\\"3 visible slashes\\\\\\\\\\\\\\""'""")
  test.run_gyp('defines-escaping.gyp')
finally:
  del os.environ['GYP_DEFINES']

test.sleep()
test.touch('defines-escaping.c')
test.build('defines-escaping.gyp')

expect = """\
\\"1 visible slash\\"
\\\\"2 visible slashes\\\\"
\\\\\\"3 visible slashes\\\\\\"
"""
test.run_built_executable('defines_escaping', stdout=expect)


# Test that various scary sequences are passed unfettered.
try:
  os.environ['GYP_DEFINES'] = \
     ("""test_format='%s\\n' """ +
      """test_args='"%PATH%, $foo, &quot; `foo`;"'""")
  test.run_gyp('defines-escaping.gyp')
finally:
  del os.environ['GYP_DEFINES']

test.sleep()
test.touch('defines-escaping.c')
test.build('defines-escaping.gyp')

expect = """\
%PATH%, $foo, &quot; `foo`;
"""
test.run_built_executable('defines_escaping', stdout=expect)


# Test commas and semi-colons preceded by backslashes (to exercise Windows'
# quoting behaviour).
try:
  os.environ['GYP_DEFINES'] = \
     ("""test_format='%s\\n%s\\n' """ +
      """test_args='"\\\\, \\\\\\\\;",""" +
                # Same thing again, but enclosed in visible quotes.
                """ "\\"\\\\, \\\\\\\\;\\""'""")
  test.run_gyp('defines-escaping.gyp')
finally:
  del os.environ['GYP_DEFINES']

test.sleep()
test.touch('defines-escaping.c')
test.build('defines-escaping.gyp')

expect = """\
\\, \\\\;
"\\, \\\\;"
"""
test.run_built_executable('defines_escaping', stdout=expect)

# We deliberately do not test having an odd number of quotes in a string
# literal because that isn't feasible in MSVS.
